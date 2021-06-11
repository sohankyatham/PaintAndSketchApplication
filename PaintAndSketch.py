# Imports
import turtle



# Screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Paint & Sketch Application")
screen.bgcolor("White")



# User
user = turtle.Turtle()
user.shape("triangle")
user.setheading(90)
user.goto(0, 0)
userspeed = 15
user.color("Black")



# Movement
def moveUp():
    y = user.ycor()
    y += userspeed
    if y > 300:
        y = 300
    user.sety(y)
    user.setheading(90)

def moveDown():
    y = user.ycor()
    y -= userspeed
    if y < -300:
        y = -300
    user.sety(y)
    user.setheading(-90)

def moveRight():
    x = user.xcor()
    x += userspeed
    if x > 300:
        x = 300
    user.setx(x)
    user.setheading(0)

def moveLeft():
    x = user.xcor()
    x -= userspeed
    if x < -300:
        x = -300
    user.setx(x)
    user.setheading(60)



# Keyboard Binding For Movement
turtle.listen()
turtle.onkey(moveUp, "Up")
turtle.onkey(moveDown, "Down")
turtle.onkey(moveRight, "Right")
turtle.onkey(moveLeft, "Left")



# Color
def whiteColor():
    user.color("white")

def blackColor():
    user.color("black")

def redColor():
    user.color("red")

def orangeColor():
    user.color("orange")

def yellowColor():
    user.color("yellow")

def greenColor():
    user.color("green")

def blueColor():
    user.color("blue")

def indigoColor():
    user.color("indigo")

def violetColor():
    user.color("violet")



# Keyboard Binding For Colors
turtle.listen()
turtle.onkey(whiteColor, "w")
turtle.onkey(blackColor, "l")
turtle.onkey(redColor, "r")
turtle.onkey(orangeColor, "o")
turtle.onkey(yellowColor, "y")
turtle.onkey(greenColor, "g")
turtle.onkey(blueColor, "b")
turtle.onkey(indigoColor, "i")
turtle.onkey(violetColor, "v")



# User Width Functions
def WidthOne():
    user.width(1)

def WidthTwo():
    user.width(2)

def WidthThree():
    user.width(3)

def WidthFour():
    user.width(4)

def WidthFive():
    user.width(5)

def WidthSix():
    user.width(6)

def WidthSeven():
    user.width(25)

def WidthEight():
    user.width(50)

def WidthNine():
    user.width(75)

def WidthTen():
    user.width(100)


# Keyboard Bindings for User Width
turtle.listen()
turtle.onkey(WidthOne, "1")
turtle.onkey(WidthTwo, "2")
turtle.onkey(WidthThree, "3")
turtle.onkey(WidthFour, "4")
turtle.onkey(WidthFive, "5")
turtle.onkey(WidthSix, "6")
turtle.onkey(WidthSeven, "7")
turtle.onkey(WidthEight, "8")
turtle.onkey(WidthNine, "9")
turtle.onkey(WidthTen, "0")



# Mainloop
screen.mainloop()
