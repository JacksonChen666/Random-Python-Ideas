from os import remove


def main():
    a = input("Text to over-intensify (Discord ONLY)\n")
    with open("TEMP.txt", "w") as f:
        f.write("**")
        for i in range(len(a)):
            if a[i] == " ":
                f.write(" *")
            else:
                f.write("*")
                f.write(a[i])
        f.write("**")
    with open("TEMP.txt") as w:
        h = w.read()
        print(h)
        remove("TEMP.txt")


main()
