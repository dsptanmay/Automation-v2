import subprocess
import sys
import os
import tkinter as tk
from tkinter import filedialog

try:
    import questionary as qr
    from github import Github
    from rich import print
except ImportError:
    subprocess.check_call(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "prompt-toolkit==2.0.10",
            "questionary==1.8.1",
            "pygithub==1.53",
            "rich==9.2.0",
            "black",
            "pylint",
        ],
        stdout=subprocess.DEVNULL,
    )
finally:
    from rich import print

    print("All modules successfully installed!")
    subprocess.check_call(
        ["curl", "https://bootstrap.pypa.io/get-pip.py", "-o", "get-pip.py"],
        stdout=subprocess.DEVNULL,
    )
    subprocess.check_call(
        [sys.executable, "get-pip.py"],
        stdout=subprocess.DEVNULL,
    )
    print("[b red] pip successfully updated![/]")

    import questionary as qr
    from github import Github


class Main:
    def __init__(self) -> None:
        term = os.get_terminal_size()
        print("-" * term.columns)
        print("Python-Github Automation".center(term.columns))
        print("-" * term.columns)
