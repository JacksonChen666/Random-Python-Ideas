import random
import turtle

t = turtle.Pen()

t.speed(0)
turtle.bgcolor("black")
t.pencolor("white")

a = 0

while True:
    t.goto(random.randint(-300, 300), random.randint(-300, 300))
    a += 1
    if a >= 500:
        t.clear()
        a = 0
