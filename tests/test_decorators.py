import pytest

from src.decorators import log


def test_log_if_true(tmp_path):
    log_file = tmp_path / "file.txt"

    @log(log_file)
    def add(a, b):
        return a + b

    result = add(1, 2)
    assert result == 3
    assert log_file.exists()


def test_log_if_false():
    log_file = None

    @log(log_file)
    def add(a, b):
        return a + b

    result = add(1, 2)
    assert result == 3
    assert "f add ок"


def test_log_if_exception_true(tmp_path):
    log_file = tmp_path / "error_log.txt"

    @log(filename=str(log_file))
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
    assert log_file.exists()
    content = log_file.read_text(encoding="utf-8")
    assert "divide error: <class 'ZeroDivisionError'>. Inputs: (1, 0)" in content
