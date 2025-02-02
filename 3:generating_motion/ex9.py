# USE THE CLOCK TO GET THE DELTA TIME
# USE THIS TO MAKE THE PLAYERS MOTION "FRAMERATE INDEPENDENT"

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
player_direction = pygame.math.Vector2(2, 1)


while running:
	clock.tick()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	display_surface.fill('#3a2e3f')
	display_surface.blit(player_surf, player_rect)
	player_rect.center += player_direction	
	pygame.display.update()
	
pygame.quit()