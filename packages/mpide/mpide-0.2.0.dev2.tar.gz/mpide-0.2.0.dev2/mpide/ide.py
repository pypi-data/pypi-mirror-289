#!/usr/bin/env python3
#                  _     _
#  _ __ ___  _ __ (_) __| | ___
# | '_ ` _ \| '_ \| |/ _` |/ _ \
# | | | | | | |_) | | (_| |  __/
# |_| |_| |_| .__/|_|\__,_|\___|
#           |_|
#
# mpide - MicroPython (Integrated) Development Environment
# Copyright (C) 2024 - Frans Fürst
#
# mpide is free software: you can redistribute it and/or modify it under the terms of the
# GNU General Public License as published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# mpide is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details at <http://www.gnu.org/licenses/>.
#
# Anyway this project is not free for machine learning. If you're using any content of this
# repository to train any sort of machine learned model (e.g. LLMs), you agree to make the whole
# model trained with this repository and all data needed to train (i.e. reproduce) the model
# publicly and freely available (i.e. free of charge and with no obligation to register to any
# service) and make sure to inform the author (me, frans.fuerst@protonmail.com) via email how to
# get and use that model and any sources needed to train it.

"""Magic REPL and file synchronization toolbox"""

# pylint: disable=too-many-branches
# pylint: disable=too-many-statements
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-public-methods
# pylint: disable=fixme

import argparse
import asyncio
import builtins
import io
import logging
import sys
from collections.abc import Iterator, MutableSequence, Sequence
from contextlib import contextmanager, suppress
from pathlib import Path

import yaml
from apparat import fs_changes
from mpremote.main import State  # type: ignore[import-untyped]
from mpremote.transport import TransportError  # type: ignore[import-untyped]
from pydantic import BaseModel
from rich.panel import Panel
from rich.syntax import Syntax
from textual import work
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical
from textual.widgets import Header, Input, Label, RichLog, Switch
from trickkiste.base_tui_app import TuiBaseApp
from trickkiste.logging_helper import apply_common_logging_cli_args
from trickkiste.misc import async_chain

from mpide.utils import async_process_output, load_module, mpyfy

__version__ = "0.2.0.dev2"  # It MUST match the version in pyproject.toml file

STARTUP_HELPTEXT = f"""{'<br>' * 100}
Quick reference
:cat <file>                # plot @file to REPL
:cp <src> <dst>            # copy file from host to target
:ramdisk                   # set up a RAM-disk at /ramdisk
:snippet <name> [<extra>]  # run snippet @name and verbatim @extra if provided
CTRL-A                     # enter raw REPL mode
CTRL-B                     # enter normal REPL mode
CTRL-D                     # soft-reboot
CTRL-E                     # enter paste mode
CTRL-C                     # send keyboard interrupt
CTRL-X                     # quit application
""".replace(
    "<br>", "\n"
)


def log() -> logging.Logger:
    """Returns the logger instance to use here"""
    return logging.getLogger("trickkiste.mpide")


class MpideConfig(BaseModel):
    """Model for shared device/mpide configuration"""

    mpy_cross_path: Path = Path("mpy-cross")
    static_files: Sequence[Path] = []
    dynamic_files: Sequence[Path] = []


