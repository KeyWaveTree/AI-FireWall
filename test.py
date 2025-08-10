import subprocess
import os

a = f"cd {os.getcwd()}; zsh %s"

subprocess.run(["zsh", "./set-mac-localproxy.sh"])
