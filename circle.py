import pygame
import random
import math
from color import *

class Circle(object):
	INCREASE = 1
	DECREASE = 2
	NORMAL = 3
	WAITING = 4

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
		self.normalTime = 0.7
		self.decreaseTime = 30
		self.framesEdge = totalFrames
		self.maxRadius = 40
		self.speedx = random.randint(1,2) * random.choice([-1,1])
		self.speedy = random.randint(1,2) * random.choice([-1,1])
		#self.speedx = 0
	def getCenterCoord(self):
		return (self.x + self.radius, self.y + self.radius)

	def update(self, FPS, totalFrames):

		if(self.state == Circle.NORMAL):
			self.x += self.speedx
			self.y += self.speedy
			if(self.x < 0 or self.x > self.size[0]):
				self.speedx *= -1
			if(self.y < 0 or self.y > self.size[1]):
				self.speedy *= -1
		if(self.state == Circle.INCREASE):
			if((totalFrames - self.framesEdge) % int(FPS/self.increaseTime) == 0):
				self.radius += 1
				if(self.radius == self.maxRadius):
					self.state = Circle.WAITING
					self.framesEdge = totalFrames
		elif(self.state ==  Circle.WAITING):
			if((totalFrames - self.framesEdge) % int(FPS/self.normalTime) == 0):
				self.framesEdge = totalFrames
				self.state = Circle.DECREASE
		elif(self.state == Circle.DECREASE):
			if((totalFrames - self.framesEdge) % int(FPS/self.decreaseTime) == 0):
				self.radius -= 1
				if(self.radius == 0):
					Circle.circleList.remove(self)


	def checkCollision(self):
		count = 0
		for c in Circle.circleList:
			if c.state == Circle.NORMAL:
				dx = abs(self.x-c.x)
				dy = abs(self.y-c.y)
				if (math.sqrt(dx*dx+dy*dy) < (self.radius + c.radius)):
					c.state = Circle.INCREASE
					count += 1
		return count



	def draw(self, screen):
		pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)


