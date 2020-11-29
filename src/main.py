import subprocess
import sys
import os
import tkinter as tk
from tkinter import filedialog

try:
    import questionary as qr
    from github import Github
    import rich
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
    import rich

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
        self.specialCharacters = ["*", "/", "\\", "|", "?", "<", ">", ":"]

    def run(self):
        choices = [
            "Make A Repository Locally",
            "Make A Repository and then push it to GitHub",
        ]

        action = qr.select(
            "Select An Action:",
            choices=choices,
            default=choices[0],
        ).ask()

        if action == choices[0]:
            pass
        elif action == choices[1]:
            pass
        else:
            raise ValueError("Error in Choosing Value!")

    def localRepo(self):
        root = tk.Tk()
        root.withdraw()

        while True:
            folderPath = filedialog.askdirectory(
                title="Choose the directory in which you want to store your project:",
                initialdir="~",
            )
            if folderPath:
                break
            else:
                print("Please Choose a folder path!")

        os.chdir(folderPath)

        while True:
            projectName = qr.text(
                "Enter the Name of the Project:", default="Local Project"
            ).ask()
            for c in projectName:
                if c in self.specialCharacters:
                    print("Invalid Folder Name!")
                    pass
                elif os.path.isdir(projectName) is True:
                    print("Folder already in use!\nTry again")
            else:
                break

        os.mkdir(projectName)

        rich.print(f"[bold green]Folder for {projectName} was successfully created![/]")
        os.chdir(projectName)
        os.mkdir("src")
        os.mkdir("tests")

        venvName = qr.select(
            "Choose a Name for the Virtual Environment:",
            choices=[".env", ".venv", "env", "venv"],
            default=".venv",
        ).ask()

        subprocess.check_call(
            [
                sys.executable,
                "-m",
                "venv",
                venvName,
            ],
            stdout=subprocess.DEVNULL,
            shell=True,
        )
