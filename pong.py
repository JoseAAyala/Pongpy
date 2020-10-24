import pygame

pygame.init()
clock = pygame.time.Clock()

screen_width = 1080
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

ball = pygame.Rect(screen_width/2-11, screen_height/2-11, 22, 22)
player = pygame.Rect(screen_width-20, screen_height/2-60, 10, 120)
enemy = pygame.Rect(10, screen_height/2-60, 10, 120)


bgColor = (25,25,25)
objectColor = (115,115,115)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	screen.fill(bgColor)
	pygame.draw.rect(screen, objectColor, player)
	pygame.draw.rect(screen, objectColor, enemy)
	pygame.draw.ellipse(screen, objectColor, ball)
	pygame.draw.aaline(screen, objectColor, (screen_width/2,0), (screen_width/2,screen_height))

	pygame.display.flip()
	clock.tick(60)
