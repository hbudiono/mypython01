import turtle
import random


mypet = turtle.Turtle()

mypet.pencolor("yellow")
mypet.shape('turtle')
mypet.shapesize(3,3,3)
mypet.speed(5)

while True :
  i =  random.randint(1,50)
  y =  random.randint(1,45)
  #mypet.penup()
  mypet.forward(i)
  mypet.right(y)
  

turtle.done()
