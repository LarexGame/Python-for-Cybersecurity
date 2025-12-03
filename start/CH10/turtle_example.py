import turtle
import random

def draw_circle(radius):
    t.circle(radius)
def draw_multiple_circles(number):
    colors = ["red", "blue", "green", "orange"]
    for i in range(number):
        # color = random.sample(colors, 1)
        t.pencolor(colors[i % 4])
        draw_circle(i * 10)
def draw_flower():
    for i in range(6):
        draw_multiple_circles(10)
        t.right(60)
t = turtle.Turtle()
draw_flower()
