a = int(input("What is the target number?\n"))
b = int(input("What is the starting number?\n"))
c = int(input("What opreation do you want? (1 is +, 2 is -, 3 is * and 4 is /)\n"))
d = int(input("By how much do you want to change? (Decimal points not allowed)\n"))
e = 0
f = 0
g = b

if c == 1:
    if b > a:
        print("Unsupported Opreation, please check in later for a new version.")
        exit()
    while True:
        if b == a:
            print("Yay! It took {} times(s) to reach {} from {}".format(e, a, g))
            exit()
        elif b > a:
            print("Oops! The number {} has gone above the target number {} and is now aborting!".format(g, a))
            exit()
        elif a > b:
            b += d
            e += 1
            if e == 1000000:
                print("Math Intensifies (Calculation took over 1M tries)")
            elif e == 1000000000:
                print("MATH INTENSIFIES (Calculation took over 1B tries)")
        elif e == 1000000000000:
            print("MATH OVER-INTENSIFIES (Calculation took over 1T tries)")
        else:
            print("Umm... what just happened?")
            raise InterruptedError
else:
    print("Unsupported Opreation")
