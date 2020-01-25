"""
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>
"""
import time
import turtle


def tExit():
    turtle.title("Goodbye")
    t.clear()
    t.write("Goodbye!", font=("Arial", 50, "normal"), align="center")
    turtle.bye()


def clear():
    t.clear()


def forward():
    t.forward(10)


def backward():
    t.backward(10)


def left():
    t.left(10)


def right():
    t.right(10)


def reset():
    t.reset()
    t.speed(0)
    turtle.listen()
    turtle.mainloop()


def exits():
    turtle.bye()


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
    t.up()
    t.home()
    t.down()


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


def pos():
    t.write(turtle.pos(), align="center", font=("Arial", 50, "normal"))
    time.sleep(1)
    undo()
    turtle.listen()
    turtle.mainloop()


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
    ts.onkey(exits, "e")
    ts.onkey(fill, "f")
    ts.onkey(home, "h")
    ts.onkey(undo, "u")
    ts.onkey(screensize, "g")
    ts.onkey(pen, "p")
    ts.onkey(writeinputtext, "t")
    ts.onkey(pos, "o")
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

Keys binded:
O as position (on-screen, temp)
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

# Stuff with pen: goto, setpos, exitonclick
