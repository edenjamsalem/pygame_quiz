# LOAD IN THE LASER IMAGE AND DRAW THE BOTTOM OF THE LASER AT THE TOP OF THE


import pygame

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter") 
running = True

display_surface.fill('#3a2e3f')

player_surf = pygame.image.load('./images/player.png').convert_alpha()
player_rect = player_surf.get_frect(topleft = (0, 0))
display_surface.blit(player_surf, player_rect)

pygame.display.update()

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

pygame.quit()