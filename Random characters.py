import random, string

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
