from app import soma

def test_1():
    assert soma(1,1) == 2

def test_2():
    assert soma(2,2) == 4

def test_3():
    assert soma(3,3) == 6

def test_4():
    assert soma(5,5) == 10

def test_5():
    assert soma(10,5) == 15
