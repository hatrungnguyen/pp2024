import os
import subprocess as sp


def os_module():
    while True:
        cmd = input("$ ")
        if cmd == "exit":
            break

        elif cmd == "pwd":
            print(os.getcwd())

        elif cmd.startswith("cd"):
            os.chdir(cmd[3:])

        else:
            os.system(cmd)


def subprocess_module():
    while True:
        cmd = input("$ ")
        if cmd == "exit":
            break

        elif cmd == "pwd":
            print(sp.run(["pwd"], capture_output=True).stdout.decode())

        elif cmd.startswith("cd"):
            sp.run(["cd", cmd[3:]])

        else:
            sp.run(cmd.split())


def main():
    choice = input("os or subprocees take one ")
    match choice:
        case "os":
            os_module()
        case "subprocees":
            subprocess_module()
        case _:
            print("Wrong choice! Should I kill you?")

if __name__ == "__main__":
    main()