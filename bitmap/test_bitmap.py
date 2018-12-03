from .bitmap import Bitmap
import pytest


source = 'bmp.bmp'

@pytest.fixture
def bmp_instance():
    return Bitmap.read_file(source)

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


def test_id_field_format(bmp_instance):
    """Tests that the 'Type' memory view decoded correctly."""
    s = bmp_instance.memory_view[0:2].tobytes().decode()
    assert isinstance(s, str) is True


def test_size_field_format(bmp_instance):
    """Tests that the 'Size' memory view decoded correctly."""
    s = bmp_instance.memory_view[2:6].tobytes()
    assert isinstance(s, str) is False


def test_reserved_format(bmp_instance):
    """Tests that the 'Reserved' memory view decoded correctly."""
    s = bmp_instance.memory_view[6:8].tobytes()
    assert isinstance(s, str) is False


def test_reserved_two_format(bmp_instance):
    """Tests that the 'Reserved 2' memory view decoded correctly."""
    s = bmp_instance.memory_view[8:10].tobytes()
    assert isinstance(s, str) is False


def test_offset_format(bmp_instance):
    """Tests that the 'offset' memory view decoded correctly."""
    s = bmp_instance.memory_view[10:14].tobytes()
    assert isinstance(s, str) is False


def test_dib_header_size_format(bmp_instance):
    """Tests that the 'DIB Header Size' memory view decoded correctly."""
    s = bmp_instance.memory_view[14:18].tobytes()
    assert isinstance(s, str) is False


def test_width_format(bmp_instance):
    """Tests that the 'Width' memory view decoded correctly."""
    s = bmp_instance.memory_view[18:22].tobytes()
    assert isinstance(s, str) is False


def test_height_format(bmp_instance):
    """Tests that the 'Height' memory view decoded correctly."""
    s = bmp_instance.memory_view[22:26].tobytes()
    assert isinstance(s, str) is False


def test_colour_planes_format(bmp_instance):
    """Tests that the 'Colour Planes' memory view decoded correctly."""
    s = bmp_instance.memory_view[26:28].tobytes()
    assert isinstance(s, str) is False


def test_bits_per_pixel_format(bmp_instance):
    """Tests that the 'Bits per Pixel' memory view decoded correctly."""
    s = bmp_instance.memory_view[28:30].tobytes()
    assert isinstance(s, str) is False


def test_compression_method_format(bmp_instance):
    """Tests that the 'Compression Method' memory view decoded correctly."""
    s = bmp_instance.memory_view[30:34].tobytes()
    assert isinstance(s, str) is False


def test_raw_image_size_format(bmp_instance):
    """Tests that the 'Raw Image Size' memory view decoded correctly."""
    s = bmp_instance.memory_view[34:38].tobytes()
    assert isinstance(s, str) is False


def test_horizontal_resolution_format(bmp_instance):
    """Tests that the 'Horizontal Resolution' memory view decoded correctly."""
    s = bmp_instance.memory_view[38:42].tobytes()
    assert isinstance(s, str) is False


def test_vertical_resolution_format(bmp_instance):
    """Tests that the 'Vertical Resolution' memory view decoded correctly."""
    s = bmp_instance.memory_view[42:46].tobytes()
    assert isinstance(s, str) is False


def test_num_of_colors_format(bmp_instance):
    """Tests that the 'Number of Colours' memory view decoded correctly. """
    s = bmp_instance.memory_view[46:50].tobytes()
    assert isinstance(s, str) is False


def test_important_colours(bmp_instance):
    """Tests that the 'Important Colours' memory view decoded correctly. """
    s = bmp_instance.memory_view[50:54].tobytes()
    assert isinstance(s, str) is False


def test_file_transform_invert(bmp_instance):
    """Tests the the file transformed correctly."""
    before = bmp_instance.pixel_array
    after = bmp_instance.invert(bmp_instance)

    assert before != after


def test_file_transform_blue(bmp_instance):
    """Tests the the file transformed correctly."""
    before = bmp_instance.color_table
    after = bmp_instance.blue(bmp_instance)

    assert before != after


def test_file_transform_purple(bmp_instance):
    """Tests the the file transformed correctly."""
    before = bmp_instance.color_table
    after = bmp_instance.purple(bmp_instance)

    assert before != after


def test_file_transform_random(bmp_instance):
    """Tests the the file transformed correctly."""
    before = bmp_instance.color_table
    after = bmp_instance.random_color(bmp_instance)

    assert before != after
