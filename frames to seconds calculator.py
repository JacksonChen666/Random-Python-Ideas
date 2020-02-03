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
print("The way to calculate FPS (Frames Per Second) to seconds is 1 divided by the FPS for example 1/60")
try:
    a = int(input("What is the FPS?\n"))
    b = int(input("How many frames?\n"))
    c = 1 / a
    d = c * b
    print("\nDebug info:\nFPS: {}\nFrames: {}\n1 Frame of {} FPS: {}\nMain Output: {}".format(a, b, a, c, d))
    print("\nMath: ({}/{})*{}".format("1", a, b))
    print("\nThe FPS is {} so {} frames is a total of {} seconds".format(a, b, d))
except ValueError:
    print("Not a number, exiting")
    exit()
