import pytest

@pytest.mark.smoke
@pytest.mark.skip
def test_myfunc2smoke():
    #with using marker
    # cmd to run pytest -m smoke
    name = "Thanuja"
    assert name == "Thanuja"

def test_myfunc3regression():
    #another way of grouping test case
    #def test_myfunc3Regression or test_myfunc3moke
    #cmd to run pytest -k regression -vs
    print("Hello welcome to python programming")