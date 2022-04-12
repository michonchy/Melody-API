import pytest
from . import app

def test_download_tmp_path():
    assert app.download_tmp_path("1") == "tmp/1"

def test_change_file_extension():
    assert app.change_file_extension("movie/test.3gpp") == "test.mp3"