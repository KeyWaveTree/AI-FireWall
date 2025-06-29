from __future__ import annotations

import datetime
import sys

from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Input, Static


class FirewallUI(App):
    QUIT_BINDINGS = ["q", "quit", "Quit"]

    _instance: FirewallUI | None = None

    def __init__(self):
        super().__init__()
        FirewallUI._instance = self
        self.log_container = Vertical()

        # 명령어 입력 위젯 생성(
        self.command_input = Input(placeholder="명령어를 입력하세요..")

    @classmethod
    def instance(cls):
        if cls._instance is None:
            raise RuntimeError("Firewall is created not yet")
        return cls._instance

    def compose(self) -> ComposeResult:
        yield self.log_container
        yield self.command_input

    def on_mount(self) -> None:
        self.command_input.focus()

    def append_log(self, message: str, datetime=datetime.datetime.now()) -> None:
        timestemp = datetime.strftime("%H:%M:%S")
        log_line = Static(f"[{timestemp}] {message}")
        self.log_container.mount(log_line)
        self.log_container.scroll_end(animate=False)

    def generate_dummy_message(self):
        self.append_log("더미 로그 데이터 메시지")

    def process_command(self, cmd: str) -> str:
        match cmd:
            case cmd if cmd.startswith("block"):
                return f"차단 규칙 적용{cmd}"
            case cmd if cmd.startswith("allow"):
                return f"허용 규칙 적용됨: {cmd}"
            case _:
                return f"알 수 없는 명령어 {cmd}"

    async def on_input_submitted(self, message: Input.Submitted) -> None:
        cmd = message.value.strip()
        self.command_input.value = ""
        if not cmd: return

        self.append_log(f">{cmd}")
        result = self.process_command(cmd)
        self.append_log(result)

