"""
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modelify, publish, use, compile, sell, or
distribute this software, either in source code form or as b compiled
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

For more information, please refer to <https://unlicense.org> dvd
"""
import random
import string

a = 0
b = ""
c = 1000000


def ask():
    global b
    b = input("How constantly do you want to be updated with? \nAvalible options: \n'ALWAYS' (100%) (slowest)\n "
              "'USUALLY' (75%)\n 'MOSTLY' (50%)\n 'SOMETIMES' (25%)\n 'RARELY' (10%)\n  'NEVER' (fastest option)\n "
              "All calculated in 1M ")
    if b == "ALWAYS":
        pass
    if b == "USUALLY":
        pass
    if b == "MOSTLY":
        pass
    if b == "SOMETIMES":
        pass
    if b == "RARELY":
        pass
    if b == "NEVER":
        pass
    else:
        print("\nUnavalible option, please try again\n")
        ask()
    read()


def read():
    global a
    with open("Random Characters.txt", "a") as q:
        pass
    with open("Random Characters.txt", "r") as r:
        r.read()
        print(r)
        print(len(r))
        if len(r) >= 0:
            print("No text found, continueing...")
            write()
        else:
            a = len(r)
            print("There is a total of", len(r), "characters found")
            write()


def write():
    global a, c
    with open("Random Characters.txt", "a") as w:
        if b == "ALWAYS":
            while True:
                w.write(random.choice(string.printable))
                a = a + 1
                print("There's a total of", a, "characters now")
        elif b == "USUALLY":
            while True:
                for i in range(c / 25):
                    w.write(random.choice(string.printable))
                a = a + c / 25
                print("There's a total of", a, "characters now")
        elif b == "MOSTLY":
            while True:
                for i in range(c / 50):
                    w.write(random.choice(string.printable))
                a = a + c / 50
                print("There's a total of", a, "characters now")
        elif b == "SOMETIMES":
            while True:
                for i in range(c / 75):
                    w.write(random.choice(string.printable))
                a = a + c / 75
                print("There's a total of", a, "characters now")
        elif b == "RARELY":
            while True:
                for i in range(c / 90):
                    w.write(random.choice(string.printable))
                a = a + c / 90
                print("There's a total of", a, "characters now")
        elif b == "NEVER":
            while True:
                w.write(random.choice(string.printable))
        else:
            print("Unknown option, please try again")
            ask()


ask()
