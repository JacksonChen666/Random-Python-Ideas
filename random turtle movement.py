import random
import turtle

t = turtle.Pen()
t.speed(0)
t.ht()
t.up()
s = turtle.Screen()
s.tracer(0)
s.setup(width=1.0, height=1.0)
a = turtle.window_width()
b = turtle.window_height()


def edgeCheck():
    if t.xcor() > a - 550:
        print("Right")
        t.goto(t.xcor() - 200, t.ycor())
    if t.ycor() > b - 550:
        print("Top")
        t.goto(t.xcor(), t.ycor() - 200)
    if t.xcor() < a * -1 + 850:
        print("Left")
        t.goto(t.xcor() + 100, t.ycor())
    if t.ycor() < b * -1 + 850:
        print("Bottom")
        t.goto(t.xcor(), t.ycor() + 100)


def exits():
    exit()


def main():
    turtle.title("Shakey")
    t.clear()
    t.goto(0, 0)
    turtle.onscreenclick(t.goto)
    a = turtle.textinput("Text", "What text on the screen do you want?")
    b = turtle.textinput("Shakeyness", "How many pixels for shakyness? (recommended: 25)")
    turtle.title("Shakey {}".format(a))
    try:
        while True:
            # print(t.xcor(),t.ycor())
            t.forward(random.uniform(0, int(b)))
            t.right(random.uniform(0, 360))
            t.write(a, font=("Arial", 100, "normal"))
            edgeCheck()
            s.update()
            t.clear()
    except turtle.Terminator as err:
        print("User closed turtle window, aborting")
        exit()
    except TypeError as err:
        print(err)
        t.goto(-600, 0)
        t.write("Error: {}\nClick to exit".format(err), font=("arial", 25, "normal"))
        s.update()
        turtle.exitonclick()
        raise TypeError
    except ValueError as err:
        print(err)
        t.goto(-600, 0)
        t.write("Error: {}\nClick to exit".format(err), font=("arial", 25, "normal"))
        s.update()
        turtle.exitonclick()
        raise ValueError
    except KeyboardInterrupt:
        print("User Cancellation")
        raise KeyboardInterrupt


main()
