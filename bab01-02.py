import turtle

mypet = turtle.Turtle()
mypet.shape('turtle')
mypet.shapesize(3,3,3)


a = 100
b = 100
c = a+b
mypet.forward(c)

d = [100,50]
mypet.penup()
mypet.setpos(d)

turtle.done()


