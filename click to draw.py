import turtle

t = turtle.Pen()
turtle.onscreenclick(t.setpos)

while True:
    for i in range(1000):
        t.forward(0)
    t.clear()
