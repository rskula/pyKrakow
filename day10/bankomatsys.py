class ATM(object):
    def login(self):
        pass

    def balance(self):
        pass

    def withdraw(self):
        pass


class Card(object):
    def __init__(self, c_cardNumber, c_pin):
        self.number = c_cardNumber
        self.pin = c_pin


class Account(object):
    def __init__(self, c_accNumber, c_balance=0):
        self.number = c_accNumber
        self.balance = c_balance


class Bank(object):
    def __init__(self, c_accounts):
        self.accounts = c_accounts


def main():
    bank = Bank({1: Account("12 1234 5678 0000 0000 0000 0000 1234 5678", 1234),
                 2: Account("12 1234 5678 0000 0000 0000 0000 1234 5679", 234),
                 3: Account("12 1234 5678 0000 0000 0000 0000 1234 5670")})
    for account in bank.accounts:
        print("{}: {}".format(bank.accounts[account].number, bank.accounts[account].balance))


if __name__ == '__main__':
    main()
