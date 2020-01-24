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
import turtle

t = turtle.Pen()


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
    t.home()


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


a = 0
b = 0
c = 1


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
    ts.listen()
    ts.mainloop()


if __name__ == '__main__':
    ts = turtle.Screen()
    ts.setup(width=1.0, height=1.0)
    turtle.title("Custom turtle drawer Intro: bit.ly/CustomTurtleIntro")
    t.write("Know how to use this program at bit.ly/CustomTurtleIntro\nUse WASD to control, best with arrow keys\nR "
            "to "
            "reset\nC to clear\nE to exit",
            font=("Arial", 50, "normal"), align="center")
    __init__()

"""
Keys to bind:


Keys binded:
G as full screen and normal
T as to write text (user input)
U to undo
P as pen up and down
H as home
WASD and arrow keys
R as Reset
C as clear
E as exit
F as fillings
H as home
"""

# Stuff with pen: onclick, ondrag, onrelease, reset, setangle, write, back, goto, home, pos, setpos, clear, done,
# exitonclick, ondrag, onscreenclick, textinput
