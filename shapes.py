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
s = turtle.Screen()
a = 2
t.speed(5)
\
while True:
    t.write(a, font=("Arial", 50, "normal"), align="center")
    if a >= 11:
        t.speed(0)
        s.tracer(5)
    if a > 49 < 98:
        s.tracer(10)
    if a > 99 < 498:
        s.tracer(100)
    if a > 499 < 1000:
        s.tracer(500)
    if a > 1001:
        t.clear()
        t.write("The limit of sides has reached\nPlease click to exit", font=("Arial", 20, "normal"), align="center")
        turtle.exitonclick()
    for i in range(a):
        t.forward(500 / a)
        t.left(360 / a)
    a += 1
    t.clear()
