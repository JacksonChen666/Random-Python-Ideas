import time

try:
    a = 1
    start = time.time()
    time.sleep(a)
    end = time.time()
    print("The program ran for a total of", end - start, "seconds with a extra times of", end - start - a, "seconds.")
    exit()
except KeyboardInterrupt:
    print("Canceled")
    exit()
