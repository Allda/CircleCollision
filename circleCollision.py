import pygame
from color import *
from circle import *

def main():
	color = Color()
	
	pygame.init()

	size = (800,600)
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption("Circle collision")

	clock = pygame.time.Clock()
	FPS = 60
	totalFrames = 0
	done = False

	circle = Circle(size)

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouseX, mouseY = event.pos
				circle = Circle(size,mouseX,mouseY)

		screen.fill(color.LIGTGREY)

		for c in Circle.circleList:
			c.draw(screen)

		pygame.display.flip()

		clock.tick(FPS)

if __name__ == "__main__":
	main()