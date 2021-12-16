import pytest


@pytest.mark.smoke
@pytest.mark.skip
# @pytest.mark.xfail
def test_secondProgram2():
    print("second program pro")
    msg= "hello"
    assert msg == "hi" , "test Failed"