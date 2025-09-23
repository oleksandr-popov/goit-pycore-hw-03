import tempfile
import os

from src.task1 import total_salary


def write_temp_file(content: str) -> str:
    """Helper to create a temporary file with given content."""
    temp = tempfile.NamedTemporaryFile(delete=False, mode="w",
                                       encoding="utf-8")
    temp.write(content)
    temp.close()
    return temp.name


def test_valid_data():
    content = "Alice,1000\nBob,2000\nCharlie,3000\n"
    filepath = write_temp_file(content)
    total, average = total_salary(filepath)
    assert total == 6000.0
    assert average == 2000.0
    os.remove(filepath)


def test_empty_file():
    filepath = write_temp_file("")
    total, average = total_salary(filepath)
    assert total == 0.0
    assert average == 0.0
    os.remove(filepath)


def test_file_not_found():
    filepath = "non_existent_file.txt"
    total, average = total_salary(filepath)
    assert total == 0.0
    assert average == 0.0


def test_invalid_lines():
    content = "Alice,1000\nInvalidLine\nBob,abc\nCharlie,3000\n"
    filepath = write_temp_file(content)
    total, average = total_salary(filepath)
    assert total == 4000.0
    assert average == 2000.0
    os.remove(filepath)


def test_mixed_valid_and_empty_lines():
    content = "\nAlice,1000\n\nBob,2000\n\n"
    filepath = write_temp_file(content)
    total, average = total_salary(filepath)
    assert total == 3000.0
    assert average == 1500.0
    os.remove(filepath)
