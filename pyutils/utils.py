import platform
import os


def clear():
    """Clears the terminal screen."""
    os_name = platform.system().lower()
    if os_name == 'windows':
        os.system('cls')
    elif os_name in ['linux', 'darwin']:
        os.system('clear')
    else:
        print("System not recognized. Could not clear screen.")
