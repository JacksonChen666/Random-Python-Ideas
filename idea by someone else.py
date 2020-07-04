a = input("What is your full name? ")
if a == "Jackson Chen":
    print("Welcome")
else:
    with open("People who tried to get into my computer.txt", "a") as f:
        f.write(a)
        f.write("\n")
        while True:
            print("GET OUT OF HERE YOU MONSTER")
