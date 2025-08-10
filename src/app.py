import asyncio
import os

# 여기에 없으면 다른 모듈이 다 실행된 후 pid를 가져오기에 프록시 설정하자마자 바로 헤제설정으로 넘어간다.
with open("/tmp/terminal_shell_pid.txt", "w") as f:
    f.write(str(os.getppid()))

from src.firewall.ui import FirewallUI
from src.firewall.controller import Controller
from src.firewall.interceptor.mitmproxy_interceptor import MitmproxyInterceptor
from src.firewall.interceptor.scapy_interceptor import ScapyInterceptor
from src.firewall.logger.logger import Logger
from src.firewall.policy.policy import Policy


class App:
    async def run(self):
        logger = Logger()
        policy = Policy("policy.json")
        controller = Controller(logger, policy)

        # UI 실행
        ui = FirewallUI(controller)

        # UI를 비동기 태스크로 실행하여 이벤트 루프를 점유하지 않고,
        # 다른 작업(패킷 캡처 등)을 동시에 실행할 수 있게 함
        asyncio.create_task(ui.run_async())

        await ui.mounted.wait()
        scapy = ScapyInterceptor(logger)
        scapy.start()

        # Mitmproxy 인터셉터 시작 (Scapy와 동일한 방식)
        mitmproxy = MitmproxyInterceptor(logger, policy)
        mitmproxy.start()

        await asyncio.Event().wait()  # 무한 대기 (앱 종료 방지)


if __name__ == "__main__":
    print("[app.py] starting application")
    app = App()
    asyncio.run(app.run())
    print("[app.py] application exited!")
