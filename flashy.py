import random
import turtle

t = turtle.Pen()

t.ht()

t.write("Flashy", font=("Arial", 200, "normal"), align="center")
try:
    while True:
        turtle.bgcolor(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
except turtle.Terminator:
    print("Turtle stopped without warning, exiting")
    exit()
