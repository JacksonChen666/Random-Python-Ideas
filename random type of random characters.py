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

with open("Random Characters.txt", "a") as w:
    with open("Random Characters log.txt", "a") as l:
        l.write("\nLog format: \n0 is spaces\n1 is lower cases\n2 is upper cases\n3 is digits\n"
                "4 is hex digits\n5 is oct digits\n 6 is punctuation\n7 is everything\n")
        while True:
            a = 0
            a = random.randint(0, 7)
            if a == 0:
                w.write(random.choice(string.whitespace))
                l.write(str(a))
            elif a == 1:
                w.write(random.choice(string.ascii_lowercase))
                l.write(str(a))
            elif a == 2:
                w.write(random.choice(string.ascii_uppercase))
                l.write(str(a))
            elif a == 3:
                w.write(random.choice(string.digits))
                l.write(str(a))
            elif a == 4:
                w.write(random.choice(string.hexdigits))
                l.write(str(a))
            elif a == 5:
                w.write(random.choice(string.octdigits))
                l.write(str(a))
            elif a == 6:
                w.write(random.choice(string.punctuation))
                l.write(str(a))
            elif a == 7:
                w.write(random.choice(string.printable))
                l.write(str(a))
