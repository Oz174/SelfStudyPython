
# python -m pytest '.\22- pytest.py' 


def add(x, y):
    return x + y


def test_add():
    assert add(3, 4) == 7
    assert add(-2, -3) == -5