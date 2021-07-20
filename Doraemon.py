import turtle as trt

hello = trt.Turtle()
hello.hideturtle()
trt.hideturtle()
trt.title("Nitin Doraemon")
upper = trt.clone()
eye = trt.clone()
nose = trt.clone()
rt_hand = trt.clone()
stomach = trt.clone()
belt = trt.clone()
letter = trt.clone()
body = trt.clone()
pocket = trt.clone()
hair = trt.clone()
eye_inside = trt.clone()
locket = trt.clone()

list_char = [letter, upper, belt, locket, stomach, eye, eye_inside, rt_hand, body, hair, nose, pocket]

for i in list_char:
    i.hideturtle()
    i.pensize(3)


def write():
    letter.penup()
    letter.goto(-250, 180)
    letter.pendown()
    letter.write("DORAEMON", move=False, font=("Verdana", 18, "underline"))


def eye_part():
    eye_inside.pensize(2)
    eye_inside.penup()
    eye_inside.goto(16, 205)
    eye_inside.pendown()
    eye_inside.fillcolor('black')
    eye_inside.begin_fill()
    eye_inside.circle(10)
    eye_inside.end_fill()

    eye_inside.penup()
    eye_inside.goto(-16, 205)
    eye_inside.pendown()
    eye_inside.fillcolor('black')
    eye_inside.begin_fill()
    eye_inside.circle(10)
    eye_inside.end_fill()

    eye_inside.penup()
    eye_inside.goto(16, 210)
    eye_inside.pendown()
    eye_inside.fillcolor('white')
    eye_inside.begin_fill()
    eye_inside.circle(3)
    eye_inside.end_fill()

    eye_inside.penup()
    eye_inside.goto(-16, 210)
    eye_inside.pendown()
    eye_inside.fillcolor('white')
    eye_inside.begin_fill()
    eye_inside.circle(3)
    eye_inside.end_fill()


def face_hair():
    hair.pensize(2)
    hair.penup()
    hair.goto(20, 175)
    hair.pendown()
    hair.fd(30)
    hair.penup()
    hair.goto(20, 180)
    hair.pendown()
    hair.goto(50, 190)
    hair.penup()
    hair.goto(20, 170)
    hair.pendown()
    hair.goto(50, 162)

    hair.penup()
    hair.goto(-20, 175)
    hair.pendown()
    hair.back(30)
    hair.penup()
    hair.goto(-20, 180)
    hair.pendown()
    hair.goto(-50, 190)
    hair.penup()
    hair.goto(-20, 170)
    hair.pendown()
    hair.goto(-50, 162)


def locket_part():
    locket.fillcolor('yellow')
    locket.penup()
    locket.goto(0, 87)
    locket.pendown()
    locket.begin_fill()
    locket.circle(14)
    locket.end_fill()
    locket.pensize(2)
    locket.penup()
    locket.goto(-12, 108)
    locket.pendown()
    locket.seth(0)
    for x in range(13):
        if x <= 2:
            locket.fd(2)
            locket.lt(4)
        else:
            locket.fd(2)
            locket.rt(4)
    locket.penup()
    locket.goto(-12, 104)
    locket.pendown()
    locket.seth(0)
    for x in range(13):
        if x <= 2:
            locket.fd(2)
            locket.lt(4)
        else:
            locket.fd(2)
            locket.rt(4)

    locket.penup()
    locket.goto(0, 87)
    locket.seth(90)
    locket.pendown()
    locket.fd(10)
    locket.dot(8)


def pocket_part():
    pocket.fillcolor('white')
    pocket.penup()
    pocket.goto(0, 100)
    pocket.seth(180)
    pocket.circle(30, 90)
    pocket.pendown()
    pocket.circle(30, 180)
    pocket.seth(180)
    pocket.fd(60)


def stomach_part():
    stomach.fillcolor('white')
    stomach.penup()
    stomach.goto(0, 130)
    stomach.seth(180)
    stomach.circle(55, 53)
    stomach.pendown()
    stomach.begin_fill()
    stomach.circle(55, 254)
    stomach.seth(180)
    stomach.fd(100)
    stomach.end_fill()


