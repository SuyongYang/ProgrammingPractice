##Many Geometric boxes

import turtle
colors = ["red","purple","blue","green","yellow","orange"]
t=turtle.Turtle()

turtle.bgcolor("gray")
t.speed(840)
t.width(3)
length =10

while length <8000:
    t.pencolor(colors[length%6])
    t.forward(length*.5)

    t.right(89)
    length +=5

turtle.done()
