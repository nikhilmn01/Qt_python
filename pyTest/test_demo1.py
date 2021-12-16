import pytest


@pytest.mark.smoke1
@pytest.mark.skip
def test_first_program(config):
    print("hello ")

@pytest.mark.skip
def test_secondProgram(config):
    print("second program")
