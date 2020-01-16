import random
import string

a = 0
def ask():
    global a
    a = int(input("How many random characters do you want?\n"))
    if a <= 0:
        ask()


def main():
    with open("Random Characters.txt", "a") as f:
        for i in range(a):
            f.write(random.choice(string.printable))
        print("done",a,"more character(s)")


ask()
main()