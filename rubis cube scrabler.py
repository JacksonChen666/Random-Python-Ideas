import os
import random

a = ["F", "R", "U", "B", "L", "D", "F'", "R'", "U'", "B'", "L'", "D'"]
b = []
times = int(input("How many moves for scrambling?\n"))

with open("TEMP.txt", "w") as t:
    for i in range(times):
        t.write(random.choice(a))
        t.write(" ")

with open("TEMP.txt") as r:
    d = r.read()

print(d)

os.remove(os.path.realpath("TEMP.txt"))
