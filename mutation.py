import pytest

def test_mutations():
    test_command = "pytest testare_functionala.py"
    mutation_command = f"mutagen run --target calculator.py --paths . --coverage --unit-test-command '{test_command}'"
    result = pytest.main(["--capture=no", "-c", "pytest_mutagen.ini", mutation_command])
    assert result == pytest.ExitCode.OK, "Mutation tests failed"
