import random
import turtle

t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
t.pensize("3")


def main():
    a = random.randint(5, 200)
    b = random.randint(3, 10)
    # c = turtle.window_width() - 500
    # d = turtle.window_height() - 500
    # e = turtle.window_width() * -1 + 500
    # f = turtle.window_height() * -1 + 500
    t.pencolor(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
    t.up()
    t.setpos(random.randint(-500, 500), random.randint(-500, 500))
    t.setheading(random.randint(0, 360))
    t.down()
    t.begin_fill()
    for i in range(b):
        t.forward(a)
        t.right(360 / b)
    t.end_fill()


ts = turtle.Screen()
ts.setup(width=1.0, height=1.0)

try:
    while True:
        main()
except turtle.Terminator:
    print("Error: User closed turtle window")
