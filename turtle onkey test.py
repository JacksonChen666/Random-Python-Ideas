import turtle

t = turtle.Pen()


def test():
    t.write("Test")


turtle.onscreenclick(test)

turtle.listen()
turtle.mainloop()
