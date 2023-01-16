import time
from turtle import *

t = Turtle()
bgcolor("black")
t.pencolor("purple")
t.speed(0)
for i in range(320):
    t.circle(190-i, 90)
    t.left(90)
    t.circle(190-i, 90)
    t.left(18)
    if i > 190:
        t.pensize(3)
        
pen = Turtle()
pen.color('red')
bgcolor('black')

def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)
        
def draw_heart():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()

font = ("Montserrat", 16, "bold")


def draw_text():
    pen.up()
    pen.setpos(-90, 90)
    pen.down()
    pen.color('white')
    pen.write("С днем рождения!", font=font)
    pen.up()
    pen.setpos(-70, 70)
    pen.down()
    time.sleep(3)
    pen.write("Мама", font=font)
    
draw_heart()
draw_text()
pen.ht()
    
mainloop()