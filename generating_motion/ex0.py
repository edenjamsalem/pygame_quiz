# REARRANGE THIS CODE SO THAT THE PLAYER IMAGE IS DRAW INSIDE OF THE PROGRAM LOOP
# THE PLAYER IMAGE SHOULD MOVE TO THE RIGHT OF THE SCREEN

# HINT: you dont need to add or del anything, just change the order

import pygame

# General Setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter") 
running = True

# Colour Screen
display_surface.fill('#3a2e3f')

# Import image
player_surf = pygame.image.load('./images/player.png').convert_alpha()
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
player_rect.x += 1

# Draw image
display_surface.blit(player_surf, player_rect)

# Update screen
pygame.display.update()

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

pygame.quit()