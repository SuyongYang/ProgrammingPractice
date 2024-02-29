import turtle
t = turtle.Turtle()
t.shape("turtle")
n = int(input("what poligon do you want?"))
degree = 360 /n
t.up()
t.goto(0,0)
t.down()
for i in range(n):
    t.forward(30)
    t.left(degree)

turtle.done()
