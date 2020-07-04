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
