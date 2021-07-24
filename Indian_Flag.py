# Program to make Indain Flag using Turtle

import turtle as nitin

flag = nitin.Turtle()
flag.hideturtle()
nitin.hideturtle()


def block():
    flag.fd(300)
    flag.rt(90)
    flag.fd(210)
    flag.rt(90)
    flag.fd(300)
    flag.rt(90)
    flag.fd(210)


def rect(color):
    flag.fillcolor(color)
    flag.begin_fill()
    flag.fd(300)
    flag.rt(90)
    flag.fd(70)
    flag.rt(90)
    flag.fd(300)
    flag.rt(90)
    flag.fd(70)
    flag.end_fill()


nitin.penup()
nitin.goto(-60, 250)
nitin.write("Indian Flag", move=False, font=("Verdana", 25, "underline"))

flag.pensize(4)
flag.penup()
flag.goto(-200, -300)
flag.pendown()
flag.goto(-200, 200)
flag.pensize(2)
block()

flag.seth(0)
rect('orange')
flag.penup()
flag.goto(-200, 60)
flag.seth(0)
flag.pendown()
rect('green')

flag.penup()
flag.goto(-85, 95)
flag.pendown()
flag.circle(-35)
flag.pensize(1)
flag.goto(-50, 95)
for i in range(24):
    flag.fd(35)
    flag.bk(35)
    flag.lt(15)

nitin.penup()
nitin.goto(-100, -250)
nitin.write("By N Programmer", move=False, font=("Verdana", 18, "underline"))

nitin.speed(1)

nitin.mainloop()
