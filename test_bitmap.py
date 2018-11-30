from bitmap import Bitmap
import pytest


source = 'bmp.bmp'


def test_for_file_not_found():
    """Tests invalid file input."""
    actual = 'notfound'
    with pytest.raises(FileNotFoundError):
        assert Bitmap.read_file(actual)


# def test_read_file():
#     """Test file read."""


def test_write_invalid_type():
    """Tests for invalid arguments in file type."""
    actual = ''
    with pytest.raises(ValueError):
        assert Bitmap.write_file(source, actual)


def test_write_file_error():
    """Tests for invalid filetype."""
    actual = 'wrong'
    with pytest.raises(TypeError):
        assert Bitmap.write_file(actual)
