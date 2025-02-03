# DRAWING IMAGES

# In this section you'll find an 'images' folder containing the images for our game
# Below is an example demonstrating how we can load and draw these into our screen


# ------------------------------------------------------------------------------------


import pygame
from random import randint

# General Setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter") 
running = True

# Colour Screen
display_surface.fill('#3a2e3f')

# Import images
player_surf = pygame.image.load('./images/player.png').convert_alpha()
meteor_surf = pygame.image.load('./images/meteor.png').convert_alpha()
laser_surf = pygame.image.load('./images/laser.png').convert_alpha()
star_surf = pygame.image.load('./images/star.png').convert_alpha()

# Create rects for each images position on the screen
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
meteor_rect = meteor_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 4))
laser_rect = laser_surf.get_frect(midbottom = player_rect.midtop)
star_positions = []
for i in range(20):
	star_positions.append(star_surf.get_frect(center = (randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT))))

# Draw images
display_surface.blit(player_surf, player_rect)
display_surface.blit(meteor_surf, meteor_rect)
display_surface.blit(laser_surf, laser_rect)
for position in star_positions:
	display_surface.blit(star_surf, position)

# Update screen
pygame.display.update()

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

pygame.quit()


# ------------------------------------------------------------------------------------

# Just as in the first section, each exercise will have some code missing
# However, this time I will ask you to change/recreate a specific aspect of it

# There are 10 exercises, worth 1 point each and which get progressively harder.
# You are free to try and run the code to check for errors or missing functionality
# At the end, there are 5 points bonus points avaiable to win if you can recreate 
# this example from scratch

# As always, good explanations to my questions wins you bonus points!

# GOOD LUCK!