#Jakub Novak
import turtle as t

#Screen setup

screen = t.Screen()
screen.title("Turtle Dimension")

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("light blue")

#Draw green rectangle at the bottom of the screen

t.penup()
t.goto((-SCREEN_WIDTH//2 , -SCREEN_HEIGHT//2))
t.dot(7)
t.speed(10)
t.pendown()

#Ground

t.fillcolor("green")
t.begin_fill()
t.forward(SCREEN_WIDTH)
t.left(90)
t.forward(SCREEN_HEIGHT//3)
t.left(90)
t.forward(SCREEN_WIDTH)
t.left(90)
t.forward(SCREEN_HEIGHT//3)

t.end_fill()
t.penup()
t.back(SCREEN_HEIGHT//3)
t.left(90)
t.forward(250)
t.right(90)
t.forward(60)
t.left(90)
t.pendown()

#Base

t.fillcolor("pink")
t.begin_fill()
t.forward(300)
t.left(90)
t.forward(300)
t.left(90)
t.forward(300)
t.left(90)
t.forward(300)
t.end_fill()
t.penup()

t.left(90)
t.forward(125)

#Door

t.pendown()
t.fillcolor("brown")
t.begin_fill()
t.forward(50)
t.left(90)
t.forward(100)
t.left(90)
t.forward(50)
t.left(90)
t.forward(100)
t.left(90)
t.end_fill()
t.penup()

#Window1

t.left(90)
t.forward(200)
t.pendown()
t.fillcolor("light blue")
t.begin_fill()
t.left(90)
t.forward(75)
t.left(90)
t.forward(75)
t.left(90)
t.forward(75)
t.left(90)
t.forward(75)
t.end_fill()

t.penup()
t.right(90)
t.forward(50)

#Window2

t.pendown()
t.begin_fill()
t.forward(75)
t.right(90)
t.forward(75)
t.right(90)
t.forward(75)
t.right(90)
t.forward(75)
t.end_fill()

t.penup()
t.right(90)
t.forward(125)
t.left(90)
t.forward(100)

#Roof

t.pendown()
t.fillcolor("red")
t.begin_fill()
t.left(45)
t.forward(212)
t.left(90)
t.forward(212)
t.left(45)
t.left(90)
t.forward(300)
t.left(135)
t.end_fill()

t.penup()
t.forward(50)

#Chimney 

t.pendown()
t.fillcolor("black")
t.begin_fill()
t.right(45)
t.forward(100)
t.left(90)
t.forward(30)
t.left(90)
t.forward(70)
t.left(45)
t.forward(45)
t.end_fill()
#End program
t.hideturtle()
t.done()
