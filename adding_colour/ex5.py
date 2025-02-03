# FLASHING SCREEN

# Make the screen flash between two colours of your choice
# e.g. red then blue then red then blue ... etc

# HINT: Use an if/else statement

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

	# Colour screen here:



pygame.quit()