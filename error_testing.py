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
    print("Press Ctrl+C (all systems)")
    while True:
        pass


def valueerror():
    while True:
        a = int(input("Enter a number or not a number: "))
        break


def indexerror():
    b = [1, 2, 3]
    b[3]


def modulenotfounderror():
    pass


def keyerror():
    r = {'1': "aa", '2': "bb", '3': "cc"}
    r['4']


def importerror():
    pass


def stopiteration():
    it = iter([1, 2, 3])
    for i in range(4):
        next(it)


def type():
    '2' + 2


def value():
    int("asifg")


def name():
    h


def zerodivision():
    q = 100 / 0

# valueerror()
# indexerror()
# modulenotfounderror()
# keyerror()
# importerror()
# stopiteration()
# type()
# value()
# name()
# zerodivision()
# keyboardinterrupt()
