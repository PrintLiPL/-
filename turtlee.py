import turtle as t
import random
pen=t.Turtle()
t.shape("circle")#turtle arrow circle square trangle
t.pensize(3)
t.speed(10000000000000000000000000000000000000000000000)

t.pencolor("blue")
"""
for i in range(4):
    t.right(90)
    t.fd(100)
t.bk(80)
t.left(120)
t.fd(80)
t.goto(70,80)
t.home()
t.hideturtle()#t.ht()
t.st()
a=random.randint(0,10)
b=random.randint(0,10)
c=random.randint(0,10)
d=(a/10,b/10,c/10)
t.fillcolor(d)
t.begin_fill()
t.circle(100)
t.end_fill()"""
#五角星
"""t.fillcolor("red")
t.begin_fill()
for i in range(5):
    t.forward(100)
    t.right(180-180/5)
t.end_fill()
"""
#圆
"""color=["red","orange","blue","yellow","black"]
x,y=0,0
for i in range(3):
    t.pencolor(color[i])
    t.circle(100)
    t.penup()
    x+=150
    t.goto(x,y)
    t.pendown()
x=50
y=-100
for i in range(-1,-3,-1):
    t.penup()
    t.pencolor(color[i])
    t.goto(x,y)
    t.pendown()
    t.circle(100)
    x+=150
"""
'''
t.penup()
t.ht()
t.goto(50,50)
t.pendown()
t.pencolor()
t.pensize(5)
t.pencolor("white")
t.fillcolor("red")
t.begin_fill()
for i in range(6):
    t.forward(100)
    t.left(180-720/6)
t.end_fill()
'''
#内切六边形
'''
t.pencolor("black")
t.penup()
t.goto(-100,-100)
t.begin_fill()
t.circle(100,360,steps=6)
t.end_fill()
t.pendown()

t.done()
'''
#方法一
'''
import turtleer as tl
tl.nbx(6)
'''
#方法二