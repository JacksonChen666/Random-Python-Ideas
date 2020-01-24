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


a = 0


def __init__():
    ts = turtle.Screen()
    ts.setup(width=1.0, height=1.0)
    turtle.title("Custom turtle drawer Intro: bit.ly/CustomTurtleIntro")
    t.write("Know how to use this program at bit.ly/CustomTurtleIntro\nR to reset\nC to clear\nE to exit",
            font=("Arial", 50, "normal"), align="center")
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
    ts.listen()
    ts.mainloop()


if __name__ == '__main__':
    __init__()

"""
Keys to bind:
F as of filling
U to undo
Q as 
H as home
"""

# Stuff with pen: onclick, ondrag, onrelease, reset, setangle, write, back, goto, home, pos, setpos, clear, done,
# exitonclick, ondrag, onkey, onkeypress, onkeyrelease, onscreenclick, textinput, title
