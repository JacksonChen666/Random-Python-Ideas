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
