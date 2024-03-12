import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    random_color = (r, b, g)
    return random_color

t.bgcolor("pink")
t.pensize(1)
t.speed("fastest")

for _ in range(100):
#
#     for color in ("red","black","yellow","White","brown","green"):
#         t.color(color)
    t.circle(100)
    t.left(10)
    t.color(random_color())

screen = t.Screen()
screen.exitonclick()