class MpIDE(TuiBaseApp):
    """mpide Textual app tailoring all features"""

    MPIDE_DIR = Path(__file__).parent
    CSS_PATH = MPIDE_DIR / "mpide.css"
    PROJECT_CONFIG_FILENAME = "mpide_project.py"

    BINDINGS = [
        Binding("ctrl+x", "app.quit", "Quit", show=True),
        Binding("ctrl+b", "ctrlb"),
        Binding("ctrl+c", "ctrlc"),
        Binding("up", "arrow_up"),
        Binding("down", "arrow_down"),
    ]

    class Prompt(Input):
        """Specialization for Input just in order to re-direct ctrl+d"""

        BINDINGS = [
            # overrides pre-defined Binding
            Binding("ctrl+a", "app.ctrla"),
            Binding("ctrl+d", "app.ctrld"),
            Binding("ctrl+e", "app.ctrle"),
        ]

    class PrintWrapper(io.StringIO):
        """Acts like print() and redirects to log"""

        def __init__(self) -> None:
            self.builtins_print = builtins.print
            super().__init__()

        def __call__(self, *args: object, **kwargs: object) -> None:
            if args == ("no device found",):
                return

            self.builtins_print(  # type: ignore [call-overload]
                *args, **{**kwargs, **{"file": (sio := io.StringIO())}}
            )
            for line in map(str.rstrip, sio.getvalue().split("\n")):
                log().warning("%s", line)

    def __init__(self, args: argparse.Namespace) -> None:
        super().__init__(logger_show_funcname=True, logger_show_tid=False, logger_show_name=False)
        self.code_log = RichLog(id="code-log")
        self.code_log.can_focus = False
        self.repl_input = self.Prompt(id="repl-input")
        self.prefix_label = Label("", id="prefix-label")
        self._mqueue: asyncio.Queue[str] = asyncio.Queue()
        self.history: MutableSequence[str] = []
        self.state = State()
        self.history_cursor = 0
        self.project_dir = args.project_dir
        self.mpide_local_dir = self.project_dir / ".mpide"
        self.mpy_cache_dir = self.mpide_local_dir / "mpy_cache"
        self.title = f"MPIDE - {self.project_dir.relative_to(Path('~').expanduser())}"
        self.project_config = MpideConfig()
        self.mpy_cross_version = ""

    def compose(self) -> ComposeResult:
        """Set up the UI"""
        yield Header(show_clock=True, id="header")
        with Vertical(id="left-pane"):
            yield self.code_log
            with Horizontal(id="input-pane"):
                yield self.prefix_label
                yield self.repl_input
        with Horizontal(classes="container"):
            yield Label("auto-sync", classes="label")
            yield (
                switch_auto_sync := Switch(
                    id="auto-sync",
                    value=True,
                    tooltip=(
                        "Automatically synchronize files tracked"
                        f" in {self.PROJECT_CONFIG_FILENAME} with device."
                    ),
                )
            )
            switch_auto_sync.can_focus = False
        yield from super().compose()
        self._richlog.can_focus = False

    async def initialize(self) -> None:
        """UI entry point"""
        self.set_log_levels((log(), "DEBUG"), ("trickkiste", "INFO"), others_level="WARNING")
        self.add_serial_output(STARTUP_HELPTEXT)
        await asyncio.sleep(0.1)  # wait for window resize updates, to avoid ugly logs
        self.add_serial_output("---")
        # redirect `print` messages from mpremote
        builtins.print = self.PrintWrapper()  # type: ignore [assignment]
        self.ensure_connection()
        self.handle_messages()
        self.mpide_local_dir.mkdir(exist_ok=True)
        with suppress(FileNotFoundError):
            with (self.mpide_local_dir / "command_history.yaml").open(encoding="utf-8") as in_file:
                self.history = yaml.load(in_file, Loader=yaml.Loader)
        await self.load_project_config()
        self.set_status_info()
        if (self.project_dir / self.PROJECT_CONFIG_FILENAME).exists():
            self.watch_fs_changes()
        else:
            self.repl_msg(
                f"[red][bold]Config file {self.PROJECT_CONFIG_FILENAME} not found"
                f" in {self.project_dir}.[/]"
                "\nREPL will still work but auto-syncing and other stuff won't"
            )

    def cleanup(self) -> None:
        """UI shutdown"""
        with (self.mpide_local_dir / "command_history.yaml").open(
            "wt", encoding="utf-8"
        ) as out_file:
            yaml.dump(self.history, out_file)

    async def on_input_submitted(self) -> None:
        """Invoke functionality after pressing Return in input field"""
        await self._mqueue.put(command := self.repl_input.value.rstrip())
        if command:
            if self.history[-1] != command:
                self.history.append(command)
        self.repl_input.value = ""
        self.history_cursor = 0

    async def action_ctrla(self) -> None:
        """React on CTRL-A"""
        await self._mqueue.put(":ctrl-a")

    async def action_ctrlb(self) -> None:
        """React on CTRL-B"""
        await self._mqueue.put(":ctrl-b")

    async def action_ctrlc(self) -> None:
        """React on CTRL-C"""
        await self._mqueue.put(":ctrl-c")

    async def action_ctrld(self) -> None:
        """React on CTRL-D"""
        await self._mqueue.put(":ctrl-d")

    async def action_ctrle(self) -> None:
        """React on CTRL-E"""
        await self._mqueue.put(":ctrl-e")

    async def action_arrow_up(self) -> None:
        """React on UP"""
        self.history_cursor = max(self.history_cursor - 1, -len(self.history))
        with suppress(IndexError):
            self.repl_input.value = self.history[self.history_cursor]

    async def action_arrow_down(self) -> None:
        """React on DOWN"""
        self.history_cursor = min(self.history_cursor + 1, 0)
        with suppress(IndexError):
            self.repl_input.value = self.history[self.history_cursor] if self.history_cursor else ""

    @work(exit_on_error=True)
    async def ensure_connection(self) -> None:
        """Continuously tries to connect"""
        show_message = True
        while True:
            if self.state.transport:
                await asyncio.sleep(1)
                continue
            try:
                if show_message:
                    log().info("connect..")
                self.state.ensure_friendly_repl()
                self.state.did_action()
                self.state.transport.serial.write(b"\r\n")
                self.print_serial()
                self.set_status_info()
            except SystemExit:
                if show_message:
                    log().error("mpremote could not connect to any device")
                self.abort_connection()
            except Exception as exc:  # pylint: disable=broad-except
                log().error("%s", exc)
            await asyncio.sleep(2)
            show_message = False

    @contextmanager
    def raw_repl(self) -> Iterator[None]:
        """Convenience decorator for entering raw repl"""
        try:
            self.state.transport.enter_raw_repl(soft_reset=False)
            yield
        finally:
            self.state.transport.exit_raw_repl()

    def repl_msg(self, msg: str) -> None:
        """Write a flashy message supporting markups to the REPL"""
        self.code_log.write(Panel(msg))

    @work(exit_on_error=True)
    async def handle_messages(self) -> None:
        """Reads messages from a queue and operates on serial. This is the only function
        allowed to write to serial to avoid conflicts (thus the queue)"""
        while True:
            element = await self._mqueue.get()
            log().debug("got element %s", element)
            try:
                if not self.state or not self.state.transport:
                    self.repl_msg("[yellow bold]no device connected")
                elif element == ":ctrl-a":
                    self.repl_msg("send CTRL-A (enter raw REPL) to device..")
                    self.state.transport.serial.write(b"\r\x01")
                elif element == ":ctrl-b":
                    self.repl_msg("send CTRL-B (leave raw REPL) to device..")
                    self.state.transport.serial.write(b"\r\x02")
                elif element == ":ctrl-d":
                    self.repl_msg("send CTRL-D (soft-reboot) to device..")
                    self.state.transport.write_ctrl_d(self.add_serial_output)
                elif element == ":ctrl-c":
                    self.state.transport.serial.write(b"\x03")
                elif element == ":ctrl-e":
                    self.repl_msg("send CTRL-E (paste mode) to device..")
                    self.state.transport.serial.write(b"\r\x05")
                elif element == ":ramdisk":
                    self.run_snippet(self.MPIDE_DIR / "target/mpide/setup_ramdisk.py")
                elif element.startswith(":snippet "):
                    _, name, *rest = element.split(maxsplit=2)
                    extra_snippet = rest[0] if rest else ""
                    if (path := self.project_dir / f"{name}.py").exists():
                        self.run_snippet(path, extra_snippet)
                    elif (path := self.MPIDE_DIR / f"target/mpide/{name}.py").exists():
                        self.run_snippet(path, extra_snippet)
                    else:
                        self.repl_msg(f"[red bold] no file {name}.py found")
                elif element.startswith(":cp "):
                    _, source_raw, target_raw = element.split()
                    if source_raw.endswith(".py") and target_raw.endswith(".mpy"):
                        source_path = await self.precompiled_from(Path(source_raw))
                    else:
                        source_path = Path(source_raw)
                    # fixme: skip identical files - keep a dict
                    # (source, target) -> hash
                    # and check if copy_cache.get((source, target)==hash
                    with self.raw_repl():
                        # self.state.transport.fs_cp(source, target)
                        log().debug("cp %s %s", source_path, target_raw)
                        with open(source_path, "rb") as in_file:
                            self.state.transport.fs_writefile(target_raw, in_file.read())
                        self.repl_msg(
                            "[blue]copied"
                            f" <project>/[bold]{source_path.relative_to(self.project_dir)}[/]"
                            f" to <device>/[bold]{target_raw}[/]"
                        )
                elif element.startswith(":cat "):
                    _, path = element.split()
                    log().debug("cat %s", path)
                    with self.raw_repl():
                        self.state.transport.exec_raw_no_follow(
                            f"with open('{path}') as f: print(f.read())"
                        )
                else:
                    self.state.transport.serial.write(f"{element}\r\n".encode())
            except TransportError as exc:
                self.repl_msg("[red bold]caught TransportError[/]")
                self.code_log.write(exc)
            except OSError as exc:
                log().error("could not write to serial: %s", exc)
                self.abort_connection()
                self.repl_msg("[red bold]serial communication failed - reset connection")
            except Exception as exc:  # pylint: disable=broad-except
                log().error("could not write: %r", exc)

    def run_snippet(self, path: Path, extra: str = "") -> None:
        """Run snippet contained in file located at @path"""
        log().debug("try to execute %s", path)
        with (path).open() as file:
            snippet = "\n".join(filter(lambda line: line.rstrip(), file.readlines() + [extra]))
        with self.raw_repl():
            try:
                self.state.transport.exec_raw_no_follow(snippet.encode())
                log().debug("executed %d lines", len(snippet.split("\n")))
            except TransportError as exc:
                self.add_serial_output(f"Error: {exc}")

    @work(exit_on_error=True)
    async def print_serial(self) -> None:
        """Reads data from serial and adds it to the output"""
        buffer = b""
        while True:
            try:
                # busy wait for data - we have to go away from mpremote to make this async..
                await asyncio.sleep(0.1)
                if not (num_bytes := self.state.transport.serial.inWaiting()):
                    if buffer:
                        self.add_serial_output(buffer.decode(errors="replace"))
                        buffer = b""
                    continue
                if (dev_data_in := self.state.transport.serial.read(num_bytes)) is not None:
                    buffer += dev_data_in
                    # todo: yield completed lines
            except AttributeError:
                # self.state.transport has already been removed
                return
            except OSError as exc:
                log().error("could not read: %s", exc)
                self.abort_connection()
                return

    def abort_connection(self) -> None:
        """Reset connection and show flashy connection state"""
        self.state = State()
        self.set_status_info()

    def set_status_info(self) -> None:
        """Sets text and color of status bar"""
        connected_device = (
            f"connected to {self.state.transport.device_name}" if self.state.transport else ""
        )
        self.update_status_bar(
            # f" PID: {current_process.pid}"
            # f" / {current_process.cpu_percent():6.1f}% CPU"
            # f" / {len(tasks)} tasks"
            # f" │ System CPU: {cpu_percent:5.1f}% / {int(cpu_percent * cpu_count):4d}%"
            # f" │ mpcross/micropython/idf"
            f" Status: {connected_device or 'not connected'}"
            f" │ mpide v{__version__}"
            f" │ mpy-cross: {self.mpy_cross_version}"
        )
        self._footer_label.styles.background = "#224422" if connected_device else "#442222"
        self.query_one(Header).styles.background = "#224422" if connected_device else "#442222"

    def add_serial_output(self, data: str) -> None:
        """Append stuff to the REPL log"""
        if data == "---":
            self.code_log.write("─" * (self.code_log.size.width - 3))
            return
        *head, tail = data.rsplit("\n", maxsplit=1)
        self.prefix_label.update(tail)
        if head:
            self.code_log.write(
                Syntax(
                    head[0],
                    "python",
                    indent_guides=True,
                    background_color="#222222",
                    word_wrap=True,
                )
            )

    async def load_project_config(self) -> None:
        """Returns held up to date instance of project configuration"""
        with suppress(FileNotFoundError):
            if self.project_dir.as_posix() not in sys.path:
                sys.path.append(
                    self.project_dir.as_posix()
                )  # needed for loading relative stuff inside mpide_project.py
            try:
                if (
                    new_config := MpideConfig.model_validate(
                        load_module(self.project_dir / self.PROJECT_CONFIG_FILENAME).config
                    )
                ) == self.project_config:
                    return
                self.project_config = new_config
                self.mpy_cross_version = "invalid"
                try:
                    stdout, _stderr, _result = await async_process_output(
                        f"{new_config.mpy_cross_path.expanduser()} --version"
                    )
                    self.mpy_cross_version = stdout[0]
                except FileNotFoundError:
                    log().warning(
                        "mpy-cross compiler (`%s`) could not be executed",
                        new_config.mpy_cross_path,
                    )
                    self.mpy_cross_version = "not-found"
                self.set_status_info()
                self.repl_msg("[blue](Re)loaded project configuration[/]")
                return
            except Exception as exc:  # pylint: disable=broad-except
                log().error("could not load %s: %s", self.PROJECT_CONFIG_FILENAME, exc)
                self.repl_msg(
                    f"[red bold]{self.PROJECT_CONFIG_FILENAME} cannot be loaded[/]"
                    "\nconsider all other issues a result and fix your config first."
                )
        self.project_config = MpideConfig()

    def target_path(self, source_path: Path) -> Path | None:
        """Returns the device counterpart of given @source_path as defined in project config,
        None if there is no mapping."""
        for target_base, file_list in (
            ("/", self.project_config.static_files),
            ("/ramdisk", self.project_config.dynamic_files),
        ):
            for path in file_list:
                if (
                    path.parent == source_path.parent
                    and path.stem == source_path.stem
                    and (
                        path.suffix == source_path.suffix
                        or (path.suffix == ".mpy" and source_path.suffix == ".py")
                    )
                ):
                    return Path(target_base) / path
        # todo: add builtins
        return None

    async def precompiled_from(self, path: Path) -> Path:
        """Returns path to precompiled result from @path"""
        mpy_cross = self.project_config.mpy_cross_path
        log().debug("mpy-cross: '%s'", mpy_cross)
        result = await mpyfy(path, mpy_cross.expanduser(), self.mpy_cache_dir)
        self.repl_msg(
            f"[blue]precompiled [bold]{result.relative_to(self.mpy_cache_dir)}[/]"
            f" from [bold]{path.relative_to(self.project_dir)}[/]"
        )
        return result

    @work(exit_on_error=True)
    async def watch_fs_changes(self) -> None:
        """Watch out for changes on filesystem and automatically update device"""

        async for src_path in async_chain(
            fs_changes(
                self.project_dir,
                min_interval=1,
                additional_ignore_pattern=("/.mpide", "/dev"),
            )
        ):
            if (
                src_path.name.startswith("~")
                or src_path.name.endswith("~")
                or src_path.suffix == ".swp"
            ):
                continue

            # since there's no trivial way to know if `mpide_project.py` is affected by any
            # change we (re)load it unconditionally
            await self.load_project_config()

            if not self.query_one("#auto-sync", Switch).value:
                log().debug("auto-synchronization with device deactivated")
                continue

            rel_src_path = src_path.relative_to(self.project_dir)
            if (target_path := self.target_path(rel_src_path)) is None:
                log().debug("%s not tracked", rel_src_path)
                continue

            log().debug("changed: %s", rel_src_path)
            log().debug("target_path: %s", target_path)
            try:
                intermediate_file = (
                    (await self.precompiled_from(src_path))
                    if src_path.suffix == ".py" and target_path.suffix == ".mpy"
                    else src_path
                )
                await self._mqueue.put(f":snippet unload_module unload_module('{target_path}')")

                # fixme: no clue why this is needed - without it, the snippet won't be
                # executed..
                await asyncio.sleep(0.5)

                await self._mqueue.put(f":cp {intermediate_file} {target_path}")

            except FileNotFoundError as exc:
                log().error("%s", exc)


def main() -> None:
    """Entry point for mpide application"""
    parser = apply_common_logging_cli_args(argparse.ArgumentParser())
    parser.add_argument(
        "project_dir", type=lambda p: Path(p).resolve().absolute(), nargs="?", default="."
    )
    MpIDE(parser.parse_args()).execute()


if __name__ == "__main__":
    main()
