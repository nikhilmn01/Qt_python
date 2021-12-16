import pytest


@pytest.fixture(scope="class")
def config():
    print("this is configuration file")
    yield
    print("I am executed last")
