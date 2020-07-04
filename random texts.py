import turtle

z = turtle.window_width() - 410  # Window sizes, may not be accurate
x = turtle.window_width() * -1 + 410  # Window sizes, may not be accurate
c = turtle.window_height() - 405  # Window sizes, may not be accurate
v = turtle.window_height() * -1 + 405  # Window sizes, may not be accurate

print(z, x, c, v)


def main():
    t = turtle.Pen()
    t.up()
    while True:
        t.goto()


main()
