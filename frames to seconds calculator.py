print("The way to calculate FPS (Frames Per Second) to seconds is 1 divided by the FPS for example 1/60")
try:
    a = int(input("What is the FPS?\n"))
    b = int(input("How many frames?\n"))
    c = 1 / a
    d = c * b
    print("\nDebug info:\nFPS: {0}\nFrames: {1}\n1 Frame of {0} FPS: {2}\n{2} Frames of {1} FPS: {3}".format(a, b, c,
                                                                                                             d))
    print("Math: ({}/{})*{}".format("1", a, b))
    print("\nThe FPS is {} so {} frames is a total of {} seconds".format(a, b, d))
except ValueError:
    print("Not a number, exiting")
    exit()
