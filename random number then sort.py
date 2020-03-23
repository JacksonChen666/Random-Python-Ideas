import random
import time


def numbers(number):
    global a
    if number is None:
        number: int = 10
    times = []
    eraseAttempts()
    b = 0
    seed = random.randint(0, 999999999)
    random.seed(seed)
    print("Your random seed is {0}".format(seed))
    starting = time.time()
    while True:
        a = []
        for i in range(number):
            a.append(random.randint(0, number))
        a = list(dict.fromkeys(a))
        b += 1
        # print("{0}/{1}".format(len(a),number))

        if len(a) == number:
            ending = time.time()
            print("It took {0} tries to get to {1} (It took {2} seconds)\n".format(b, number,
                                                                                   round(ending - starting, 2)))
            a = sorted(a)
            with open("RNTS.txt", "w") as h:
                h.write(str(a))
            break
        else:
            # writeAttempts("{0}/{1}\n".format(len(a), number))
            pass


def writeAttempts(fileName="RNTS Attempts", text=None):
    global a, number
    if text is None:
        text = "{0}/{1}\n".format(len(a), number)
    with open("{}.txt".format(fileName), "a") as h:
        h.write(text)  # "{0}/{1}".format(len(a), number


def writeList(fileName="RNTS", text=None):
    global a
    if text is None:
        text = a
    with open("{}.txt".format(fileName), "w") as q:
        q.write(text)


def eraseAttempts(fileName="RNTS Attempts"):
    with open("{}.txt".format(fileName), "w") as w:
        pass


for i in range(50):
    numbers(i)
