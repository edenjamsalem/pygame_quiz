# USING PYGAME'S RGB HEXADECIMAL

# Using the RGB Hexadecimal format, fill the screen with a RED, then a GREEN then a BLUE colour
# Run the code to see if it worked

import pygame

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter") 
running = True

# Colour screen here:



while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

pygame.quit()