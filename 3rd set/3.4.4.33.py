import turtle
screen = turtle.Screen()
aik=turtle.Turtle()

location = [(120, 50), (120, 50), (30, 50), (135, 50*2**(1/2)), (135,50), (135,50*2**(1/2)),(135,50),(135,50*2**(1/2)),(135,50)]

for (x, y) in location:
    aik.left(x)
    aik.forward(y)

screen.exitonclick()
