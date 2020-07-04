import random
import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.setup(500, 500)
s.tracer(0)
a = 2
t.ht()
t.up()
t.goto(-500, 0)
t.down()


def draw():
    global a
    for i in range(a):
        t.forward(100 / a)
        t.left(360 / a)


while True:
    t.clear()
    if t.xcor() > 500:
        t.up()
        t.goto(-500, 0)
        t.down()
        a += 1
    draw()
    s.update()
    t.pencolor(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
    t.forward(5)
