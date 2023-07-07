from calculator import app

def test_addition():
    calc = app()
    calc.display.set("2+2")
    calc.result(calc.display)
    assert calc.display.get() == "4"

def test_subtraction():
    calc = app()
    calc.display.set("5-3")
    calc.result(calc.display)
    assert calc.display.get() == "2"

def test_multiplication():
    calc = app()
    calc.display.set("3*4")
    calc.result(calc.display)
    assert calc.display.get() == "12"

def test_division():
    calc = app()
    calc.display.set("6/2")
    calc.result(calc.display)
    assert calc.display.get() == "3.0"

def test_round():
    calc = app()
    calc.display.set("3.14159")
    calc.round(2)
    assert calc.display.get() == "3.14"

def test_divide_by_zero():
    calc = app()
    calc.display.set("1/0")
    calc.result(calc.display)
    assert calc.display.get() == "UNDEFINED"

def test_infinity():
    calc = app()
    calc.display.set("1e1000")
    calc.result(calc.display)
    assert calc.display.get() == "Inf"
