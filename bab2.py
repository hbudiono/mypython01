import turtle

budi = turtle.Turtle()
budi.shape('turtle')
budi.color('blue')
budi.shapesize(2,2,2)

wati = turtle.Turtle()
wati.shape('turtle')
wati.color('pink')
wati.shapesize(2,2,2)


a = 100
b = 2*a
#budi.penup()
#budi.goto(-100,-100)
#budi.pendown()
budi.forward(a)
wati.right(180)
wati.forward(b)


turtle.done()