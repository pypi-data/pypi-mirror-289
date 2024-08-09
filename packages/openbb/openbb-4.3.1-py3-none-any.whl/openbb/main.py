import os
import subprocess
import sys


def main(build: bool = False):
    # Path to the startup script

    # Set the PYTHONSTARTUP environment variable
    env = os.environ.copy()
    _build = "True" if build else "False"

    # Command to start Python in interactive mode
    command = ["ipython", "-c", f"from openbb import app_builder;obb=app_builder.build({_build})", "-i"]
    #command = ["ipython", "-c", "from openbb import obb", "-i"]

    # Execute the command with the modified environment
    subprocess.run(command, env=env, check=False)  # noqa: S603


if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "build":
        main(build=True)
    else:
        main(build=False)
