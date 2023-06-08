import turtle

from itertools import cycle
colors=cycle(['red','orange','yellow','green','blue','purple'])

def drew_circle(size):
     turtle.pencolor(next(colors))
     turtle.circle(size)
     drew_circle(size+5)

turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(10)
drew_circle(30)
