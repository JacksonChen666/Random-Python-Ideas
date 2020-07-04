from time import sleep

a = 1

while True:
    print(a)
    sleep(a)
    a /= 2
    if a == 0:
        exit()
