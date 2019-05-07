import math
import turtle

# Define window size as constants
window = turtle.Screen()  # create a window for the turtle to draw on
window.title("Turtle Demo")  # the title to show at the top of the window
WINDOW_WIDTH = 800  # size constants for easy changing
WINDOW_HEIGHT = 500
window.setup(WINDOW_WIDTH, WINDOW_HEIGHT)  # specify window size (width, height)
window.setworldcoordinates(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)  # coordinate system: origin at lower-left

# Create the turtle
my_turtle = turtle.Turtle()
my_turtle.speed("normal")  # how fast the turtle should move

# # Move the turtle to draw
# my_turtle.penup()       # do not draw while moving
# my_turtle.goto(30, 60)  # walk to coordinates
# my_turtle.pendown()     # start drawing again
# my_turtle.forward(80)   # move forward
# my_turtle.left(60)      # turn left
# my_turtle.forward(120)  # move forward
# my_turtle.right(120)    # turn left
# my_turtle.forward(120)  # move forward

def draw_axes(turtle, y_max, x_max, offset = 10):
    '''
    Draw x and y axes in one pass
    Offset from the 0,0 corner of the window by fixed amount
    '''
    turtle.penup()
    turtle.goto(offset, y_max - offset)          # [TODO] calculate tick marks using y-max from file
    turtle.pendown()
    turtle.goto(offset, offset)
    turtle.goto(x_max - offset, offset)

# pass global turtle and window dimensions
draw_axes(my_turtle, WINDOW_HEIGHT, WINDOW_WIDTH, offset = 10)
# √


def draw_lines(turtle, y_max):
    '''
    Concept for drawing tick marks, final version will likely have more arguments
    This simple version is hard-coded to jump up by 10 each time.
    A good version would:
    - start at 0 on the x axis
    - start at a point on the y axis derived from the maximum height and the tick number (1...n)
        - perhaps 'tick_num' is an input?
        - y_max would not be necessary, start at 0 and use the global WINDOW_HEIGHT to determine the limit
    - also write a tick label/value
        - perhaps this is also an input?
    '''
    turtle.penup()
    turtle.goto(0, 20)
    while turtle.ycor() < y_max:                # [TODO] switch to for loop; derive upper limit from window height (1/10 of height per tick mark)
        turtle.pendown()                        # e.g. `for i in range(n): ...`   # draw n ticks
        # turtle.write(turtle.ycor(), font = ('Arial', 8, 'normal'))     # write the current position with line
        turtle.forward(15)
        turtle.penup()
        turtle.goto(0, turtle.ycor() + 10)     # increment y-position, x never needs to change

draw_lines(my_turtle, WINDOW_HEIGHT)

def draw_some_text(turtle, x, y, text, color):
    '''
    Have a turtle draw some text at x/y, with a given color
    To label axes for your homework, one solution is to simply call turtle.write(...) within your draw_y_tickmark function so that
    each time your function draws a tickmark it also writes a label in the same pass.
    (hint: that means that the tickmark label needs to be an argument to the draw_y_tickmark() function; check the turtle.write(...) in draw_lines() above)
    '''
    turtle.penup()
    turtle.goto(x, y)
    turtle.pencolor(color)
    turtle.write(text, font=('Arial', 12, 'bold'))

# In this example I'll pass the global window variables(/2) to write in the middle
draw_some_text(my_turtle, WINDOW_WIDTH/2, WINDOW_HEIGHT/2, "Hello", "violet")

def draw_bar(turtle, x0, w, h, color = "violet"):
    '''
    Outline a function for drawing a rectangle (bar)
    A rectangle needs a starting position and has 2 dimensions, length & width
    Your function will need to label the bars as well and change color for each bar
    '''
    turtle.penup()
    turtle.goto(x0, 10)     # This turtle starts at x0 and y = 10 because I used a slight offset on my lines, y = 10 is zero on my axis
                            # The combination of penup() + goto() may be simple for your function, depending on how you implement your program
                            # You may wish to use the turtle's heading and forward command
    # draw bar
    turtle.fillcolor(color)
    turtle.width(x0+w)
    turtle.pendown()
    # turtle.begin_fill()   # Using fill is probably a better dynamic way to fill-in a shape b/c this will just draw a smear with rounded ends
    turtle.setheading(90)
    turtle.forward(h)       # This is not necessarily the best way to draw a rectangle!
    # turtle.end_fill()
    turtle.penup()

    # Using fill, skeleton:
    # set heading to 0
    # go forward -> left -> forward -> etc. to draw a rectangle using height+width
    # end fill
    # lift up pen

draw_bar(my_turtle, 20, 20, 100)

# Make the turtle graphics appear and run, waiting for the user to close the screen
# This MUST be the last statement executed in the script
window.mainloop()

