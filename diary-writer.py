import time


def main():
    with open("My Diary.txt", "a") as a:
        day = input("What do you want to write?\n")
        a.write("{0}\n{1}\n\n".format(time.ctime(), day))
        while True:
            ask = input("Do you have anything to add on?[y/N]\n")
            ask.lower()
            if ask == "y":
                main()
            elif ask == "n":
                print("Ok then, bye!")
                exit()
            else:
                print("I don't understand you. Can you please try again?")


main()
