from turtle import Turtle, Screen

tim = Turtle()

tim.shape('turtle')

# for _ in range (50):
#   tim.forward(10)
#   tim.penup()
#   tim.forward(10)
#   tim.pendown()

#TRIANGLE
for _ in range (3):
 tim.forward(100)
 tim.right(120)
 tim.color("lime green")

#SQUARE
for _ in range (4):
 tim.forward(100)
 tim.right(90)
 tim.color("blue")

#PENTAGONE
for _ in range (5):
 tim.forward(100)
 tim.right(72)
 tim.color("red")

#HEXAGONE
for _ in range (6):
 tim.forward(100)
 tim.right(60)
 tim.color("wheat")

#OCTAGON
for _ in range(8):
 tim.forward(100)
 tim.right(45)
 tim.color("black")

#NONAGON
for _ in range(9):
 tim.forward(100)
 tim.right(40)
 tim.color("brown")

#DECAGON
for _ in range(10):
 tim.forward(100)
 tim.right(36)
 tim.color("lime green")

screen = Screen()
screen.exitonclick()

