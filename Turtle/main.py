import turtle as t
from art import *  # funny module xD

t.pensize(5)
t.speed(2000)

art_2 = art("woman", number=2)
print(art_2)

for i in range(0, 400, 20):
    t.forward(i)
    t.right(90)

t.Screen().exitonclick()
