from src.firewall.command import command
from src.firewall.ui import FirewallUI


class Controller:
    def __init__(self):
        self.ui: FirewallUI

    @command("block")
    async def block_command(self, arg: str):
        self.ui.append_log(f"차단 규칙 적용됨: {arg}")

    @command("allow")
    async def allow_command(self, arg: str):
        self.ui.append_log(f"허용 규칙 적용됨: {arg}")
