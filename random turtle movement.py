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
import random
import turtle

t = turtle.Pen()
t.speed(0)
t.ht()
t.up()
s = turtle.Screen()
s.tracer(0)
s.setup(width=1.0, height=1.0)


def edgeCheck():
    if t.xcor() > turtle.window_width():
        t.goto(turtle.window_width() - 500, t.ycor())
    if t.ycor() > turtle.window_height():
        t.goto(t.xcor(), turtle.window_height() - 500)
    if t.xcor() < turtle.window_width() * -1:
        t.goto(turtle.window_width() * -1 + 500, t.ycor())
    if t.ycor() < turtle.window_height() * -1:
        t.goto(t.xcor(), turtle.window_height() * -1 + 500)


def main():
    turtle.title("Shakey")
    t.clear()
    t.goto(0, 0)
    turtle.onscreenclick(t.goto)
    a = turtle.textinput("Text", "What text on the screen do you want?")
    b = turtle.textinput("Shakeyness", "How many pixels for shakyness? (recommended: 25)")
    turtle.title("Shakey {}".format(a))
    try:
        while True:
            # print(t.xcor(),t.ycor())
            t.forward(random.uniform(0, int(b)))
            t.right(random.uniform(0, 360))
            t.write(a, font=("Arial", 100, "normal"))
            edgeCheck()
            s.update()
            t.clear()
    except turtle.Terminator as err:
        print("User closed turtle window, aborting")
        exit()
    except TypeError as err:
        print(err)
        t.goto(-600, 0)
        t.write("Error: {}\nClick to exit".format(err), font=("arial", 25, "normal"))
        s.update()
        turtle.exitonclick()
    except ValueError as err:
        print(err)
        t.goto(-600, 0)
        t.write("Error: {}\nClick to exit".format(err), font=("arial", 25, "normal"))
        s.update()
        turtle.exitonclick()


main()
