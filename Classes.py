# ! /usr/bin/env python3


class Money:

    # __init__ is the name of  the constructor
    #  (self,anAmount, aCurrency) are the arguments pass to the constructor
    # self refers to an object under construction
    def __init__(self, anAmount, aCurrency):
        self.amount = anAmount
        self.currency = aCurrency

    def __str__(self):
        return str(self.amount) + ' ' + self.currency

    def __add__(self, otherMoney):
        if self.currency == otherMoney.currency:
            return Money((self.amount + otherMoney.amount), self.currency)

    def convert(self, rate, newCurrency):
        newAmount = self.amount*rate
        self.amount = round(newAmount, 2)
        self.currency = newCurrency
        return self

    def times(self, factor):
        return Money((self.amount * factor), self.currency)


money1 = Money(100, 'GBP')
print(money1.amount, money1.currency)

money2 = Money(50, 'EUR')
money3 = money2.convert(3, 'RUB')
print(money3)

money4 = Money(11, 'EUR')
money5 = Money(40, 'EUR')
print(money4 + money5)

money6 = Money(100, 'CNY')
print(money6.times(4))
