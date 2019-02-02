import locale

class Account:

    NATURAL_PERSON = "F"
    LEGAL_PERSON = "J"

    def __init__(self, number, holder, balance, type=NATURAL_PERSON, limit=1000.0):
        locale.setlocale(locale.LC_MONETARY, "")
        self.__number = number
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit
        self.__type = type

    @property
    def number(self):
        return self.__number

    @property
    def holder(self):
        return self.__holder

    @property
    def balance(self):
        return self.__balance

    @property
    def limit(self):
        return self.__limit

    @property
    def type(self):
        return self.__type;

    @type.setter
    def type(self, type):
        self.__type = type

    @limit.setter
    def limit(self, limit):
        self.__limit = limit

    def deposit(self, value):
        self.__balance += value

    def cash_out(self, value):
        if (value <= self.__available_value()):
            self.__balance -= value
        else:
            print("The value {0} exceeds the limit".format(self.__currency_value(value)))

    def __available_value(self):
        return self.__limit + self.__balance

    def __currency_value(self,value):
        return locale.currency(value, grouping=True)

    def print_statement(self):
        print("{0} has {1} in the account.".format(self.__holder, self.__currency_value(self.__balance)))

    def transfer_to(self, account, value):
        self.cash_out(value)
        account.deposit(value)

    @staticmethod
    def bank_prefix():
        return "341"