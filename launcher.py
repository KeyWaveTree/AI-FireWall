# main과 같은 상단에 기능 추가
import platform
import subprocess
import sys
import time
import psutil


def watchdog(main_pid: int) -> None:
    print(f"Watchdog started with main_pid{main_pid}")

    unset_command = []
    system = platform.system()
    if system == "Windows":
        subprocess.run(["set-window-localproxy.bat"])
        unset_command = ["unset-win-localproxy.bat"]

    elif system == "Darwin":
        subprocess.run(["bash", "./set-mac-localproxy.sh"])
        unset_command = ["bash", "./unset-mac-localproxy.sh"]

    elif system == "Linux":
        subprocess.run(["set-fedora-localproxy.sh"])
        unset_command = ["unset-fedora-localproxy.sh"]

    while True:
        if not psutil.pid_exists(main_pid):
            print(f"PID {main_pid} does not exits. Exting watchdog.")
            result = subprocess.run(unset_command)
            print(f"[watchdog] unset result: {result.returncode}")
            break
        time.sleep(1)


if __name__ == "__main__":
    main_pid = int(sys.argv[1])
    print(f"--------main pid--------- {main_pid}")
    watchdog(main_pid)
