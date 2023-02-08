import subprocess
import sys


def install_requirements():
    """Install all requirements for the project."""
    # Install requirements
    subprocess.call([sys.executable, "-m", "pip",
                    "install", "-r", "requirements.txt"])


if __name__ == "__main__":
    install_requirements()
