# DANILO VULANOVIC TURTLE ASSESMENT

import turtle as t
screen = t.Screen()
t.speed(6)


screen.title("Turtle Drawing")

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

# AKY

screen.bgcolor('light blue')

# GRASS

t.penup()
t.goto((-SCREEN_WIDTH//2, -SCREEN_HEIGHT//2))
t.dot(7)
t.pendown()

t.fillcolor('green')
t.begin_fill()
t.forward(SCREEN_WIDTH)
t.left(90)
t.forward(SCREEN_HEIGHT//3)
t.left(90)
t.forward(SCREEN_WIDTH)
t.left(90)
t.forward(SCREEN_HEIGHT//3)

t.end_fill()

#HOUSE BODY

t.fillcolor('light yellow')
t.begin_fill()
t.penup()
t.goto(0,90)
t.pendown()
t.forward(280)   # side
t.right(90)
t.forward(220)   # bott
t.right(90)
t.forward(280)   # side
t.right(90)
t.forward(220)   # top
t.right(90)
t.end_fill()

#HOSUE ROOF

t.fillcolor('red')
t.begin_fill()

t.right(90)
t.forward(220)
t.right(120)
t.forward(220)
t.right(120)
t.forward(220)

t.end_fill()

t.penup()

# #CHIMNEY

t.pendown()
t.fillcolor('grey')
t.begin_fill()
t.left(180)
t.forward(70)
t.right(30)
t.forward(75)
t.left(90)
t.forward(30)
t.left(90)
t.forward(75)
t.left(90)
t.forward(30)
t.penup()
t.right(60)
t.forward(70)

t.end_fill()

#WINDOWS

t.right(30)
t.forward(50)
t.right(90)
t.forward(20)
t.pendown()
t.fillcolor('blue')
t.begin_fill()
for i in range (4):
    t.forward(65)
    t.left(90)
t.end_fill()

t.penup()
t.forward(115)
t.pendown()
t.fillcolor('blue')
t.begin_fill()
for i in range (4):
    t.forward(65)
    t.left(90)
t.end_fill()
t.penup()

#DOOR

t.left(90)
t.forward(230)
t.pendown()

t.fillcolor('brown')
t.begin_fill()
t.left(90)
t.forward(50)
t.left(90)
t.forward(100)
t.left(90)
t.forward(50)
t.left(90)
t.forward(100)
t.end_fill()
t.penup()


#DOG HOUSE


t.left(90)
t.forward(330)
t.right(90)
t.forward(50)
t.left(90)
t.fillcolor('brown')
t.begin_fill()
t.pendown()
t.left(90)
t.forward(70)
t.left(60)
t.forward(70)
t.left(60)
t.forward(70)
t.left(60)
t.forward(70)
t.left(90)
t.forward(70)
t.end_fill()
t.fillcolor('grey')
t.begin_fill()
t.circle(30)
t.end_fill()
t.penup()


#SUN

t.left(90)
t.forward(380)
t.right(90)
t.forward(140)
t.pendown()
t.fillcolor('yellow')
t.begin_fill()
t.circle(67)
t.end_fill()



t.done()