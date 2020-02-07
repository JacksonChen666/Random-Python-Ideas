"""
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
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
    b = input("How constantly do you want to be updated with? \nAvalible options: \n'Always' (100%) (slowest)\n "
              "'Usually' (75%)\n 'Mostly' (50%)\n 'Sometimes' (25%)\n 'Rarely' (10%)\n  'Never' (fastest option)\n "
              "All calculated in 1M ")
    print(b)
    if b == "Always":
        pass
    if b == "Usually":
        pass
    if b == "Mostly":
        pass
    if b == "Sometimes":
        pass
    if b == "Rarely":
        pass
    if b == "Never":
        pass
    else:
        print("\nUnavailable option, please try again\n")
        ask()
    # read()
    write()


# def read():
#     global a
#     with open("Random Characters.txt", "a") as q:
#         pass
#     with open("Random Characters.txt", "r") as r:
#         r.read()
#         print(r)
#         print(len(r))
#         if len(r) >= 0:
#             print("No text found, continueing...")
#             write()
#         else:
#             a = len(r)
#             print("There is a total of", len(r), "characters found")
#             write()


def write():
    global a, c
    with open("Random Characters.txt", "a") as w:
        if b == "ALWAYS":
            while True:
                w.write(random.choice(string.printable))
                a += 1
                print("Written a total of {} characters".format(c / 1))
        elif b == "USUALLY":
            while True:
                for i in range(c / 25):
                    w.write(random.choice(string.printable))
                a = a + c / 25
                print("Written a total of {} characters".format(c / 25))
        elif b == "MOSTLY":
            while True:
                for i in range(c / 50):
                    w.write(random.choice(string.printable))
                a = a + c / 50
                print("Written a total of {} characters".format(c / 50))
        elif b == "SOMETIMES":
            while True:
                for i in range(c / 75):
                    w.write(random.choice(string.printable))
                a = a + c / 75
                print("Written a total of {} characters".format(c / 75))
        elif b == "RARELY":
            while True:
                for i in range(c / 90):
                    w.write(random.choice(string.printable))
                a = a + c / 90
                print("Written a total of {} characters".format(c / 90))
        elif b == "NEVER":
            while True:
                w.write(random.choice(string.printable))
        else:
            print("Unknown option, please try again")
            ask()


ask()
