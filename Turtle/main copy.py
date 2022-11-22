import turtle as t
from random import randint

t.pensize(5)
WIDTH, HEIGHT = 1920, 1800
screen = t.Screen()
screen.setup(WIDTH, HEIGHT)
screen.screensize(WIDTH*3, HEIGHT*3)
screen.bgpic()


t.Screen().exitonclick()
