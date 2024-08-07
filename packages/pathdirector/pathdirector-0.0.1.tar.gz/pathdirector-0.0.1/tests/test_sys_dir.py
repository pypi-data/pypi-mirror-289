import os
import pytest
from unittest.mock import patch
from pathlib import Path
from pathdirector.sys_dir import get_download_dir, get_music_dir, \
    get_pictures_dir, get_videos_dir


@pytest.fixture
def mock_userprofile():
    with patch.dict(os.environ, {'USERPROFILE': 'C:/Users/User'}):
        yield


@pytest.fixture
def mock_path_home_unix():
    with patch('pathlib.Path.home', return_value=Path('/home/user')):
        yield


def normalize_path(path):
    return str(path).replace('\\', '/')


def test_get_download_dir_windows(mock_userprofile):
    with patch('os.name', 'nt'):
        expected_path = Path('C:/Users/User/Downloads')
        result = get_download_dir()
        assert normalize_path(result) == normalize_path(expected_path)


def test_get_download_dir_unix(mock_path_home_unix):
    with patch('os.name', 'posix'):
        expected_path = Path('/home/user/Downloads')
        result = get_download_dir()
        assert normalize_path(result) == normalize_path(expected_path)


def test_get_music_dir_windows(mock_userprofile):
    with patch('os.name', 'nt'):
        expected_path = Path('C:/Users/User/Music')
        result = get_music_dir()
        assert normalize_path(result) == normalize_path(expected_path)


def test_get_music_dir_unix(mock_path_home_unix):
    with patch('os.name', 'posix'):
        expected_path = Path('/home/user/Music')
        result = get_music_dir()
        assert normalize_path(result) == normalize_path(expected_path)


def test_get_videos_dir_windows(mock_userprofile):
    with patch('os.name', 'nt'):
        expected_path = Path('C:/Users/User/Videos')
        result = get_videos_dir()
        assert normalize_path(result) == normalize_path(expected_path)


def test_get_videos_dir_unix(mock_path_home_unix):
    with patch('os.name', 'posix'):
        expected_path = Path('/home/user/Videos')
        result = get_videos_dir()
        assert normalize_path(result) == normalize_path(expected_path)


def test_get_pictures_dir_windows(mock_userprofile):
    with patch('os.name', 'nt'):
        expected_path = Path('C:/Users/User/Pictures')
        result = get_pictures_dir()
        assert normalize_path(result) == normalize_path(expected_path)


def test_get_pictures_dir_unix(mock_path_home_unix):
    with patch('os.name', 'posix'):
        expected_path = Path('/home/user/Pictures')
        result = get_pictures_dir()
        assert normalize_path(result) == normalize_path(expected_path)


if __name__ == "__main__":
    pytest.main()
