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
import time


def ask():
    global b
    b = input("What is the password?\n")
    main()


def main():
    global b
    if b == "h":
        print("The password is 0123456789")
        exit()
    elif b == "h4ck3r m0d3 666":
        time.sleep(0.5)
        print("Connecting to hacking server...")
        time.sleep(5)
        print("Requesting data...")
        time.sleep(2)
        print("Receiving data...")
        time.sleep(5)
        print("Decoding encrypted data...")
        time.sleep(10)
        print("Reading data....")
        time.sleep(3)
        print("Succsessful! Entering password...")
        b = "h"
        time.sleep(0.5)
        ask2()
    else:
        print("Wrong code, please try again!\n")
        ask()


def ask2():
    input("\n   What's the password?\n")
    main()


ask()
