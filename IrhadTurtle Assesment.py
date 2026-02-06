##Turtle Graphics Score Assignment

import turtle as t


## Screen setup

screen = t.Screen()
screen.title("Turtle Creation")

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("Light Blue")

##Draw big retangle at the bottom of the screen
##Grass
t.penup()
t.goto((-SCREEN_WIDTH/2, -SCREEN_HEIGHT//2))
t.dot(7)
t.pendown()

t.fillcolor("dark green")
t.begin_fill()
t.forward(SCREEN_WIDTH)
t.left(90)
t.forward(SCREEN_HEIGHT//3)
t.left(90)
t.forward(SCREEN_WIDTH)
t.left(90)
t.forward(SCREEN_HEIGHT//3)
t.left(90)
t.end_fill()


#Trailer
t.penup()
t.goto((200, -100))
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.left(180)
t.forward(300)
t.right(90)
t.forward(100)
t.right(90)
t.forward(300)
t.right(90)
t.forward(100)
t.right(90)
t.forward(300)
t.end_fill()
#Truck Front
t.penup()
t.goto((-100, -50))
t.pendown()
t.fillcolor("grey")
t.begin_fill()

t.right(90)
t.forward(120)
t.left(90)
t.forward(70)
t.left(90)
t.forward(60)
t.right(90)
t.forward(40)
t.left(90)
t.forward(60)
t.left(90)
t.forward(110)
t.end_fill()
#Wheels
t.penup()
t.goto((-100, -125))

t.pendown()
t.begin_fill()
t.circle(25)
t.fillcolor("black")
t.end_fill()

t.penup()
t.goto((200, -125))
t.pendown()
t.begin_fill()
t.circle(25)
t.fillcolor("black")
t.end_fill()










t.hideturtle()
#End Program
t.done()

