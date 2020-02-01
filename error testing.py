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


def keyboardinterrupt():
    try:
        print("Press Ctrl+C (all systems)")
        while True:
            True
    except KeyboardInterrupt as error:
        print("Error: User requested cancellation, the actions has been canceled")


def valueerror():
    try:
        while True:
            a = int(input("Enter a number or not a number: "))
            break
    except ValueError as error:
        print("Error: Not a number:\n{}".format(error))


def indexerror():
    try:
        b = [1, 2, 3]
        b[3]
    except IndexError as error:
        print("Error: Tried to access an invalid index:\n{}".format(error))


def modulenotfounderror():
    try:
        import asjfghowieurgowehrbuwhrboguawbrgaufwlf
    except ModuleNotFoundError as error:
        print("Error: Tried to import an invalid module:\n{}".format(error))


def keyerror():
    try:
        r = {'1': "aa", '2': "bb", '3': "cc"}
        r['4']
    except KeyError as error:
        print("Error: Key not found: \n{0}".format(error))


def importerror():
    try:
        from math import soifhgw
    except ImportError as error:
        print("Error: Tried to import a invalid function:\n{}".format(error))


def stopiteration():
    try:
        it = iter([1, 2, 3])
        for i in range(4):
            next(it)
    except StopIteration as error:
        print("Error: Unable to find the next iterator item:\n{}".format(error))


def type():
    try:
        '2' + 2
    except TypeError as error:
        print("Error: Invalid Stuff:\n{}".format(error))


def value():
    try:
        int("asifg")
    except ValueError as error:
        print("Error: Attempted to turn non int to int:\n{}".format(error))


def name():
    try:
        h
    except NameError as error:
        print("Error: Object not found:\n{}".format(error))


def zerodivision():
    try:
        q = 100 / 0
    except ZeroDivisionError as error:
        print("Error: Attempted to divide a number with 0:\n{}".format(error))


valueerror()
indexerror()
modulenotfounderror()
keyerror()
importerror()
stopiteration()
type()
value()
name()
zerodivision()
keyboardinterrupt()
