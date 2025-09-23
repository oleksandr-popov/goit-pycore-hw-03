import pytest
import tempfile
import os

from src.task2 import get_cats_info


def write_temp_file(content: str) -> str:
    """Helper to create a temporary file with given content."""
    temp = tempfile.NamedTemporaryFile(delete=False, mode="w",
                                       encoding="utf-8")
    temp.write(content)
    temp.close()
    return temp.name


def test_valid_data():
    content = "1,Whiskers,3\n2,Tom,5\n3,Luna,2\n"
    filepath = write_temp_file(content)
    result = get_cats_info(filepath)
    expected = [
        {"id": "1", "name": "Whiskers", "age": 3},
        {"id": "2", "name": "Tom", "age": 5},
        {"id": "3", "name": "Luna", "age": 2},
    ]
    assert result == expected
    os.remove(filepath)


def test_empty_file():
    filepath = write_temp_file("")
    result = get_cats_info(filepath)
    assert result == []
    os.remove(filepath)


def test_file_not_found():
    result = get_cats_info("non_existent_file.txt")
    assert result == []


def test_malformed_line_missing_field():
    content = "1,Whiskers\n2,Tom,5\n"
    filepath = write_temp_file(content)
    with pytest.raises(ValueError):
        # This will raise ValueError due to unpacking error
        get_cats_info(filepath)
    os.remove(filepath)


def test_malformed_line_invalid_age():
    content = "1,Whiskers,three\n"
    filepath = write_temp_file(content)
    result = get_cats_info(filepath)
    assert result == []
    os.remove(filepath)


def test_custom_separator():
    content = "1|Whiskers|3\n2|Tom|5\n"
    filepath = write_temp_file(content)
    result = get_cats_info(filepath, separator="|")
    expected = [
        {"id": "1", "name": "Whiskers", "age": 3},
        {"id": "2", "name": "Tom", "age": 5},
    ]
    assert result == expected
