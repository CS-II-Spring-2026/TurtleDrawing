import turtle as t

screen =t.Screen()
screen.title("turtle Dimenaions")

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("light blue")
t.penup()
t.goto((-SCREEN_WIDTH//2 , -SCREEN_HEIGHT//2))
t.dot(7)
t.pendown()

#grass
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


#house
t.penup()
t.setheading(0)
t.goto(-100, -100)
t.pendown()
t.fillcolor("tan")
t.begin_fill()
for _ in range(4):
    t.forward(200)
    t.left(90)
t.end_fill()

#chimney
t.penup()
t.goto(90, 120)
t.setheading(0)
t.pendown()

t.fillcolor("brown")
t.begin_fill()
t.forward(40)
t.left(90)
t.forward(80)
t.left(90)
t.forward(40)
t.left(90)
t.forward(80)
t.end_fill()



# Roof
t.penup()
t.goto(-140, 100)
t.setheading(0)
t.pendown()

t.fillcolor("red")
t.begin_fill()
t.forward(280)
t.left(120)
t.forward(280)
t.left(120)
t.forward(280)
t.end_fill()

#door
t.penup()
t.goto(-20, -100)
t.setheading(0)
t.pendown()

t.fillcolor("brown")
t.begin_fill()
t.forward(40)
t.left(90)
t.forward(80)
t.left(90)
t.forward(40)
t.left(90)
t.forward(80)
t.end_fill()

#sun
t.penup()
t.goto(370, 220)
t.setheading(0)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
t.circle(70)
t.end_fill()

#window
t.penup()
t.goto(-40, 40)
t.setheading(0)
t.pendown()
t.fillcolor("dark blue")
t.begin_fill()
t.circle(20)
t.end_fill()

#window 2
t.penup()
t.goto(40, 40)
t.setheading(0)
t.pendown()
t.fillcolor("dark blue")
t.begin_fill()
t.circle(20)
t.end_fill()


t.hideturtle()
t.done()
