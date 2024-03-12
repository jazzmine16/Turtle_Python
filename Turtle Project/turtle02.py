import turtle as t
import random

timm = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


directions = [0,90,180,270]
timm.pensize(15)
timm.speed("fastest")

for _ in range(100):
     timm.color(random_color())
     timm.forward(30)
     timm.setheading(random.choice(directions))






screen = t.Screen()
screen.exitonclick()







