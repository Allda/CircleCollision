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
		self.font = pygame.font.Font("font/LEGO_BRIX.ttf",15)
		self.score = 0
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
		scoreAll = 0
		for c in Circle.circleList:
			if c.state == Circle.NORMAL:
				dx = abs(self.x-c.x)
				dy = abs(self.y-c.y)
				if (math.sqrt(dx*dx+dy*dy) < (self.radius + c.radius)):
					c.state = Circle.INCREASE
					c.exp = self.exp+1
					c.score = int(math.pow(2,self.exp))
					scoreAll =+ c.score
					count += 1
		return (count,scoreAll)



	def draw(self, screen):
		ck = (127, 33, 33)
		s = pygame.Surface((self.maxRadius*2,self.radius*2))
		s.fill(ck)
		s.set_colorkey(ck)

		pygame.draw.circle(s, self.color, (self.radius,self.radius), self.radius)

		s.set_alpha(200)
		screen.blit(s, (self.x-self.radius, self.y-self.radius))
		if self.state == Circle.WAITING:

			text = self.font.render("+"+str(self.score),1,Color.WHITE)

			textPos = text.get_rect()
			textPos.centerx = self.x
			textPos.centery = self.y
			screen.blit(text,textPos)



