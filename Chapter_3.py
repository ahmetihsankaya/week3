# creating figures with turtle

import turtle

screen = turtle.Screen()
screen.title("aik")
screen.bgcolor("gray")

aik = turtle.Turtle()

aik.color("Red")

# drawing a tetragon
aik.forward(50)
aik.left(90)
aik.forward(100)
aik.left(90)
aik.forward(50)
aik.left(90)
aik.forward(100)
aik.left(90)

# for & if statements
# start with specifying a list
turtles_names = ['Leonardo','Michelangelo','Donatello','Raphael']
for index in turtles_names:
    print(index)

x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# we can also use "for" to speed up turtles!
# here is a hexagon
for corner in range(6):
    print(corner)
    aik.color("Blue")
    aik.forward(50)
    aik.left(60)

# "for" & "if" together to create an equilateral triangle
for counter in range(20):
    if counter % 2 == 0:
        aik.forward(50)
    aik.left(60)
screen.exitonclick()

#a bit more complicated
for counter in range(50):
    if counter % 2 == 0:
        aik.forward(50)
    else:
        aik.backward(10)
    aik.left(61)

#stamps
import turtle
window = turtle.Screen()
window.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")

tess.penup() # This is new
size = 20
for _ in range(30):
    tess.stamp() # Leave an impression on the canvas
    size = size + 3 # Increase the size on every iteration
    tess.forward(size) # Move tess along
    tess.right(24) # ... and turn her

window.mainloop()

#incremental increase
numbers = [2, 2, 2, 2, 2]
running_total = 60
for number in numbers:
    running_total = running_total + number
    print(running_total)

