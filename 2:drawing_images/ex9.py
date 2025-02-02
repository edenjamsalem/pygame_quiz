# USE A LIST STORE 20 RANDOM POSITIONS ON THE SCREEN
# THEN DRAW A STAR AT EACH OF THESE POSITIONS

import pygame

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter") 
running = True

display_surface.fill('#3a2e3f')

star_surf = pygame.image.load('./images/star').convert_alpha()
star_positions = []
...

pygame.display.update()

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

pygame.quit()


