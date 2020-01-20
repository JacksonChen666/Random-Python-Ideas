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
        t.pencolor(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
        # t.down()
        t.goto(b, d)
        b = b + 1
        if t.xcor() >= a:
            d = d + 1
            b = w
            break
            # print(a,b,c,d) # Debugging


while True:
    main()
    if t.ycor() >= c:
        turtle.done()
