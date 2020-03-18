import turtle
screen = turtle.Screen()
aik=turtle.Turtle()
aik.shape("turtle")

location = [(160, 20), (-43, 10), (270, 8), (-43, 12)]

for (x, y) in location:
    aik.left(x)
    aik.forward(y)

screen.exitonclick()
