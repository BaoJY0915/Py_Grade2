from turtle import *

def inputnum():
    x,y = eval(input('请输入：'))
    return x,y

def drawline():
##    hideturtle()
    x = -100
    y = -50
    pensize = 50
    for i in range(10):
        x += 50

        r,g,b = 0,abs(-x/280),1
        pencolor((r,g,b))
        penup()
        goto(x,y)
        pendown()
        forward(50)

setup(800,600,200,200)
##tracer(False)
speed(5)
##x,y = inputnum()
a = drawline()
done()
