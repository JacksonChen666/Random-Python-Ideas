"""This is free and unencumbered software released into the public domain.

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

For more information, please refer to <https://unlicense.org>"""

import string
import random

a = 0

def ask():
    global a
    a = int(input("How many terms do you want? "))
    if a <= 0:
        ask()
    elif a > 2000:
        a = 2000
        print("Quizlet does not allow you to import a set over 2000 terms. It has now been set to 2000.")

def main():
    with open("Quizlet terms.txt", "w") as f:
        for i in range(a):
            b = random.randint(1, 10)
            c = random.randint(1, 10)
            for n in range(b):
                f.write(random.choice(string.ascii_letters))
            f.write("\t")  # tab
            for m in range(c):
                f.write(random.choice(string.ascii_letters))
            f.write("\n")  # new line

ask()
input("Done, open the text and create a new set on quizlet, and just copy and paste in default format")