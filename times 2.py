import string
a = 1
b = []
c = 1000
d = 0
with open("Times 2.txt","w") as f:
    while True:
        c = c * 1000
        print("Calculated a total of",c,"numbers")
        for i in range(1000):
            a = a * 2
            b.append(a)
        f.write(str(b))
        f.write("\n")
        b.clear()