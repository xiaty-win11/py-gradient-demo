from turtle import Turtle
import turtle
t = Turtle()
t.speed(0)
turtle.colormode(255)
a, b, c = 255, 255, 255
t.pensize(5)
t.hideturtle()
turtle.bgcolor('black')
for i in range(180):
    if a > 0: a -= 5
    if b > 1: b -= 2
    t.color(a, b, c)
    t.forward(201)
    t.back(200)
    t.right(1)
for i in range(180):
    if a < 255: a += 5
    if b < 254: b += 2
    t.color(a, b, c)
    t.forward(201)
    t.back(200)
    t.right(1)
turtle.done()
