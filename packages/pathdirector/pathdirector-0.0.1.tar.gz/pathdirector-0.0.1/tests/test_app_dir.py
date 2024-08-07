import os
import pytest
import platform
from unittest.mock import patch
from pathlib import Path
from pathdirector import application_dir


@pytest.fixture
def mock_path_mkdir():
    with patch.object(Path, 'mkdir', return_value=None) as mock_mkdir:
        yield mock_mkdir


def test_get_application_dir_windows_roaming(mock_path_mkdir):
    with patch('platform.system', return_value='Windows'), \
            patch('os.getenv', return_value='C:/Users/User/AppData/Roaming'):
        appname = 'MyApp'
        expected_path = Path('C:/Users/User/AppData/Roaming') / appname
        result = application_dir.get_application_dir(appname, roaming=True)
        assert Path(result) == expected_path
        mock_path_mkdir.assert_called_once()


def test_get_application_dir_windows_non_roaming(mock_path_mkdir):
    with patch('platform.system', return_value='Windows'), \
            patch('os.getenv', return_value=None):
        appname = 'MyApp'
        expected_path = Path.home() / 'Documents' / appname
        result = application_dir.get_application_dir(appname, roaming=False)
        assert Path(result) == expected_path
        mock_path_mkdir.assert_called_once()


def test_get_application_dir_macos(mock_path_mkdir):
    with patch('platform.system', return_value='Darwin'):
        appname = 'MyApp'
        expected_path = Path.home() / 'Library' / 'Application Support' / appname
        result = application_dir.get_application_dir(appname)
        assert Path(result) == expected_path
        mock_path_mkdir.assert_called_once()


def test_get_application_dir_linux(mock_path_mkdir):
    with patch('platform.system', return_value='Linux'):
        appname = 'MyApp'
        expected_path = Path.home() / f'.{appname}'
        result = application_dir.get_application_dir(appname)
        assert Path(result) == expected_path
        mock_path_mkdir.assert_called_once()


if __name__ == "__main__":
    pytest.main()
