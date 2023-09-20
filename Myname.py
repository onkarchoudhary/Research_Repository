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

# Function to draw the letter 'O'
def draw_O():
    draw_thick_line(0, -100, 0, 0, 10, "blue")
    draw_thick_line(0, 0, 50, 0, 10, "blue")
    draw_thick_line(0, -100, 50, -100, 10, "blue")
    draw_thick_line(50, 0, 50, -100, 10, "blue")

# Function to draw the letter 'N'
def draw_N():
    draw_thick_line(100, 0, 100, -100, 10, "red")
    draw_thick_line(100, 0, 150, -100, 10, "red")
    draw_thick_line(150, 0, 150, -100, 10, "red")

# Function to draw the letter 'K'
def draw_K():
    draw_thick_line(200, 0, 200, -100, 10, "green")
    draw_thick_line(200, -50, 250, 0, 10, "green")
    draw_thick_line(200, -50, 250, -100, 10, "green")
