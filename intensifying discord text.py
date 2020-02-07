import os

a = input("Text to overintensify (Discord)\n")
b = list(a)
with open("TEMP.txt", "w") as f:
    f.write("***")
    for i in range(len(a)):
        if b[i] == " ":
            f.write(" ")
        else:
            f.write(a[i])
            f.write("*")
    f.write("**")

with open("TEMP.txt", "r") as w:
    h = w.read()
    print(h)
    os.remove("TEMP.txt")
