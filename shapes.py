import turtle

t = turtle.Pen()
s = turtle.Screen()
a = 2
t.speed(5)

while True:
    t.write(a, font=("Arial", 50, "normal"), align="center")
    if a >= 11:
        t.speed(0)
        s.tracer(5)
    if a > 49 < 98:
        s.tracer(10)
    if a > 99 < 498:
        s.tracer(100)
    if a > 499 < 1000:
        s.tracer(500)
    if a > 1001:
        t.clear()
        t.write("The limit of sides has reached\nPlease click to exit", font=("Arial", 20, "normal"), align="center")
        turtle.exitonclick()
    for i in range(a):
        t.forward(500 / a)
        t.left(360 / a)
    a += 1
    t.clear()
