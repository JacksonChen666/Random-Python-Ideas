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

a = 0

input("To use this file, please run it in the console. Press enter to continue")


def no_update():
    with open("Random characters.txt", "a") as f:
        print("Use CTRL+C to stop")
        while True:
            f.write(random.choice(string.printable))

def constant_update():
    with open("Random characters.txt", "a") as f:
        while True:
            f.write(random.choice(string.printable))
            a = a + 1
            print("Written a total of",a,"characters, use CTRL+C to stop")

def oneM_update():
    with open("Random characters.txt", "a") as f:
        while True:
            for i in range(1000000):
                f.write(random.choice(string.printable))
            a = a + 1000000
            print("Written a total of",a,"characters, use CTRL+C to stop")

def tenM_update():
    with open("Random characters.txt", "a") as f:
        while True:
            for i in range(10000000):
                f.write(random.choice(string.printable))
            a = a + 10000000
            print("Written a total of",a,"characters, use CTRL+C to stop")

def hundredM_update():
    with open("Random characters.txt", "a") as f:
        while True:
            for i in range(100000000):
                f.write(random.choice(string.printable))
            a = a + 100000000
            print("Written a total of", a, "characters, use CTRL+C to stop")

def oneB_update():
    with open("Random characters.txt", "a") as f:
        while True:
            for i in range(1000000000):
                f.write(random.choice(string.printable))
            a = a + 1000000000
            print("Written a total of", a, "characters, use CTRL+C to stop")


def tenB_update():
    with open("Random characters.txt", "a") as f:
        while True:
            for i in range(10000000000):
                f.write(random.choice(string.printable))
            a = a + 10000000000
            print("Written a total of", a, "characters, use CTRL+C to stop")

def hundredB_update():
    with open("Random characters.txt", "a") as f:
        while True:
            for i in range(100000000000):
                f.write(random.choice(string.printable))
            a = a + 100000000000
            print("Written a total of", a, "characters, use CTRL+C to stop")

def oneT_update():
    with open("Random characters.txt", "a") as f:
        while True:
            for i in range(1000000000000):
                f.write(random.choice(string.printable))
            a = a + 1000000000000
            print("Written a total of", a, "characters, use CTRL+C to stop")


def calculations():
    if a < 1000:
        pass
    elif a < 1000000:
        pass
    elif a < 1000000000:
        pass
    elif a < 1000000000000:
        pass
