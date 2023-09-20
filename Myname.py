import turtle

# Create a turtle screen
window = turtle.Screen()
window.bgcolor("white")

# Create a turtle
pen = turtle.Turtle()
pen.speed(1)  # Set the drawing speed (1 is slowest)

# Function to draw a thick line

def draw_thick_line(x1, y1, x2, y2, width, color):
    pen.penup()
    pen.goto(x1, y1)
    pen.pendown()
    pen.pensize(width)
    pen.pencolor(color)
    pen.goto(x2, y2)
