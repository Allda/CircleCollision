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

	myfont = pygame.font.Font("font/LEGO_BRIX.ttf",30)
	myBigfont = pygame.font.Font("font/LEGO_BRIX.ttf",60)

	level = Level(screen,size, totalFrames)

	userAction = False

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if userAction:
					if rv == Level.WIN:
						level.nextLevel(totalFrames)
						print "Next Level"
					elif rv == Level.LOSE:
						level.restartLevel(totalFrames)
						print "Retry"
					userAction = False
				else:
					mouseX, mouseY = event.pos
					print mouseX, mouseY
					level.mouseEvent(mouseX, mouseY, totalFrames)
					#circle = Circle(size,mouseX,mouseY)
					#circle = Circle(size)

		screen.fill(color.LIGTGREY)
		if not userAction:
			rv = level.update(FPS, totalFrames)
			if(rv == Level.LOSE):
				print "You Lose game"
				userAction = True
		collisonCount = myfont.render("Score: " + str(level.collision) +"/" +str(level.require),1,color.WHITE)
		screen.blit(collisonCount, (30,50))

		level.draw(screen)

		if(rv == Level.WIN):
			userAction = True
			winStr = myBigfont.render("You WIN",1,color.RED)
			screen.blit(winStr, (300,250))
		pygame.display.flip()

		clock.tick(FPS)
		totalFrames += 1

if __name__ == "__main__":
	main()