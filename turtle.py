from turtle import *
import random
from multiprocessing import Pool
pool = Pool()

##colors = ['tan', 'tan4', 'tomato3', 'wheat', 'plum']
##for sh in ["arrow", "turtle", "circle", "square", "triangle", "classic"]:
##    shape(sh)
##    color(random.choice(colors))
##    forward(150)
##    right(90)
##    forward(50)
##    right(45)
##    backward(25)

extra_colors = ["yellow","gold","orange","red","maroon","violet","magenta","purple","navy","blue","skyblue","cyan","turquoise","lightgreen","green","darkgreen","chocolate","brown","black","gray","white"]

def walk_and_draw(t:Turtle):
    # t.color('tan')
    # t.shape('turtle')
    t.speed(2)
    t.pensize(4)
    for c in extra_colors:
        t.color(c)
        t.write(c)
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        t.goto(x,y)
        # clone.goto(-x, -y)
        t.dot()
        # clone.dot()
    
# walk_and_draw(Turtle())

pool.apply_async(walk_and_draw(Turtle()))
pool.apply_async(walk_and_draw(Turtle()))