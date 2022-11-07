import pytest

class BankAccount:
    def __init__(self, name, age):
        self.balance = 0
        self.min_balance = 0
        self.name = name
        self.age = age
        self.movements = []

    def deposit(self, amount):
        if not isinstance(amount, int):
            raise ValueError('Only numbers are allowed')
        if amount < 0:
            raise ValueError('Only positive values are allowed')

        new_movement = f"deposit {amount} from {self.name}"
        self.movements.append(new_movement)
        print(new_movement)

        self.balance += amount
        print(self)

    def withdraw(self, amount):
        if not isinstance(amount, int):
            raise ValueError('Only numbers are allowed')
        if amount < 0:
            raise ValueError('Only positive values are allowed')
        if amount > self.balance:
            raise ValueError('Deposit some money please')

        new_movement = f"withdraw {amount} from {self.name}"
        self.movements.append(new_movement)
        print(new_movement)

        self.balance -= amount
        print(self)
        self.display_warning()

    def __str__(self):
       return f"{self.name} owns {self.balance}, "

    def print_movements(self):
        for i in self.movements:
            print(i)

    def display_warning(self):
        if self.balance < self.min_balance:
            print(f"hey {self.name}, you balance is lower than the allowed balance. Be carefully")

    def set_min_balance(self, min_balance):
        self.min_balance = min_balance

    def grant_loan(self, loan, days):
        self.max_loan = 1000000
        min_days = 30
        self._days = days
        try:
            loan > self.max_loan
        except ValueError:
            print(f"it is too much, max loan is {self.max_loan}")
        try:
            days < min_days
        except AttributeError:
            print(f"it is too quick, min 30 days are allowed")
            self.balance += loan



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


