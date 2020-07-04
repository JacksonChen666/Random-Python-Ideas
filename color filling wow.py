import random
import turtle

t = turtle.Pen()

# turtle.bgcolor("black")
t.speed(0)

a = turtle.window_width() - 410  # Window sizes, may not be accurate
b = turtle.window_width() * -1 + 410  # Window sizes, may not be accurate
c = turtle.window_height() - 405  # Window sizes, may not be accurate
d = turtle.window_height() * -1 + 405  # Window sizes, may not be accurate

q = turtle.window_width() - 410  # Window sizes, may not be accurate
w = turtle.window_width() * -1 + 410  # Window sizes, may not be accurate
e = turtle.window_height() - 405  # Window sizes, may not be accurate
r = turtle.window_height() * -1 + 405  # Window sizes, may not be accurate
print(a, b, c, d)


def main():
    global a, b, c, d, q, w, e, r
    t.up()
    t.setpos(b, d)
    t.down()
    while True:
        # print(t.xcor(),t.ycor()) # Position debugging
        # t.up()
        # l = random.uniform(0,1)
        # k = random.uniform(0,1)
        # j = random.uniform(0,1)
        t.pencolor(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
        # t.fillcolor(l,k,j)
        # t.down()
        t.goto(b, d)
        b += 1
        if t.xcor() >= a:
            d += 1
            b = w
            break
            # print(a,b,c,d) # Debugging


while True:
    main()
    if t.ycor() >= c:
        turtle.done()
