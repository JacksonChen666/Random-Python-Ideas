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
a = int(input("What is the target number?\n"))
b = int(input("What is the starting number?\n"))
c = int(input("What opreation do you want? (1 is +, 2 is -, 3 is * and 4 is /)\n"))
d = int(input("By how much do you want to change? (Decimal points not allowed)\n"))
e = 0
f = 0
g = b

if c == 1:
    if b > a:
        print("Unsupported Opreation, please check in later for a new version.")
        exit()
    while True:
        if b == a:
            print("Yay! It took {} times(s) to reach {} from {}".format(e, a, g))
            exit()
        elif b > a:
            print("Oops! The number {} has gone above the target number {} and is now aborting!".format(g, a))
            exit()
        elif a > b:
            b += d
            e += 1
            if e == 1000000:
                print("Math Intensifies (Calculation took over 1M tries)")
            elif e == 1000000000:
                print("MATH INTENSIFIES (Calculation took over 1B tries)")
        elif e == 1000000000000:
            print("MATH OVER-INTENSIFIES (Calculation took over 1T tries)")
        else:
            print("Umm... what just happened?")
            raise InterruptedError
else:
    print("Unsupported Opreation")
