r = 0
g = 0
b = 0
inputs = ""
line = 0


# How it should work:
# Adds 1 to blue, then if it is over 255, add 1 to green, then if it goes over again, add 1 to red and stop if over 255
def main():
    global r, g, b
    with open("RGB numbers.txt", "w") as n:
        while True:
            # print(r, g, b)
            n.write("{} {} {}\n".format(r, g, b))
            b += 1
            if b > 255:
                b = 0
                g += 1
            if g > 255:
                r += 1
                g = 0
            if r > 255:
                print("Done")
                read()


# def read():
#     global inputs, r, g, b
#     inputs = input("Would you like the file to be printed?\n")
#     inputs.lower()
#     if inputs == "y":
#         while True:
#             print("{} {} {}".format(r, g, b))
#             b += 1
#             if b > 255:
#                 b = 0
#                 g += 1
#             if g > 255:
#                 r += 1
#                 g = 0
#             if r > 255:
#                 print("Done")
#     else:
#         print("Ok, bye")
#         exit()


while True:
    main()
    read()
