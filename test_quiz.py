from quiz import validate_name
from quiz import validate_answer


def test_valid_name():
    assert validate_name("Zak") is True


def test_empty_name():
    assert validate_name("") is False


def test_valid_answer():
    assert validate_answer("A") is True


def test_invalid_answer():
    assert validate_answer("X") is False