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

# h

t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
t.pensize("3")

c = 0
d = 0
e = 0
f = 0


def main():
    global c, d, e, f
    a = random.randint(5, 200)
    b = random.randint(2, 10)
    # c = turtle.window_width() - 500
    # d = turtle.window_height() - 500
    # e = turtle.window_width() * -1 + 500
    # f = turtle.window_height() * -1 + 500
    t.pencolor(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
    t.penup()
    # t.goto(random.randint(c, 0), random.randint(d, 0))
    t.setheading(random.randint(0, 360))
    t.pendown()
    t.begin_fill()
    for i in range(b):
        t.forward(a)
        t.right(360 / b)
    t.end_fill()


while True:
    main()
    # print(c, d, e, f)
