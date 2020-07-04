import time


# noinspection PyGlobalUndefined
def ask():
    # noinspection PyGlobalUndefined
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
        print("Successful! Entering password...")
        b = "h"
        time.sleep(0.5)
        ask2()
    else:
        print("Wrong code, please try again!\n")
        ask()


def ask2():
    input("\nWhat's the password?\n")
    main()


ask()
