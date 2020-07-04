"""1234567890qwertyuiopasdfghjklzxcvbnm!@#$%^&*(QWETYIOPSDGHJLZCVB"""
import random

a = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd',
     'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '!', '@', '#', '$', '%', '^', '&', '*', '(', 'Q',
     'W', 'E', 'T', 'Y', 'I', 'O', 'P', 'S', 'D', 'G', 'H', 'J', 'L', 'Z', 'C', 'V', 'B']
m = 1000
b = "{0}"
s = []

for i in range(m):
    s.append(random.choice(a))
    s.append(b)
print(s)
