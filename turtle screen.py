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

t = turtle.Turtle()
s = turtle.Screen()
s.setup(500, 500)
s.tracer(0)
a = 2
t.ht()
t.up()
t.goto(-500, 0)
t.down()


def draw():
    global a
    for i in range(a):
        t.forward(100 / a)
        t.left(360 / a)


while True:
    t.clear()
    if t.xcor() > 500:
        t.up()
        t.goto(-500, 0)
        t.down()
        a += 1
    draw()
    s.update()
    t.pencolor(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
    t.forward(1)
