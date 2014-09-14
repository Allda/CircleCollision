import pygame
from circle import *

class Level(object):
	WAITING = 1
	INGAME = 2
	def __init__(self, screen, size):
		self.screen =screen
		self.size = size
		self.startCount = 3
		self.require = 1
		self.state = Level.WAITING

	def mouseEvent(self,x,y, totalFrames):
		if(self.state == Level.WAITING):
			circle = Circle(self.size, x, y, totalFrames,Circle.INCREASE)
			self.state = Level.INGAME
		else:
			pass

	def update(self, FPS, totalFrames):
		for c in Circle.circleList:
			c.update(FPS, totalFrames)
			c.draw(self.screen)
