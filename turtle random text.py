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
import string
import turtle


def __init__():
    global t, q, a, s, d, f
    t = turtle.Pen()
    q = random.choice(string.printable)
    t.up()
    t.speed(5)
    q = 300
    w = 250
    # Main way
    a = turtle.window_height() - q
    s = turtle.window_height() * -1 + q
    d = turtle.window_width() - w
    f = turtle.window_width() * -1 + w
    # Using the division is the alt solution. The numbers are not perfect
    z = turtle.window_height() / 1.6142
    x = turtle.window_height() / 1.6142
    c = turtle.window_width() / 1.4237288134
    v = turtle.window_width() / 1.4237288134
    # t.ht()
    print(a, s, d, f, z, x, c, v)
    # ts = turtle.Screen()
    # ts.setup(width=0.0, height=0.0)


def main():
    global q, a, s, d, f
    turtle.bye()
    t.goto(a, d)
    t.dot(10)
    t.goto(s, f)
    t.dot(10)
    t.goto(d, a)
    t.dot(10)
    t.goto(f, s)
    t.dot(10)


# while True:
#     t.goto(random.randint(s, a), random.randint(f, d))


# Idea: turtle writes random text in random size and color

if __name__ == '__main__':
    __init__()
    main()
