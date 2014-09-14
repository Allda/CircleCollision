import pygame
from circle import *

class Level(object):
	WAITING = 1
	INGAME = 2
	LOSE = 15
	WIN = 16
	def __init__(self, screen, size, totalFrames):
		self.screen =screen
		self.size = size
		self.base = 10
		self.resetValues()
		self.level = 1
		self.generateCircles(totalFrames)


	def resetValues(self):
		self.circletCount = int(math.log(self.base,2)*10)
		self.require = int(self.circletCount*(0.1*math.log(self.base,2)))
		self.state = Level.WAITING
		self.collision = 0


	def mouseEvent(self,x,y, totalFrames):
		if(self.state == Level.WAITING):
			circle = Circle(self.size, x, y, totalFrames,Circle.INCREASE)
			self.state = Level.INGAME
		else:
			pass

	def draw(self,screen):
		for c in Circle.circleList:
			c.draw(screen)

	def update(self, FPS, totalFrames):
		for c in Circle.circleList:
			c.update(FPS, totalFrames)

		for c in Circle.circleList:
			if c.state == Circle.INCREASE or c.state == Circle.WAITING or c.state == Circle.DECREASE:
				self.collision += c.checkCollision()
		if self.require <= self.collision:
			return Level.WIN
		if (self.checkLose()):
			return Level.LOSE

	def checkLose(self):
		if self.state == Level.INGAME:
			for c in Circle.circleList:
				if c.state == Circle.INCREASE or c.state == Circle.WAITING or c.state == Circle.DECREASE:
					return False
			return True
		else:
			return False

	def generateCircles(self, totalFrames):
		for i in range(0,self.circletCount):
			circle = Circle(self.size,None,None, totalFrames)
			circle.draw(self.screen)

	def nextLevel(self, totalFrames):
		self.base *= 2
		self.resetValues()
		Circle.circleList[:] = []

		self.level += 1
		self.generateCircles(totalFrames)

	def restartLevel(self,totalFrames):
		self.state = Level.WAITING
		self.collision = 0
		Circle.circleList[:] = []
		self.generateCircles(totalFrames)
