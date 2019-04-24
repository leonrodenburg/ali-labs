import sys
import subprocess
from colorama import Fore


def verify():
    result = subprocess.run(["aliyun", "oss", "ls"], capture_output=True)
    if result.returncode == 0:
        succeed("You successfully passed lab 1!")
    else:
        fail("Verification failed, please check all steps and try again")


def succeed(msg):
    print(Fore.GREEN + msg)
    sys.exit(0)


def fail(msg):
    print(Fore.RED + msg)
    sys.exit(1)


if __name__ == "__main__":
    from colorama import init

    init()

    verify()
