# HERE WE HAVE THE GENERAL SETUP FOR RUNNING OUR GAME

# It creates a window, sets a caption and runs a continuous loop for our program
# So far there is just one event inside the loop to listen for the 'X' button being pressed
# and then exit the program


# ------------------------------------------------------------------------------------


import pygame

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter") 
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

pygame.quit()


# ------------------------------------------------------------------------------------



# Each exercise in this section has a copy of this code with something missing
# Before each exercise you will have 1 minute to read this file and remember it
# Then you will need to fill in the missing line(s) of code by yourself

# There are 10 exercises, worth 1 point each and which get progressively harder.
# You are free to try and run the code to check for errors or missing functionality
# At the end, there are 5 points bonus points avaiable to win if you can recreate 
# the whole document from scratch

# As always, good explanations to my questions wins you bonus points!

# GOOD LUCK!