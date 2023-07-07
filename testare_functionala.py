import pytest
from tkinter import *
from calculator import app
from decimal import Decimal


@pytest.fixture(scope="module")
def calculator():
    return app()

def test_addition(calculator):
    calculator.display.set('3+4')
    calculator.result(calculator.display)
    assert calculator.display.get() == '7'


def test_subtraction(calculator):
    calculator.display.set('7-4')
    calculator.result(calculator.display)
    assert calculator.display.get() == '3'

def test_multiplication(calculator):
    calculator.display.set('7*4')
    calculator.result(calculator.display)
    assert calculator.display.get() == '28'

def test_division(calculator):
    calculator.display.set('8/4')
    calculator.result(calculator.display)
    assert calculator.display.get() == '2.0'

def test_clear(calculator):
    calculator.display.set('1237')  # set display to a non-empty string
    calculator.button_clear.invoke()  # simulate a click on the clear button
    assert calculator.display.get() == ''

def test_negative_numbers():
    calculator = app()
    calculator.display.set("-5+3")
    calculator.result(calculator.display)
    assert calculator.display.get() == "-2"

def test_decimal_numbers():
    calculator = app()
    calculator.display.set("2.5+3.7")
    calculator.result(calculator.display)
    assert calculator.display.get() == "6.2"

def test_multiple_numbers():
    calculator = app()
    calculator.display.set("2+3+4")
    calculator.result(calculator.display)
    assert calculator.display.get() == "9"

def test_operator_priority():
    calculator = app()
    calculator.display.set("2+3*4-5")
    calculator.result(calculator.display)
    assert calculator.display.get() == "9"

def test_large_numbers():
    calculator = app()
    calculator.display.set("1000000000000000000000000000000000000000000000000000000000000+1")
    calculator.result(calculator.display)
    expected = Decimal("1e+60")
    actual = Decimal(calculator.display.get()).normalize()
    assert actual == expected

def test_small_numbers():
    calculator = app()
    calculator.display.set("0.0000000000000000000000000000000000000000000000000000000000001+0.0000000000000000000000000000000000000000000000000000000000002")
    calculator.result(calculator.display)
    assert calculator.display.get() == "3e-61"

def test_float_operations():
    calculator = app()
    # Test adunare
    calculator.display.set("2.5+1.25")
    calculator.result(calculator.display)
    assert Decimal(calculator.display.get()) == Decimal("3.75")
    # Test scadere
    calculator.display.set("2.5-1.25")
    calculator.result(calculator.display)
    assert Decimal(calculator.display.get()) == Decimal("1.25")
    # Test inmultire
    calculator.display.set("2.5*1.25")
    calculator.result(calculator.display)
    assert Decimal(calculator.display.get()) == Decimal("3.125")
    # Test impartire
    calculator.display.set("2.5/1.25")
    calculator.result(calculator.display)
    assert Decimal(calculator.display.get()) == Decimal("2")


def test_nan_inf_operations():
    calculator = app()
    # Test division by zero
    calculator.display.set("1/0")
    calculator.result(calculator.display)
    assert calculator.display.get() == "UNDEFINED", "Result should be Inf for division by zero"

    # Test NaN operations
    calculator.display.set("0/0")
    calculator.result(calculator.display)
    assert calculator.display.get() == "UNDEFINED", "Result should be UNDEFINED for NaN operations"


def test_float_overflow():
    calculator = app()
    # Test depasire limite float
    calculator.display.set(str(Decimal('1e400') * Decimal('1e400')))
    calculator.result(calculator.display)
    assert calculator.display.get() == "Inf"

def test_round_float():
    calculator = app()
    # Test rotunjire la 2 zecimale
    calculator.display.set("1.23456789")
    calculator.round(2)
    assert calculator.display.get() == "1.23"
    # Test rotunjire la 5 zecimale
    calculator.display.set("1.23456789")
    calculator.round(5)
    assert calculator.display.get() == "1.23457"

