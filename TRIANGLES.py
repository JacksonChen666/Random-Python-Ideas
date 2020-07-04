import random
import turtle

t = turtle.Pen()
t.speed(0)
t.pencolor("white")
turtle.bgcolor("black")

a = 820


def main():
    global a
    t.hideturtle()
    t.penup()
    t.goto(-416, -378)
    t.pendown()
    while True:
        # t.begin_fill()
        a = random.uniform(0, 820)
        # a = a - 1
        # if a <= 0:
        #     a = 825
        for i in range(3):
            t.forward(a)
            t.left(360 / 3)
        # t.end_fill()


main()
turtle.done()
