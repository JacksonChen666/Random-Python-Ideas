import random
import string
import turtle


def __init__():
    global t, q, a, s, d, f
    t = turtle.Pen()
    s = turtle.Screen()
    s.tracer(10)
    t.up()
    t.speed(0)
    q = 300
    w = 250
    # Main way
    a = turtle.window_height() - q
    s = turtle.window_height() * -1 + q
    d = turtle.window_width() - w
    f = turtle.window_width() * -1 + w
    # Using the division is the alt solution. The numbers are not perfect
    z = turtle.window_height() / 1.6142
    x = turtle.window_height() / 1.6142
    c = turtle.window_width() / 1.4237288134
    v = turtle.window_width() / 1.4237288134
    t.ht()
    print(a, s, d, f, z, x, c, v)


def main():
    # noinspection PyGlobalUndefined
    global q, a, s, d, f
    # t.goto(a, d)
    # t.dot(10)
    # t.goto(s, f)
    # t.dot(10)
    # t.goto(d, a)
    # t.dot(10)
    # t.goto(f, s)
    # t.dot(10)
    # turtle.done()
    while True:
        for i in range(2500):
            q = random.choice(string.printable)
            t.goto(random.randint(s, a), random.randint(f, d))
            t.write("{}".format(q),
                    align="center", font=("Arial", random.randint(10, 100), "normal"))
        t.clear()


# Idea: turtle writes random text in random size and color

if __name__ == '__main__':
    __init__()
    main()
