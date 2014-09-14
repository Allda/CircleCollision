import pygame
import random
from color import *

class Circle(object):
	INCREASE = 1
	DECREASE = 2
	NORMAL = 3

	circleList = []
	def __init__(self,size, x, y, totalFrames, state = NORMAL):
		#__init__(self, size)
		self.size = size
		if x == None:
			self.x = random.randint(0,size[0])
		else:
			self.x = x
		if y == None:
			self.y = random.randint(0,size[1])
		else:
			self.y = y
		self.radius = 10
		self.state = state
		Circle.circleList.append(self)
		self.color = Color.getRandomColor(None)
		self.increaseTime = 30
		self.normalTime = 1
		self.decreaseTime = 1
		self.framesEdge = totalFrames
		self.maxRadius = 40
		

	def update(self, FPS, totalFrames):
		if(self.state == Circle.INCREASE):
			if((totalFrames - self.framesEdge) % int(FPS/self.increaseTime) == 0):
				self.radius += 1
				if(self.radius == self.maxRadius):
					self.state = Circle.NORMAL

	def draw(self, screen):
		pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)