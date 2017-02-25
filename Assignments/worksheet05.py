# Lab 5

# 1
# Difference number one: Origin is the upper left corner of the canvas.
# Difference number two: Y is reversed, so the further down the Y axis, the higher Y is.

# 2 - isn't it three?
# import pygame
# pygame.init()
# size(x,y)

# 3
# Each element of the RGB triad is a number ranging from 0 to 255.
# Zero means there is none of the color, and 255 displays as much of the color as possible.
# If all three colors are (225, 255, 255), the color appears white.

# 4
# The color-names are variables and are not expected to change, which makes them a constant.
# Variables that are constants are being named with all upper-case letters.
# If the color is expected to change, it would be in lower case.

# 5
# The pygame.display.set_mode() opens the window to display the drawings. It can also create games that runs in
# a full-screen mode. This removes the start menu, title bars, and gives the game control of everything
# on the screen.                                                                                                                                                                                                                                                                                                                                                                               'But if you want to find out more about full-screen games, check out the documentation on pygame's display command.

# 6
# This 'for event in pygame.event.get()' is a “event processing” code that handles all the keystrokes,
# mouse button clicks, and several other types of events, that the user does.
# The events all go together in a list and then the program uses a for loop
# to loop through each event.

# 7
#  The pygame.time.Clock is used to manage how fast the screen updates.

# 8
# For this line: pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
# Screen: Draws on screen.
# [0, 0]: The line is drawn from this point.
# [100, 100]: The line is drawn to this point.
# 5: The line is 5 pixels wide.

# 9
# Using a loop.

# 10
# There will not be a border around the rectangle, if the width is 0 pixels.
# Instead it will be filled in with the specified color.

# 11
# x, y of the origin coordinate = 20, 20
# The origin coordinate is specifying the upper left of a rectangle that contains the ellipse.
# The length and the width of the ellipse = 250, 100.

# 12
# The start and end angles for the arc.

# 13
# 1.) The program creates a variable that holds information about the font to be used. What typeface and how big.
# 2.) The program creates an image of the text.
# 3.) The program tells where this image of the text should be on the screen.

# 14
# Because the first line states the selected font, size, bold and italics, and should only run once.

# 15
# It is the coordinates for the corners of the polygon, to draw a line between.

# 16
# It flips the display after drawing. This waits to display the screen until the program has finished drawing.
# The command “flips” the graphics to the screen. Excluding this command will mean the program just shows a
# blank screen. Any drawing code after this flip will not be displayed.

# 17
# It is the proper shutdown of a Pygame program
# By clicking the “close” button of a window while running a Pygame program in IDLE will cause the program to crash.
# Even though the loop has exited, the program hasn't told the computer to close the window.
# By calling the command, the program will close any open windows and exit as desired.

# 18
# pygame.draw.circle(screen, BLUE, [300, 50], 20, 0)

