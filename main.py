import os
import subprocess
import sys
import shlex


def startApp():
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
    return subprocess.Popen(["osascript", "-e", appleScript])


def main():
    appProc = startApp()
    print(f"app started with PID {appProc}")

    appProc.wait()
    print("app process exited")


if __name__ == "__main__":
    main()
