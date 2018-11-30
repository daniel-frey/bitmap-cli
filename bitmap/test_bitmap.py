from .bitmap import Bitmap
import pytest


source = 'bmp.bmp'


def test_for_file_not_found():
    """Tests invalid file input."""
    actual = 'notfound'
    with pytest.raises(FileNotFoundError):
        assert Bitmap.read_file(actual)


def test_write_file_error():
    """Tests for invalid argument."""
    actual = 'wrong'
    with pytest.raises(TypeError):
        assert Bitmap.write_file(actual)
