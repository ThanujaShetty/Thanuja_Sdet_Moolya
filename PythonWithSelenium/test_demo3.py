import pytest

@pytest.mark.usefixtures("setup")
class Test_demo:

    def test_mytestFunch(self):
        print("hello Thanu")

    def test_mytestFunch8(self):
        print("hai")


@pytest.mark.usefixtures("data")
class Test_demo1:
    def test_mymethod(self,data):
        print("data is",data)

@pytest.mark.usefixtures("name")
class Test_demo1:
    def test_mymethod(self,data):
        print("data is",data)
