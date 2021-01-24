import turtle
turtle.pensize(3)
turtle.penup()
turtle.goto(-100,-50)
turtle.pendown()
turtle.begin_fill()
turtle.color('yellow',(0.75,0.75,0.75))
turtle.circle(40,steps = 6)
turtle.end_fill()


turtle.penup()
turtle.goto(0,-50)
turtle.pendown()
turtle.begin_fill()
turtle.color('yellow',(0.5,0.5,0.5))
turtle.circle(40,steps = 6)
turtle.end_fill()
