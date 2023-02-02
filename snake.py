
import turtle

turtle.speed(0)
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.pensize(5)
for i in range(100):
    turtle.forward(i * 5)
    turtle.right(90)
    turtle.forward(i * 5)
    turtle.right(90)
