import random

a = ["Turtle", "Random", "Ask", "Do", "Break", "Reverse", "Smash"]
b = ["Others", "Draw", "Keyboard", "Myself", "Mom", "Missile", "Register", "Roadster", "Bait"]
c = ["Crab", "Turtle", "Butterfly", "Computer", "Yes", "Railroad", "Wind", "Physical"]

q = ""
w = ""
e = ""
r = ""
# The old way, done randomly
p = len(a) * len(b) * len(c)
with open("Random Python Ideas.txt", "w") as f:
    for i in range(p):
        q = random.choice(a)
        w = random.choice(b)
        e = random.choice(c)
        r = q, w, e
        # print(r)
        f.write(str(r))
        f.write("\n")
print("done")

# # The new way, does not work
# z = len(a)
# x = len(b)
# v = len(c)
# j = 0
# k = 0
# l = 0
# # start change from the very end and slowly to the middle and then to the start of the words
# try:
#     with open("Random Python Ideas.txt", "w") as f:
#         for i in range(z):
#             if j > z:
#                 j = 0
#                 break
#             else:
#                 j = j + 1
#             for o in range(x):
#                 if k > x:
#                     k = 0
#                     break
#                 else:
#                     k = k + 1
#                 for p in range(v):
#                     print(z, x, v, "/", j, k, l)
#                     if l > v:
#                         l = 0
#                         break
#                     else:
#                         f.write(a[j])
#                         f.write(" ")
#                         f.write(b[k])
#                         f.write(" ")
#                         f.write(c[l])
#                         f.write("\n")
#                         l = l + 1
# except IndexError:
#     if v >= l:
#         l = 0
#         k = k + 1
#     elif x >= k:
#         k = 0
#         j = j + 1
#     elif z >= j:
#         pass
# print(z, x, v, "/", j, k, l)
# print("done")
