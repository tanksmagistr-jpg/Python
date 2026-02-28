import pytest
from string_utils import StringUtils

utils = StringUtils()

# ----------------------------------------------------------
# Тесты для метода capitalize
# ----------------------------------------------------------
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("123", "123"),
    ("", ""),
    ("already Capitalized", "Already capitalized"),  # остальные символы становятся строчными
    ("SKYPRO", "Skypro"),
    (" first space", " first space"),  # пробел в начале - первый символ не буква
])
def test_capitalize_positive(input_str, expected):
    assert utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_val, expected_exception", [
    (None, AttributeError),
    (123, AttributeError),        # у int нет метода capitalize
    ([], AttributeError),
    ({"a": 1}, AttributeError),
])
def test_capitalize_negative(input_val, expected_exception):
    with pytest.raises(expected_exception):
        utils.capitalize(input_val)

# ----------------------------------------------------------
# Тесты для метода trim
# ----------------------------------------------------------
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("skypro", "skypro"),
    ("   hello world   ", "hello world   "),  # пробелы в конце не удаляются
    ("", ""),
    ("   ", ""),
    ("\t skypro", "\t skypro"),  # табуляция не удаляется (только пробел)
])
def test_trim_positive(input_str, expected):
    assert utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_val, expected_exception", [
    (None, AttributeError),
    (123, AttributeError),
    ([], AttributeError),
])
def test_trim_negative(input_val, expected_exception):
    with pytest.raises(expected_exception):
        utils.trim(input_val)

# ----------------------------------------------------------
# Тесты для метода contains
# ----------------------------------------------------------
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "U", False),
    ("", "", True),                 # пустая строка содержит пустую подстроку
    ("abc", "", True),              # любая строка содержит пустую строку
    ("abc", "abc", True),
    ("abc", "abcd", False),
    ("123", "2", True),
    ("Hello world", "world", True),
    ("Hello world", " ", True),
])
def test_contains_positive(string, symbol, expected):
    assert utils.contains(string, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected_exception", [
    (None, "a", AttributeError),
    ("abc", None, TypeError),       # None не может быть аргументом index
    (123, "a", AttributeError),
    ("abc", 123, TypeError),        # int не может быть аргументом index
])
def test_contains_negative(string, symbol, expected_exception):
    with pytest.raises(expected_exception):
        utils.contains(string, symbol)

# ----------------------------------------------------------
# Тесты для метода delete_symbol
# ----------------------------------------------------------
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("SkyPro", "x", "SkyPro"),
    ("", "", ""),                     # удаление пустой подстроки из пустой
    ("abc", "", "abc"),                # удаление пустой подстроки ничего не меняет
    ("hello world", "o", "hell wrld"),
    ("abacaba", "a", "bcb"),
    ("123321", "3", "1221"),
])
def test_delete_symbol_positive(string, symbol, expected):
    assert utils.delete_symbol(string, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected_exception", [
    (None, "a", AttributeError),
    ("abc", None, TypeError),
    (123, "a", AttributeError),
    ("abc", 123, TypeError),
])
def test_delete_symbol_negative(string, symbol, expected_exception):
    with pytest.raises(expected_exception):
        utils.delete_symbol(string, symbol)