import pygame
from color import *
from circle import *
from level import *

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

	level = Level(screen,size)

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouseX, mouseY = event.pos
				print mouseX, mouseY
				level.mouseEvent(mouseX, mouseY, totalFrames)
				#circle = Circle(size,mouseX,mouseY)
				#circle = Circle(size)

		screen.fill(color.LIGTGREY)

		level.update(FPS, totalFrames)

		pygame.display.flip()

		clock.tick(FPS)
		totalFrames += 1

if __name__ == "__main__":
	main()