def small_part():
    rt_hand.penup()
    rt_hand.fillcolor('white')
    rt_hand.goto(65, 120)
    rt_hand.lt(44)
    rt_hand.fd(50)
    rt_hand.seth(270)
    rt_hand.pendown()
    rt_hand.begin_fill()
    rt_hand.circle(20, 360)
    rt_hand.end_fill()

    rt_hand.penup()
    rt_hand.goto(75, 92)
    rt_hand.seth(270)
    rt_hand.fd(2)
    rt_hand.fd(20)
    rt_hand.rt(0.5)
    initial = 0
    for i in range(8):
        rt_hand.rt(0.5)
        initial += 3
        rt_hand.fd(initial)

    rt_hand.seth(180)
    rt_hand.fd(46)

    rt_hand.pendown()
    for i in range(20):
        rt_hand.fd(2)
        rt_hand.lt(10)
    rt_hand.seth(0)
    rt_hand.fd(46)
    for i in range(20):
        rt_hand.fd(2)
        rt_hand.lt(10)
    rt_hand.seth(180)
    rt_hand.fd(46)
    rt_hand.penup()

    rt_hand.seth(90)
    rt_hand.circle(20, 180)
    rt_hand.seth(180)

    rt_hand.fd(46)

    rt_hand.pendown()
    for i in range(20):
        rt_hand.fd(2)
        rt_hand.lt(10)
    rt_hand.seth(0)
    rt_hand.fd(46)
    for i in range(20):
        rt_hand.fd(2)
        rt_hand.lt(10)
    rt_hand.seth(180)
    rt_hand.fd(46)
    rt_hand.penup()

    rt_hand.seth(90)
    initial = 0
    for i in range(8):
        rt_hand.lt(0.4)
        initial += 3
        rt_hand.fd(initial)
    rt_hand.fd(10)

    rt_hand.seth(270)
    rt_hand.fd(15)
    rt_hand.rt(40)
    rt_hand.seth(130)
    rt_hand.fd(100)
    rt_hand.seth(284)
    rt_hand.pendown()
    rt_hand.begin_fill()
    rt_hand.circle(20, 360)
    rt_hand.end_fill()
    rt_hand.circle(20, 180)
    rt_hand.seth(284)
    rt_hand.goto(-60, 120)
    rt_hand.end_fill()
    rt_hand.speed(0)



# for making body
def body_part():
    body.fillcolor('#00a0de')
    body.penup()
    body.goto(65, 120)
    body.pendown()
    body.begin_fill()
    body.lt(44)
    body.fd(50)
    body.seth(270)
    body.circle(20, 360)

    body.circle(20, 100)
    body.seth(235)
    body.fd(86)
    body.penup()
    body.goto(75, 92)
    body.seth(270)
    body.pendown()
    body.fd(2)
    body.fd(20)
    body.rt(0.5)
    initial = 0
    for i in range(8):
        body.rt(0.5)
        initial += 3
        body.fd(initial)

    body.seth(180)
    body.pencolor('white')
    body.fd(46)

    body.pencolor('black')
    body.seth(90)
    body.circle(20, 180)
    body.seth(180)

    body.pencolor('white')
    body.fd(46)

    body.pencolor('black')
    body.seth(90)
    initial = 0
    for i in range(8):
        body.lt(0.4)
        initial += 3
        body.fd(initial)
    body.fd(10)

    body.seth(270)
    body.fd(15)
    body.rt(40)
    body.seth(130)
    body.fd(100)
    body.seth(284)
    body.circle(20, 360)
    body.circle(20, 180)
    body.seth(284)
    body.goto(-60, 122)
    body.seth(270)
    body.fd(15)
    body.seth(0)
    body.fd(125)
    body.lt(90)
    body.fd(15)
    body.end_fill()

    small_part()


def belt_make():
    belt.fillcolor('red')
    belt.penup()
    belt.goto(-60, 122)
    belt.pendown()
    belt.begin_fill()
    belt.fd(125)
    belt.rt(90)
    belt.fd(15)
    belt.rt(90)
    belt.fd(125)
    belt.rt(90)
    belt.fd(15)
    belt.end_fill()


def nose_make():
    nose.fillcolor('red')
    nose.penup()
    nose.goto(0, 187)
    nose.pendown()
    nose.begin_fill()
    nose.circle(10)
    nose.end_fill()
    nose.rt(90)
    nose.fd(50)
    nose.rt(90)
    for x in range(28):
        nose.rt(1.2)
        nose.fd(2)
    nose.penup()
    nose.goto(0, 137)
    nose.lt(217)
    # nose.fd(-2)
    nose.pendown()
    for x in range(28):
        nose.lt(1.2)
        nose.fd(2)


def eye_make():
    # global eye
    eye.fillcolor('white')
    eye.penup()
    eye.goto(20, 200)
    eye.pendown()
    eye.begin_fill()
    eye.circle(21)
    eye.end_fill()
    eye.penup()
    eye.lt(90)
    eye.fd(10)
    eye.lt(50)
    eye.fd(38)
    eye.pendown()
    eye.begin_fill()
    eye.circle(21)
    eye.end_fill()


#for making head
def upper_part():
    upper.fillcolor('#00a0de')
    upper.penup()
    upper.goto(0, 100)
    upper.circle(90, 40)
    upper.pendown()

    upper.begin_fill()
    upper.circle(90, 280)
    upper.end_fill()
    upper.penup()
    upper.home()
    upper.goto(0, 100)
    upper.circle(68, 48)
    upper.pendown()
    upper.fillcolor('white')
    upper.begin_fill()
    upper.circle(68, 100)
    upper.seth(180)
    upper.fd(70)
    upper.seth(209)
    upper.circle(68, 102)
    upper.end_fill()

    belt_make()
    eye_make()
    eye_part()
    nose_make()
    face_hair()


# main function which have control of all function
def N_Programmer():
    hello.penup()
    hello.goto(40,-180)
    hello.pendown()
    write()
    upper_part()
    body_part()
    stomach_part()
    pocket_part()
    locket_part()
    hello.write("By N programmer",move=False,font=("Verdana", 20, "underline"))


if __name__=='__main__':
    N_Programmer()

trt.speed(0)
trt.mainloop()
