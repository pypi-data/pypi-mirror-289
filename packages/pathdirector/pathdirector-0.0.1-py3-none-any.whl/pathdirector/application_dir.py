import os
from pathlib import Path
import platform


def get_application_dir(appname: str, roaming: bool = False) -> str:
    """
    Get the directory path for a user's application data based on the application name.

    Args:
    appname (str): The name of the application.
    roaming (bool): Whether to use the roaming directory on Windows.

    Returns:
    str: The path to the application data directory.
    """
    system = platform.system()

    if system == 'Windows':
        if roaming:
            app_path = Path(os.getenv('APPDATA')) / appname
        else:
            app_path = Path.home() / 'Documents' / appname
    elif system == 'Darwin':  # macOS
        app_path = Path.home() / 'Library' / 'Application Support' / appname
    else:  # Linux and other Unix-like systems
        app_path = Path.home() / f'.{appname}'

    try:
        app_path.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        print(f"An error occurred while creating the directory: {e}")

    return str(app_path)
