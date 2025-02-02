import pygame

# general setup
pygame.init()


pygame.display.set_caption("Space Shooter") 
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

pygame.quit()