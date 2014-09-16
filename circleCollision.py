import pygame
import sys
from color import *
from circle import *
from level import *
from menu import *

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

	options = {
		0: "New Game",
		1: "About",
		2: "Exit"
	}
	rv = menuScreen(size, screen, options, 100, clock)
	if rv == 2:
		sys.exit()
	if rv == 1:
		#TODO about screen
		pass
	userAction = False

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if userAction:
					if rv == Level.WIN:
						level.nextLevel(totalFrames)
					elif rv == Level.LOSE:
						level.restartLevel(totalFrames)
					userAction = False
				else:
					mouseX, mouseY = event.pos
					level.mouseEvent(mouseX, mouseY, totalFrames)
					#circle = Circle(size,mouseX,mouseY)
					#circle = Circle(size)

		screen.fill(color.LIGTGREY)
		if not userAction:
			rv = level.update(FPS, totalFrames)
			if(rv == Level.LOSE):
				userAction = True
				options = {
					0: "Retry",
					1: "Exit"
				}
				loseStr = myBigfont.render("You Lose ",1,color.RED)
				rv = menuScreen(size, screen, options, 200,clock, loseStr)
				if rv == 1:
					sys.exit()
				if rv == 0:
					level.restartLevel(totalFrames)
					userAction = False
		collisonCount = myfont.render("Score: " + str(level.collision) +"/" +str(level.require),1,color.WHITE)
		points = myfont.render("Points: " + str(level.score),1,color.WHITE)
		screen.blit(collisonCount, (30,30))
		screen.blit(points,(30,70))

		level.draw(screen)

		if(rv == Level.WIN):
			userAction = True
			winStr = myBigfont.render("You WIN",1,color.RED)
			options = {
				0: "Next level",
				1: "Restart level",
				2: "Exit"
			}
			rv = menuScreen(size, screen, options, 200,clock, winStr)
			
			if rv == 2:
				sys.exit()
			if rv == 1:
				level.restartLevel(totalFrames)
				userAction = False
			if rv == 0:
				level.nextLevel(totalFrames)
				userAction = False
			screen.blit(winStr, (300,250))

		pygame.display.flip()

		clock.tick(FPS)
		totalFrames += 1

def menuScreen(size,screen, options, topMargin, clock, otherText = None):
	
	menu = Menu(size,options,"font/LEGO_BRIX.ttf",50,(Color.BLACK,Color.GREY, Color.GREEN), topMargin)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				#keys = pygame.key.get_pressed()  #checking pressed keys
				rv = menu.key(event.key)
				if rv != None:
					return rv
			elif event.type == pygame.MOUSEBUTTONDOWN:
				rv = menu.mousePress()
				if rv != None:
					return rv
		menu.mousePos(pygame.mouse.get_pos())

		screen.fill(Color.LIGTGREY)
		if (otherText != None):
			otherTextPos = otherText.get_rect()
			otherTextPos.centerx = int(size[0]/2)
			otherTextPos.centery = 50
			screen.blit(otherText,otherTextPos)
		menu.draw(screen)
		pygame.display.flip()
		clock.tick(30)

if __name__ == "__main__":
	main()