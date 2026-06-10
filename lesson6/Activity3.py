import turtle

# creating canvas
turtle.Screen().bgcolor("Orange")

sc = turtle.Screen()
sc.setup(400,300)

turtle.title("welcome to Turtle Window")

# turtle object creation
pen = turtle.Turtle()

# creating a square
for i in range(3):
    pen.forward(50)
    pen.left(120)
    i = i+1

for i in range(2):
    pen.forward(100)
    pen.left(90)
    pen.forward(200)
    pen.left(90)
    i = i+1

