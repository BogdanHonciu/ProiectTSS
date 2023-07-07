import pytest
from calculator import app


def test_statement_coverage():
    test_app = app()
    test_app.button_clear.invoke()
    assert test_app.display.get() == ""

    # test all number buttons
    for i in range(10):
        test_app.number_buttons[i].invoke()
        assert test_app.display.get() == str(i)

    # test dot button
    test_app.button_dot.invoke()
    assert test_app.display.get() == "."

    # test round button
    test_app.button_round.invoke()
    assert test_app.display.get() == "UNDEFINED"

    # test addition
    test_app.number_buttons[1].invoke()
    test_app.operation_buttons[0].invoke()
    test_app.number_buttons[2].invoke()
    test_app.operation_buttons[4].invoke()
    assert test_app.display.get() == "3.00"

    # test subtraction
    test_app.button_clear.invoke()
    test_app.number_buttons[5].invoke()
    test_app.operation_buttons[1].invoke()
    test_app.number_buttons[2].invoke()
    test_app.operation_buttons[4].invoke()
    assert test_app.display.get() == "3.00"

    # test multiplication
    test_app.button_clear.invoke()
    test_app.number_buttons[3].invoke()
    test_app.operation_buttons[2].invoke()
    test_app.number_buttons[4].invoke()
    test_app.operation_buttons[4].invoke()
    assert test_app.display.get() == "12.00"

    # test division
    test_app.button_clear.invoke()
    test_app.number_buttons[4].invoke()
    test_app.operation_buttons[3].invoke()
    test_app.number_buttons[2].invoke()
    test_app.operation_buttons[4].invoke()
    assert test_app.display.get() == "2.00"

    # test zero division
    test_app.button_clear.invoke()
    test_app.number_buttons[4].invoke()
    test_app.operation_buttons[3].invoke()
    test_app.number_buttons[0].invoke()
    test_app.operation_buttons[4].invoke()
    assert test_app.display.get() == "UNDEFINED"
