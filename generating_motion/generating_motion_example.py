# GENERATING MOTION

# So far, we have been rendering our images outside of the programs loop
# This means all our images are completely static
# In this section, you are going to make the player image move around the screen

import pygame

# General Setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter") 
clock = pygame.time.Clock()
running = True

# Import image
player_surf = pygame.image.load('./images/player.png').convert_alpha()
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
player_direction = pygame.math.Vector2(1, 1)
speed = 400

while running:
	dt = clock.tick() / 1000
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	display_surface.fill('#3a2e3f')
	
	if (player_rect.right >= WINDOW_WIDTH or player_rect.left <= 0):
		player_direction.x *= -1
	if (player_rect.top <= 0 or player_rect.bottom >= WINDOW_HEIGHT):
		player_direction.y *= -1

	player_rect.center += player_direction * speed * dt
	display_surface.blit(player_surf, player_rect)
	pygame.display.update()
	
pygame.quit()