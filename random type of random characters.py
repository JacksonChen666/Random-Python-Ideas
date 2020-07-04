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
