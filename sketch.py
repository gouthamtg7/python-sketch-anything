import turtle as t
from turtle import Turtle, Screen
timmy = Turtle()
screen = Screen()
def forwards():
    timmy.forward(10)
def backwards():
    timmy.forward(-10)
def left():
    timmy.left(5)
    timmy.forward(10)
def right():
    timmy.right(5)
    timmy.forward(10)
def clear():
    timmy.clear()
    timmy.reset()
screen.listen()
screen.onkeypress(fun=forwards,key="w"or"W")
screen.onkeypress(fun=backwards,key="s"or"S")
screen.onkeypress(fun=left,key="a"or"A")
screen.onkeypress(fun=right,key="d"or"D")
screen.onkey(fun=clear,key="c"or"C")
screen.onscreenclick(fun=screen.exitonclick(),btn=3)
