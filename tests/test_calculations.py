from app.calculations import add,subtract,multiply,divide


def test_add():
    print("testing weird data")
    assert add(5,3)==8

def test_sub():
    print("=>testing sub method")
    assert subtract(8,5)==3

def test_mul():
    print("=>testing multiply method")
    assert multiply(8,5)==40

def test_divide():
    print("=>testing divide method")
    assert divide(4,2)==2