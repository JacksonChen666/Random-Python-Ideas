import turtle, random

t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
t.pensize("3")

c = 0
d = 0
e = 0
f = 0


def main():
    global c, d, e, f
    a = random.randint(5, 200)
    b = random.randint(2, 10)
    # c = turtle.window_width() - 500
    # d = turtle.window_height() - 500
    # e = turtle.window_width() * -1 + 500
    # f = turtle.window_height() * -1 + 500
    t.pencolor(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
    t.penup()
    # t.goto(random.randint(c, 0), random.randint(d, 0))
    t.setheading(random.randint(0, 360))
    t.pendown()
    t.begin_fill()
    for i in range(b):
        t.forward(a)
        t.right(360 / b)
    t.end_fill()


while True:
    main()
    # print(c, d, e, f)
