from turtle import *
import colorsys as cs

tracer(50)
bgcolor("black")
pensize(2)
h = 0.3

for i in range(260):
    c = cs.hsv_to_rgb(h, 1, 1)
    h += 0.006
    color(c)
    goto(0,0)
    circle(i, 60)
    lt(60)
    circle(260-i, -60)
    lt(60)
done()
