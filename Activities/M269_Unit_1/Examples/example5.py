#!/usr/bin/env python3

class Money: 
    def __init__(self, anAmount, aCurrency):
        self.amount = anAmount
        self.currency = aCurrency
    
    def __str__(self):
        return str(self.amount) + ' ' + self.currency
     
    def convert(self, rateFromTo, newCurrency):
        newAmount = self.amount*rateFromTo
        self.amount = round(newAmount)
        self.currency = newCurrency
        return self
    
    #The __add__ method should go here
    
    #Your times method should go here   
    
# End of class definition: make sure all methods are
# above here and are indented.
        
money1 = Money(10, 'GBP')

print(money1.amount)
print(money1.currency)

money1.amount = 42
print(money1.amount)

money2 = Money(100, 'EUR')
print(money2)

money3 = money2.convert(39.91, 'RUB')
print(money3)
