# ADDING COLOUR TO OUR SCREEN

# If you run this program, you'll see that the screen is blank
# I want you to fill in this screen with a colour of your choice

# You will need to use:
# - the ".fill()" method for the display_surface
# - the "pygame.display.update()" method to update the screen with the change in colour


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


