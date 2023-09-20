import turtle

# Create a turtle object
star = turtle.Turtle()

# Define the length of each side of the star
side_length = 100

# Loop to draw the five sides of the star
for _ in range(5):
    star.forward(side_length)  # Move the turtle forward by the side length
    star.right(144)           # Turn the turtle 144 degrees to the right

# Close the turtle graphics window on click
turtle.exitonclick()
