# REWRITE THE STAR POSITIONS LIST USING A LIST COMPREHENSION
# YOU CAN USE GOOGLE IF YOU CAN'T REMEMBER WHAT THIS IS

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
for i in range(20):
	star_positions.append(star_surf.get_frect(center = (randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT))))
for position in star_positions:
	display_surface.blit(star_surf, position)

pygame.display.update()

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

pygame.quit()


