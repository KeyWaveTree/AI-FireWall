import os
import subprocess
import sys
import shlex
import time


def clearPreviousPid():
    pid_file = "/tmp/terminal_shell_pid.txt"
    if os.path.exists(pid_file):
        os.remove(pid_file)


def waitForTerminalPid(
    path: str = "/tmp/terminal_shell_pid.txt", timeout: int = 10
) -> int:
    for _ in range(50):
        if os.path.exists(path):
            with open(path) as f:
                return int(f.read())
        time.sleep(0.1)
    raise RuntimeError("No new Terminal shell process found")


# 새로운 콘솔 창을 하나 띄어준다.
def startApp() -> None:
    # creationflags=subprocess.CREATE_NEW_CONSOLE ->
    # macOS에서는 기능이 없어 attribute error가 나온다.
    # return subprocess.Popen(
    #     [sys.executable, "src/app.py"], creationflags=subprocess.CREATE_NEW_CONSOLE
    # )

    # 해결 방법: mac os의 osacript 및 terminal 명령으로 실행
    # 쉘 명령어에서 quote를 사용하여 문자열을 감싸거나 escape 처리(안전하게 사용하기 위하여)
    pythonPath = shlex.quote(sys.executable)
    rootPath = shlex.quote(os.path.abspath("."))  # absolute path로 실행할 app 파일 지정
    cmd = f"cd {rootPath}; {pythonPath} -m src.app"

    # AppleScript로 전달할 명령어
    appleScript = f'tell application "Terminal" to do script "{cmd}"'

    # osascript를 사용하여 새로운 터미널 창에서 실행
    subprocess.Popen(["osascript", "-e", appleScript])


def startLauncher(app_pid):
    return subprocess.Popen(
        [sys.executable, "launcher.py", str(app_pid)],
        stdin=subprocess.DEVNULL,
        start_new_session=True,
    )


def main():
    # 실행하기전 파일 삭제하여 클린한 상태를 유지
    clearPreviousPid()

    # 지금 만들자 마자 프록시 서버 헤제되는 문제 아마 return 프로세스 pid가 아닌 다른 프로세스 pid를 가지고 있을 가능성이 높음.
    # ㄴ>  터미널 창의 pid값이 return 되는 문제 -> 확인 해봤는데 이 문제가 아니였다.
    # ㄴ> "osascript는 터미널 앱에게 "do script 'python -m src.app'" 요청만 전달하고 곧 종료됩니다."
    # app 파일을 먼저 가지고 온다.
    # 현재 실행중인 pid를 출력

    startApp()
    appPid = waitForTerminalPid()
    print(f"app started with PID {appPid} and main pid{os.getpid()}")

    # launcher 파일도 가지고 온다.
    # 왜 launcher 파일을 나중에 가지고 오는가? ->
    launcher_proc = startLauncher(appPid)
    print(f"Launcher started with PID {launcher_proc.pid}")

    # appProc.wait()
    # print("app process exited")

    # 런처 프로세스 종료
    launcher_proc.wait()
    print("Launcher process exited. ")


if __name__ == "__main__":
    main()
