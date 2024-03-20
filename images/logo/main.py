# Comments come after a #. Bring in all the
# turtle graphics functions.

import turtle

"""
BLOCK COMMENT (when you want to not use multiple
lines
put between sets of triple quotes.
Here is a list of useful turtle graphics
instructions.
They create marks on the screen
https://realpython.com/courses/python-turtlebeginners/
# You can also type things like the code below
into a command-line python interpreter (if you
want to)
# Make a red turtle/cursor with a green outline
>>> import turtle
>>> turtle.color('red', 'green')
>>> forward(200)
4
>>> right(90) # 90 degree turn
>>> forward(200) # Move 200 units forward
>>> right(90)
>>> forward(200)
>>> right(90)
>>> forward(200)
>>> begin_fill()
>>> circle(10)
>>> circle(200)
>>> dot(20)
>>> stamp()
10
>>> forward(20)
"""
# Set up the turtle graphics
s = turtle.getscreen()
# Get the "turtle" or cursor to be used.
# you can then type t.<instruction> to do
#various actions.

t = turtle.Turtle()

# Move the cursor to a specific direction and
#position (up and at position (-100,-100) )
# The cursor has a green outline and red inside
#so it makes green lines and fills things red.

t.color("green", "red")

# Needed to keep the window open.  Add all your
#code BEFORE the next line.

t.goto(-150, -150)

t.right(90)


s.mainloop()