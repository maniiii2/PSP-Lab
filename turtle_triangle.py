#triangle with turtle
import turtle
triangle= turtle.Turtle()
triangle.color("pink")

line = 50
angle = 120
for _ in range(3):
    triangle.backward(line)
    triangle.right(angle)
