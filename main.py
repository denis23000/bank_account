# Write a BankAccount class that works like specified:
#
# Steps:
#
# 1.Store the current value of the BankAccount in an attribute named balance that should start with 0.
# (Hint: implement __init__() function)
#
# 2.Now create some instances of BankAccount and check whether they are instances of the said classes or not
# (Hint: use isinstance() for this)
#
# 3.Add a deposit method that receives a value and adds it to balance and prints balance
#
# 4.Add a withdraw method that receives a value and subtracts it from balance and prints balance
import pytest

class BankAccount:
    def __init__(self, name, age):
        self.balance = 0
        self.name = name
        self.age = age

    def deposit(self, amount):
        if not isinstance(amount, int):
            raise ValueError('Only numbers are allowed')
        if amount < 0:
            raise ValueError('Only positive values are allowed')

        self.balance += amount
        print(self)

    def withdraw(self, amount):
        if not isinstance(amount, int):
            raise ValueError('Only numbers are allowed')
        if amount < 0:
            raise ValueError('Only positive values are allowed')
        if amount > self.balance:
            raise ValueError('Deposit some money please')
        self.balance -= amount
        print(self)

    def __str__(self):
       return f"{self.name} owns {self.balance}, "



oriyomi_account = BankAccount('oriyomi', 27)
oriyomi_account.deposit(3000)

mark_account = BankAccount(age=25, name='mark')
mark_account.deposit(5000)
mark_account.withdraw(4000)
oliver = BankAccount(age=45, name='oliver')
oliver.deposit(1000)

# print(oriyomi_account)
# print(mark_account)

isinstance(oriyomi_account, BankAccount)
if isinstance(oriyomi_account, BankAccount):
    print('yes, it is a bank account')
else:
    print('it is not a bank account')


def test_only_positive_amount():

    account = BankAccount(name='oliver', age=47)

    with pytest.raises(ValueError):
        account.deposit(-100)
    with pytest.raises(ValueError):
        account.withdraw(-100)


def test_no_strings_allowed():

    account = BankAccount(name='oliver', age=47)

    with pytest.raises(ValueError):
        account.deposit('mark')
    with pytest.raises(ValueError):
        account.withdraw('mark')

def test_no_negavtive_balance_allowed():

    account = BankAccount(name='oliver', age=47)
    account.deposit(1000)

    with pytest.raises(ValueError):
        account.withdraw(2000)
    with pytest.raises(ValueError):
        account.withdraw('mark')
