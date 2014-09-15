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
	def __init__(self,size, x, y, totalFrames, exp = 0, state = NORMAL):
		#__init__(self, size)
		self.size = size
		self.radius = 10
		self.exp = exp
		if x == None:
			self.x = random.randint(self.radius,size[0]-self.radius)
		else:
			self.x = x
		if y == None:
			self.y = random.randint(self.radius,size[1]-self.radius)
		else:
			self.y = y
		
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
			if(self.x-self.radius < 0 or self.x+self.radius > self.size[0]):
				self.speedx *= -1
			if(self.y-self.radius < 0 or self.y+self.radius > self.size[1]):
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
		ck = (127, 33, 33)
		size = 20
		s = pygame.Surface((self.maxRadius*2,self.radius*2))

		# first, "erase" the surface by filling it with a color and
		# setting this color as colorkey, so the surface is empty
		s.fill(ck)
		s.set_colorkey(ck)

		pygame.draw.circle(s, self.color, (self.radius,self.radius), self.radius)

		# after drawing the circle, we can set the 
		# alpha value (transparency) of the surface
		s.set_alpha(200)

		screen.blit(s, (self.x-self.radius, self.y-self.radius))
		'''s = pygame.Surface((self.radius*2-1, self.radius*2+1))
		s.fill((127,33,33))
		s.set_colorkey((127,33,33))
		pygame.draw.circle(s,self.color,(self.x,self.y),self.radius,2)
		#s.set_alpha(75)
		screen.blit(s,(self.x-self.radius,self.y-self.radius))
		pygame.display.flip()
		#pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)'''


