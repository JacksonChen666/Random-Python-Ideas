"""1234567890qwertyuiopasdfghjklzxcvbnm!@#$%^&*(QWETYIOPSDGHJLZCVB"""
import random

a = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd',
     'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '!', '@', '#', '$', '%', '^', '&', '*', '(', 'Q',
     'W', 'E', 'T', 'Y', 'I', 'O', 'P', 'S', 'D', 'G', 'H', 'J', 'L', 'Z', 'C', 'V', 'B']
n = 100
b = 0
q = "{0}"
w = "{1}"
with open("Virtual Piano Random Notes (Don't forget to remove all spaces!).txt", "w") as f:
    n = input("How many notes do you want (Default 100)? ")
    while True:
        b += 1
        if n == b:
            print("Opreation completed")
            break
        elif n >= b:
            f.write(random.choice(a))
            f.write("{0}")
