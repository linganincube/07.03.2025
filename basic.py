from turtle import *

speed(0)
bgcolor("purple")

for i in range(190):
    color("black")
    circle(190-i, 90)
    left(90)
    circle(190-i, 90)
    left(18)
done()