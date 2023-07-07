import pytest
from pytestqt.qtbot import QtBot
from calculator import app
from PyQt5.QtCore import Qt


@pytest.fixture
def gui(qtbot):
    gui = app()
    qtbot.addWidget(gui)
    return gui
def test_display(qtbot):
    calculator_widget = app()
    qtbot.addWidget(calculator_widget)
    display_widget = calculator_widget.display
    assert display_widget.get() == ""


def test_buttons(gui, qtbot):
    # Test number buttons
    for num in range(10):
        qtbot.mouseClick(gui.number_buttons[num], Qt.LeftButton)
    assert gui.display.text() == '1234567890'

    # Test addition button
    qtbot.mouseClick(gui.add_button, Qt.LeftButton)
    assert gui.operation == '+'

    # Test subtraction button
    qtbot.mouseClick(gui.subtract_button, Qt.LeftButton)
    assert gui.operation == '-'

    # Test multiplication button
    qtbot.mouseClick(gui.multiply_button, Qt.LeftButton)
    assert gui.operation == '*'

    # Test division button
    qtbot.mouseClick(gui.divide_button, Qt.LeftButton)
    assert gui.operation == '/'

    # Test clear button
    qtbot.mouseClick(gui.clear_button, Qt.LeftButton)
    assert gui.display.text() == '0'
    assert gui.operation == ''
    assert gui.first_operand == ''

    # Test calculation with integers
    qtbot.mouseClick(gui.number_buttons[2], Qt.LeftButton)
    qtbot.mouseClick(gui.number_buttons[5], Qt.LeftButton)
    qtbot.mouseClick(gui.add_button, Qt.LeftButton)
    qtbot.mouseClick(gui.number_buttons[3], Qt.LeftButton)
    qtbot.mouseClick(gui.number_buttons[5], Qt.LeftButton)
    qtbot.mouseClick(gui.equal_button, Qt.LeftButton)
    assert gui.display.text() == '60'

    # Test calculation with floats
    qtbot.mouseClick(gui.clear_button, Qt.LeftButton)
    qtbot.mouseClick(gui.number_buttons[2], Qt.LeftButton)
    qtbot.mouseClick(gui.decimal_button, Qt.LeftButton)
    qtbot.mouseClick(gui.number_buttons[5], Qt.LeftButton)
    qtbot.mouseClick(gui.add_button, Qt.LeftButton)
    qtbot.mouseClick(gui.number_buttons[1], Qt.LeftButton)
    qtbot.mouseClick(gui.decimal_button, Qt.LeftButton)
    qtbot.mouseClick(gui.number_buttons[5], Qt.LeftButton)
    qtbot.mouseClick(gui.equal_button, Qt.LeftButton)
    assert gui.display.text() == '4.0'
