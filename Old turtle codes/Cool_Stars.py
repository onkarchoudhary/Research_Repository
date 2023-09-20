import turtle

# Create a turtle screen
window = turtle.Screen()
window.bgcolor("white")

# Create a turtle
pen = turtle.Turtle()
pen.speed(1)  # Set the drawing speed (1 is slowest)

# Set the turtle shape to "turtle"
# You can use "classic" for the classic turtle shape
pen.shape("turtle")

# Function to draw a star
def draw_star(size):
    for _ in range(5):
        pen.forward(size)
        pen.right(144)

# Function to draw the central star with surrounding stars


def draw_stars():
    central_star_size = 100
    surrounding_star_size = 30

    # Draw the central star
    pen.color("red")
    draw_star(central_star_size)

    # Draw surrounding stars
    for _ in range(5):
        pen.penup()
        pen.forward(central_star_size + 20)  # Move to the next position
        pen.pendown()
        pen.color("blue")
        draw_star(surrounding_star_size)
        pen.penup()
        pen.backward(central_star_size + 20)  # Return to the center
        pen.right(72)  # Rotate for the next star 


# Position the turtle and draw the stars
pen.penup()
pen.goto(0, -50)  # Position the turtle
pen.pendown()
draw_stars()

# Close the turtle graphics window on click
window.exitonclick()
