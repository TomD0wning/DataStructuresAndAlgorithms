from turtle import *

t = Turtle()
window = t.getscreen()

def draw(t,lineLength):
    if lineLength > 0:
        t.forward(lineLength)
        t.right(90)
        draw(t,lineLength -5)

draw(t,200)
window.exitonclick()