import turtle


def tExit():
    turtle.bye()


def clear():
    t.clear()


def forward():
    t.forward(q)


def backward():
    t.backward(q)


def left():
    t.left(q)


def right():
    t.right(q)


def reset():
    t.reset()
    t.speed(0)
    turtle.listen()
    turtle.mainloop()


def fill():
    global a
    if a == 0:
        a = 1
        t.begin_fill()
    elif a == 1:
        a = 0
        t.end_fill()


def pen():
    global b
    if b == 0:
        b = 1
        t.up()
    elif b == 1:
        b = 0
        t.down()


def home():
    t.speed(2)
    t.up()
    t.home()
    t.down()
    t.speed(0)


def screensize():
    global c
    if c == 0:
        ts.setup(width=1.0, height=1.0)
        c = 1
    elif c == 1:
        ts.setup(width=0.5, height=0.75)
        c = 0


def undo():
    t.undo()


def writeinputtext():
    d = turtle.textinput("Text", "What text do you want to write?")
    t.write(d, align="center", font=("Arial", 50, "normal"))
    turtle.listen()
    turtle.mainloop()


# def pos():
#     t.write(turtle.pos(), align="center", font=("Arial", 50, "normal"))
#     times.sleep(1)
#     undo()
#     turtle.listen()
#     turtle.mainloop()


def speed():
    q = turtle.textinput("Speed",
                         "How many pixels do you want to move with 1 click? Applies to all movement Default=10")
    turtle.listen()
    turtle.mainloop()


def sides():
    pass

# def setangle():
#     h = turtle.textinput("Set angle", "What angle to you want to set to? 0-360")
#     turtle.setpos(h)
#     turtle.listen()
#     turtle.mainloop()


# def pencolor():
#     d = turtle.textinput("Red Pen Color", "How much red do you want? 0-1")
#     e = turtle.textinput("Green Pen Color", "How much green do you want? 0-1")
#     f = turtle.textinput("Blue Pen Color", "How much blue do you want? 0-1")
#     t.pencolor(d, e, f)
#     turtle.listen()
# turtle.mainloop()
#
#
# def fillcolor():
#     d = turtle.textinput("Red Fill Color", "How much red do you want? 0-1")
#     e = turtle.textinput("Green Fill Color", "How much green do you want? 0-1")
#     f = turtle.textinput("Blue Fill Color", "How much blue do you want? 0-1")
#     t.fillcolor(d, e, f)
#     turtle.listen()
#     turtle.mainloop()


a = 0
b = 0
c = 1
h = 0
q = 10
u = 0


def __init__():
    ts.onkeypress(forward, "w")
    ts.onkeypress(forward, "Up")
    ts.onkeypress(backward, "s")
    ts.onkeypress(backward, "Down")
    ts.onkeypress(left, "a")
    ts.onkeypress(left, "Left")
    ts.onkeypress(right, "d")
    ts.onkeypress(right, "Right")
    ts.onkey(reset, "r")
    ts.onkey(clear, "c")
    ts.onkey(tExit, "e")
    ts.onkey(fill, "f")
    ts.onkey(home, "h")
    ts.onkey(undo, "u")
    ts.onkey(screensize, "g")
    ts.onkey(pen, "p")
    ts.onkey(writeinputtext, "t")
    # ts.onkey(pos, "o")
    # ts.onkey(setangle, "j")
    # ts.onkey(pencolor, "x")
    # ts.onkey(fillcolor, "z")
    turtle.listen()
    turtle.mainloop()


if __name__ == '__main__':
    t = turtle.Pen()
    t.speed(0)
    ts = turtle.Screen()
    ts.setup(width=1.0, height=1.0)
    turtle.title("Custom turtle drawer Intro: bit.ly/CustomTurtleIntro")
    t.write("Know how to use this program at bit.ly/CustomTurtleIntro\nUse WASD to control, best with arrow keys\nR "
            "to reset\nC to clear\nE to exit", font=("Arial", 50, "normal"), align="center")
    turtle.onscreenclick(t.goto)
    __init__()
    turtle.listen()
    turtle.mainloop()

"""
Keys to bind:
X as pen color (broken)
Z as pen filling color (broken)
J as set angle (broken)
O as position (on-screen, temp, broken)
I as speed (broken)

Keys binded:
G as full screen and normal
T as to write text (user input)
U to undo
P as pen up and down
H as home
WASD and arrow keys for movement
R as Reset
C as clear
E as exit
F as fillings
"""
