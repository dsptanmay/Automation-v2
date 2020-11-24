import subprocess as sp
import sys
import pkg_resources


def setup():
    installed = {pkg.key for pkg in pkg_resources.working_set}
    required = {
        "prompt-toolkit==2.0.10",
        "questionary",
        "pygithub",
        "tabulate",
    }
    missing = required - installed

    python = sys.executable
    if missing:
        for module in missing:
            try:
                sp.check_call(
                    [
                        python,
                        "-m",
                        "pip",
                        "install",
                        "--no-cache-dir",
                        module,
                    ],
                    stdout=sp.DEVNULL,
                )
            except Exception:
                print("An error occurred in installing {}".format(module))
            else:
                print("{} was successfully installed!".format(module))
    else:
        print("All modules are already installed!")