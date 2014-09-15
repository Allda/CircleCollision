import pygame

class Menu(object):
	VERTICAL = 1
	NONE = -1
	def __init__(self, size, options, font, fontSize, colors, topMargin, style = VERTICAL):
		self.options = options
		self.topMargin = topMargin
		self.count = len(options)
		self.bg = colors[0]
		self.fontColor = colors[1]
		self.activeColor = colors[2]
		self.x = 100
		self.y = 30
		self.size = size
		self.selected = options.keys()[0]
		self.fontSize = fontSize
		self.font = pygame.font.Font(font,fontSize)

	def draw(self, screen):
		offset = 0
		for key,val in self.options.items():
			if key == self.selected:
				text = self.font.render(val,1,self.activeColor)
			else:
				text = self.font.render(val,1,self.fontColor)

			textPos = text.get_rect()
			textPos.centerx = int(self.size[0]/2)
			textPos.centery = self.topMargin+(offset*(self.fontSize+30))
			offset += 1
			screen.blit(text,textPos)


	def key(self, key):
		if(key == pygame.K_DOWN):
			self.selected = (self.selected + 1) % self.count
			return None
		if(key == pygame.K_UP):
			self.selected = (self.selected - 1 )
			if self.selected < 0:
				self.selected = self.count -1
			return None
		if(key == pygame.K_SPACE):
			return self.selected