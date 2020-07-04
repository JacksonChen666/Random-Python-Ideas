import random
import string

while True:
    a = []
    for i in range(1000000):
        a.append(random.choice(string.printable))
    print(a)
