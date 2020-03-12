#Exercises 3.4.4
#1st question
n=int(input("Give me a number!\n"))

if n>6:
    print("not a valid day number, try again!")
    n = int(input("Give me a number!\n"))
    print("%s is... " % n)
    if n==0:
        print("Sunday")
    elif n==1:
        print("Monday")
    elif n==2:
        print("Tuesday")
    elif n==3:
        print("Wednesday")
    elif n==4:
        print("Thursday")
    elif n==5:
        print("Friday")
    elif n==6:
        print("Saturday")

#2nd question
leave_day=int(input("Which day are you leaving?\n"))
number_days=int(input("How many days will you stay there?\n"))
return_day=(leave_day+number_days)%7
print("The return day is %s" % return_day)
if return_day == 0:
    print("Sunday")
elif return_day == 1:
    print("Monday")
elif return_day == 2:
    print("Tuesday")
elif return_day == 3:
    print("Wednesday")
elif return_day == 4:
    print("Thursday")
elif return_day == 5:
    print("Friday")
elif return_day == 6:
    print("Saturday")

#3rd question
# b>=a
# a<b
# a<18 or day != 3
# a<18 or day == 3

#4th question
#those statements evaluates the logical correctness of these expressions, producing True or False

#5th question
print((not (True and False)) or True)
#all are True except not (True and True) or False

#6th question
exam_mark=float(input("What is the exam mark?\n"))
print("The exam mark of %s corresponds to following grade:" %exam_mark)
if exam_mark<40:
    print("F3")
elif exam_mark>=40 and exam_mark<45:
    print("F2")
elif exam_mark>=45 and exam_mark<50:
    print("F1 Supp")
elif exam_mark>=50 and exam_mark<60:
    print("Third")
elif exam_mark>=60 and exam_mark<70:
    print("Second")
elif exam_mark>=70 and exam_mark<75:
    print("Upper Second")
elif exam_mark>=75:
    print("First")

#7th question
a=int(input("What's the length of the right side?\n"))
b=int(input("What's the length of the left side?\n"))

print((a**2+b**2)**0.5)

#8th question
def is_rightangled(a, b, c):
    return abs((a ** 2 + b ** 2) - (c ** 2)) < 0.001

# test cases and expected results
is_rightangled(1.5, 2.0, 2.5) #True
is_rightangled(4.0, 8.0, 16.0) #False
is_rightangled(4.1, 8.2, 9.1678787077) #True
is_rightangled(4.1, 8.2, 9.16787) #True
is_rightangled(4.1, 8.2, 9.168) #False
is_rightangled(0.5, 0.4, 0.64031) #True

#9th question
def is_rightangled(a, b, c):
    if a > b and a > c:
        return abs((b ** 2 + c ** 2) - (a ** 2)) < 0.001
    elif b > a and b > c:
        return abs((a ** 2 + c ** 2) - (b ** 2)) < 0.001
    else:
        return abs((a ** 2 + b ** 2) - (c ** 2)) < 0.001

#10th question
import math
a = math.sqrt(2.0)
print(a,a*a)
print(a*a==2.0)

#1st
for _ in range(1000):
    print("We like Python's turtles!")

#2nd
n=["January","February","March","April","May","June","July","August","September","October","November","December"]
for months in n:
    print("One of the months of the year is", months)

#3rd
import turtle
window = turtle.Screen()
tess = turtle.Turtle()
tess.left(3645)
window.mainloop()

#4th
numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]
for n in numbers:
    print(n)

for n in numbers:
    print(n,n**2)

total=0
for n in numbers:
    total=n+total
    print(total)

product=1
for n in numbers:
    product=n*product
print(product)

#5th
import turtle
screen = turtle.Screen()
aik=turtle.Turtle()

for _ in range(3):
    aik.forward(50)
    aik.left(120)

for _ in range(4):
    aik.forward(50)
    aik.left(90)

for _ in range(6):
    aik.forward(50)
    aik.left(60)

for _ in range(8):
    aik.forward(50)
    aik.left(45)

screen.exitonclick()

#6th
import turtle
screen = turtle.Screen()
aik=turtle.Turtle()
aik.shape("turtle")

angles=[160, -43, 270, -97, -43, 200, -940, 17,-86]

for _ in angles:
    aik.forward(100)
    aik.left(_)

screen.exitonclick()

#7th
import turtle
screen = turtle.Screen()
aik=turtle.Turtle()
aik.shape("turtle")
angles=[160, -43, 270, -97, -43, 200, -940, 17,-86]

for _ in angles:
    aik.forward(100)
    aik.left(_)

screen.exitonclick()

#8th
print(360/18)

#9th
import turtle
window = turtle.Screen()
tess = turtle.Turtle()
tess.right(90)
tess.left(3600)
tess.right(-90)
tess.speed(10)
tess.left(3600)
tess.speed(0)
tess.left(3645)
tess.forward(-100)

#10th
import turtle
window = turtle.Screen()
tess = turtle.Turtle()
tess.hideturtle()
tess.left(30)
tess.forward(100)
tess.right(30)
tess.backward(100)
tess.right(30)
tess.forward(100)
tess.left(150)
tess.forward(100)
tess.left(150)
tess.forward(100)

window.exitonclick()

#11th
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

#12th
import turtle
aik = turtle.Turtle()
print(type(aik))