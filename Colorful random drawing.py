import random
import turtle

t = turtle.Pen()

turtle.bgcolor("black")


# Make turtle go to random positions near the turtle
# noinspection PyMissingOrEmptyDocstring
def main():
    while True:
        t.ht()
        a = random.randint(1, 4)
        b = random.uniform(0, 1)
        c = random.uniform(0, 1)
        d = random.uniform(0, 1)
        t.pencolor(b, c, d)
        if a == 1:
            t.goto(t.xcor() + 1, t.ycor())
        elif a == 2:
            t.goto(t.xcor(), t.ycor() + 1)
        elif a == 3:
            t.goto(t.xcor(), t.ycor() - 1)
        elif a == 4:
            t.goto(t.xcor() - 1, t.ycor())


main()
