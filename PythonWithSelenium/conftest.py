import pytest



@pytest.fixture(scope="class")
def setup():
    print("Before driver. execute before each test")
    yield
    print("After execute after each test ")

@pytest.fixture(scope='class')
def name():
    return ["thanu","abhi"]
@pytest.fixture(params=["thanu","hai"])
def data(request):
    return request.param

