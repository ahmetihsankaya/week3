import turtle
screen = turtle.Screen()
aik=turtle.Turtle()
aik.shape("turtle")
angles=[160, -43, 270, -97, -43, 200, -940, 17,-86]

for _ in angles:
    aik.forward(100)
    aik.left(_)

screen.exitonclick()