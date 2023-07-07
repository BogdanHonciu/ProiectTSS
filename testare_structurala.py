from calculator import app
import pytest


@pytest.fixture
def calculator():
    calc = app()
    yield calc


def test_clear(calculator):
    calculator.display.set("123")
    calculator.button_clear.invoke()
    assert calculator.display.get() == ""


def test_addition(calculator):
    calculator.display.set("10+5")
    calculator.result(calculator.display)
    assert calculator.display.get() == "15"


def test_subtraction(calculator):
    calculator.display.set("10-5")
    calculator.result(calculator.display)
    assert calculator.display.get() == "5"


def test_multiplication(calculator):
    calculator.display.set("10*5")
    calculator.result(calculator.display)
    assert calculator.display.get() == "50"


def test_division(calculator):
    calculator.display.set("10/5")
    calculator.result(calculator.display)
    assert calculator.display.get() == "2.0"


def test_division_by_zero(calculator):
    calculator.display.set("10/0")
    calculator.result(calculator.display)
    assert calculator.display.get() == "UNDEFINED"


def test_round(calculator):
    calculator.display.set("3.14159")
    calculator.button_round.invoke()
    assert calculator.display.get() == "3.14"


def test_round_with_invalid_input(calculator):
    calculator.display.set("invalid_input")
    calculator.button_round.invoke()
    assert calculator.display.get() == "UNDEFINED"


def test_get_dot_button_not_found(calculator):
    with pytest.raises(ValueError):
        calculator.get_button("non-existent button")
