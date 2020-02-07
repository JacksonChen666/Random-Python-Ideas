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

a = 0  # min
b = 0  # max
c = 0  # amount of signs
d = []  # math problem
e = 0  # which sign
p = 0  # problems created
h = str(d)  # turns d into string


def ask():
    global a, b, c, p
    a = input("\nMinimum number\n")
    b = input("\nMaximum Number\n")
    if a > b:
        print("Sorry, but you can't have a minimum number larger than a maximum number. Please try again")
        ask()
    c = input("\nHow many signs in the math problem? (+,-,*./)\n")
    p = input("\nHow many problems do you want?\n")
    sel()


def sel():
    global a, b, c, d, p, h, e
    with open("Math problems.txt", "a") as m:
        for p in range(int(p)):
            for c in range(int(c)):
                d.append(random.randint(a, b))
                e = random.randint(0, 3)
                if e == 0:
                    d.append("+")
                elif e == 1:
                    d.append("-")
                elif e == 2:
                    d.append("*")
                elif e == 3:
                    d.append("/")
            d.append(random.randint(a, b))
            m.write("\n")
    print("\nYour math problem has been successfully written into a text document in the same folder as the code!\n")
    repeat()


def repeat():
    q = ""
    q = input("\nWould you like to continue creating more math problems (YES or NO)?\n")
    if q == "YES":
        ask()
    elif q == "NO":
        exits()
    elif q == "yES":
        ask()
    elif q == "yeS":
        ask()
    elif q == "yes":
        ask()
    elif q == "Yes":
        ask()
    elif q == "YEs":
        ask()
    elif q == "yEs":
        ask()
    elif q == "yeS":
        ask()
    elif q == "nO":
        exits()
    elif q == "No":
        exits()
    elif q == "no":
        exits()
    else:
        unknown()
        repeat()


def unknown():
    print("\nI didn't understand you, can you please try again?\n")


def exits():
    print("\nThanks for using random math problem generator, the program will now exit.\n")
    exit()


ask()
