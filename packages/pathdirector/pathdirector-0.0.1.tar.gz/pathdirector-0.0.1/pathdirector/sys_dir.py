import os
from pathlib import Path


def get_download_dir() -> Path:
    """
    Get the directory path for a user's downloads based on the OS.

    Returns:
        Path: The path to the download directory.
    """
    if os.name == 'nt':  # For Windows
        download_dir = Path(os.environ['USERPROFILE']) / 'Downloads'
    else:  # For Unix-based systems
        download_dir = Path.home() / 'Downloads'

    return download_dir


def get_music_dir() -> Path:
    """
    Get the directory path for a user's music based on the OS.

    Returns:
        Path: The path to the music directory.
    """
    if os.name == 'nt':  # For Windows
        music_dir = Path(os.environ['USERPROFILE']) / 'Music'
    else:  # For Unix-based systems
        music_dir = Path.home() / 'Music'

    return music_dir


def get_pictures_dir():
    """
        Get the directory path for a user's pictures based on the OS.

        Returns:
            Path: The path to the picture directory.
    """
    if os.name == 'nt':  # For Windows
        picture_dir = Path(os.environ['USERPROFILE']) / 'Pictures'
    else:  # For Unix-based systems
        picture_dir = Path.home() / 'Pictures'

    return picture_dir


def get_videos_dir():
    """
        Get the directory path for a user's Videos based on the OS.

        Returns:
            Path: The path to the Videos directory.
    """
    if os.name == 'nt':  # For Windows
        videos_dir = Path(os.environ['USERPROFILE']) / 'Videos'
    else:  # For Unix-based systems
        videos_dir = Path.home() / 'Videos'

    return videos_dir
