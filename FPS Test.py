from time import sleep

print("This FPS Test may not be as fast as expected if used with different programs to run. Please use your system's "
      "console if possible.")
fps = int(input("What FPS do you want to test?\n"))
times = int(input("How long do you want the test to last for in seconds?\n"))
a = fps * times
b = 1 / fps
c = 0
input("Get your camera ready on slo-mo mode and start recording the screen, and press enter if you are ready.")
for i in range(int(a)):
    c += 1
    sleep(b)
    print(c)
