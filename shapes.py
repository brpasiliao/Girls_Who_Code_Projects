from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
x_pos = 0
y_pos = 0
t.setposition(x_pos, y_pos)

### Write your code below:

begin_fill()

fillcolor("blue")

for each in range(3):
    forward(100)
    right(120)

end_fill()




# Close window on click.
exitonclick()