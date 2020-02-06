a = input("Text to overintensify (Discord)\n")
b = list(a)
with open("TEMP.txt", "w") as f:
    f.write("***")
    for i in range(len(a)):
        f.write(a[i])
        f.write("*")
    f.write("**")

with open("TEMP.txt", "r") as w:
    h = w.read()
    print(h)
    print(
        "This program is unoptimized for proper formatting on discord. Use the preview feature in the text field instead.")
