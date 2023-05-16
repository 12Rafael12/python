import turtle
a = turtle.Screen()
turtle.hideturtle()

turtle.begin_fill()
turtle.color("red")
for x in range(2):
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
turtle.end_fill()
turtle.right(90)
turtle.forward(70)
turtle.left(90)
turtle.forward(120)

turtle.begin_fill()
turtle.color("green","red")
turtle.pensize(5)
for i in range(5):
    turtle.forward(65)
    turtle.right(144)
turtle.end_fill()

turtle.mainloop()