import turtle
window = turtle.Screen()
window.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")

tess.stamp()
tess.penup()
tess.forward(100)
tess.pendown()
tess.forward(20)
tess.penup()
tess.forward(20)
tess.stamp()
tess.backward(140)

for _ in range(11):

    tess.left(30)
    tess.penup()
    tess.forward(100)
    tess.pendown()
    tess.forward(20)
    tess.penup()
    tess.forward(20)
    tess.stamp()
    tess.backward(140)

tess.hideturtle()
window.exitonclick()