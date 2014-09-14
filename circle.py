import pygame
import random
from color import *

class Circle(object):
	GROWING = 1
	STARTING = 2

	circleList = []
	def __init__(self,size, x, y,  state = GROWING):
		__init__(self, size, state)
		self.x = x
		self.y = y

	def __init__(self,size, state = GROWING):
		self.size = size
		self.x = random.randint(0,size[0])
		self.y = random.randint(0,size[1])
		self.radius = 10
		self.state = state
		Circle.circleList.append(self)
		self.color = Color.getRandomColor(None)

	def update(self):
		pass

	def draw(self, screen):
		pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)