from app.calculations import add, subtract, multiply, divide, BankAccount, InsufficientFundsException
import pytest

@pytest.fixture
def zero_bank_account():
    return BankAccount()
@pytest.fixture
def bank_account():
    return BankAccount(50)

@pytest.mark.parametrize("num1,num2,expected",[(3,2,5),(7,1,8),(12,4,16)])
def test_add(num1,num2,expected):
    print("testing weird data")
    assert add(num1,num2)==expected

def test_sub():
    print("=>testing sub method")
    assert subtract(8,5)==3

def test_mul():
    print("=>testing multiply method")
    assert multiply(8,5)==40

def test_divide():
    print("=>testing divide method")
    assert divide(4,2)==2

def test_bank_set_initial_amount():
    bank_account = BankAccount(50)
    assert bank_account.balance == 50

def test_bank_default_amount(zero_bank_account):
    # bank_account = BankAccount()
    assert zero_bank_account.balance == 0

def test_withdraw():
    bank_account = BankAccount(50)
    bank_account.withdraw(20)
    assert bank_account.balance == 30

def test_deposit():
    bank_account=BankAccount(50)
    bank_account.deposit(30)
    assert bank_account.balance == 80
    assert round(bank_account.balance,6)==80

def test_bank_transaction(zero_bank_account):
    zero_bank_account.deposit(215)
    zero_bank_account.withdraw(214)
    assert zero_bank_account.balance==1

def test_insufficient_funds(bank_account):
    with pytest.raises(InsufficientFundsException):
        bank_account.withdraw(200)