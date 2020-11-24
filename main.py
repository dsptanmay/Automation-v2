__author__ = "Tanmay Deshpande"
import os
from os import path

from setup import setup

try:
    setup()
except Exception as e:
    exit()
else:
    import questionary as qr
    from github import Github
    from rich import print


class App:
    def __init__(self) -> None:
        term = os.get_terminal_size()
        print("-" * term.columns)
        print("Repo Automation".center(term.columns))
        print("-" * term.columns)
        self.specialCharacters = ["/", "\\", "*", "?", ":", "<", ">", "|", '"']

    def run(self):
        actions = [
            "Create A Project Locally",
            "Create a Project and Make A Repo for it on GitHub",
            "EXIT",
        ]
        while True:
            action = qr.select(
                "Choose an action:",
                choices=actions,
                default=actions[0],
                qmark=">>>",
            ).ask()

            if action == actions[0]:
                self.localProject()
            elif action == actions[1]:
                self.gitHubProject()
            elif action == actions[2]:
                print("Exiting the program...")
                exit(0)
            else:
                print("Error in choosing action!")
                exit()

    def localProject(self):
        """Method for creating local Project"""
        while True:
            projectName = qr.text(
                "Enter the name of the Project:",
                default="Git Project",
                qmark=">>>",
            ).ask()
            chars = [c for c in projectName]
            for i in chars:
                if i in self.specialCharacters:
                    print("Invalid Directory!\nTry Again")
                    return
            else:
                break
        while True:
            projectPath = qr.text(
                "Enter the Folder Inside which you want to store your project: "
            ).ask()
            if path.isdir(projectPath):
                print("[bold blue]  Directory Validated Successfully![/]")
                break
            else:
                print("Invalid directory!")

        try:
            os.chdir(projectPath)
            os.mkdir(projectName)
        except Exception as e:
            print(e)
        else:
            print("[bold green]  Project Folder succesfully created![/]")

        try:
            os.chdir(projectName)
        except Exception as e:
            print(f"[bold red] {e}[/]")
            exit()
        else:
            os.mkdir("tests")
            os.mkdir("src")
            print(
                "[italic red]src[/] and [italic red]tests[/] folders successfully created!"
            )

    def gitHubProject(self):
        """Method for creating GitHub Project"""
        pass


if __name__ == "__main__":
    app = App()
    app.run()
