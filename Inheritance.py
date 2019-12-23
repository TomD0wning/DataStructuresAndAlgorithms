#! /usr/bin/env python3

# An example of inheritance, using logic gates

class LogicGate:

    def __init__(self,n):
        self.label =n
        self.output = None
    
    def getLabel(self):
        return self.label
    
    def getOutput(self):
        self.output = self.performGateLogic()
        print(self.output)
        return self.output

class BinaryGate(LogicGate):
    
    def __init__(self,n):
        super().__init__(n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.PinA == None:
            return int(input("Enter a Pin A input for gate " + \
            self.getLabel() + "-->"))
        else:
            return self.PinA.getFrom().getOutput()
    
    def getPinB(self):
        return int(input("Enter a Pin B input for gate " + \
        self.getLabel() + "-->"))

    def setNextPin(self,source):
        if self.pinA == None:
            self.PinA = source
        else:
            if self.pinB == None:
                self.PinB = source
            else:
                raise RuntimeError("NO EMPTY PINS")
    
class UnaryGate(LogicGate):

    def __init__(self,n):
        super().__init__(n)

        self.pin = None

    def getPin(self):
        return int(input("Enter a Pin input for gate " + \
        self.getLabel() + "-->"))

    def setNextPin(self,source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError("NO EMPT PINS")

class AndGate(BinaryGate):
    
    def __init__ (self,n):
        super().__init__(n)


    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    
    def __init__ (self,n):
        super().__init__(n)


    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a==1 or b==1:
            return 1
        else:
            return 0

class NotGate(UnaryGate):
    
    def __init__(self,n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPin()
        if a == 1:
            return 0
        else:
            return 1

class Connector:
    def __init__(self,fGate, tGate):
        self.fromGate = fGate
        self.toGate = tGate

        tGate.setNextPin(self)
    
    def getFrom(self):
        return self.fromGate
    
    def getTo(self):
        return self.toGate


#Testing of the logic gate inheritance

g1 = AndGate("G1")
g2 = AndGate("G2")
g3 = OrGate("G3")
g4 = NotGate("G4")
c1 = Connector(g1,g3)
c2 = Connector(g2,g3)
c3 = Connector(g3,g4)

g4.getOutput()


