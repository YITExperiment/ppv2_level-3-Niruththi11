import turtle

from itertools import cycle
colors =cycle(['red','orange','yellow','green','blue','purple'])

def drew_circle(size,angle,shift):
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
    draw_circle(size+5, angle+1,shift+1)

turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(7)
drew_circle(30,0,1)
