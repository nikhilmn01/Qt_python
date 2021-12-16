import pytest


# from pyTest.conftest import config


@pytest.mark.usefixtures("config")
class TestExample:
    def test_first_program(self):
        print("hello ")

    def test_secondProgram(self):
        print("second program")

    def test_secondProgram2(self):
        print("second program pro")
        msg = "hello"
        assert not msg == "hi", "test Failed"


