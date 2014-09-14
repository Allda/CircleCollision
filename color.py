
import random

class Color(object):
	BLACK    = (   0,   0,   0)
	WHITE    = ( 255, 255, 255)
	GREEN    = (   0, 255,   0)
	RED      = ( 255,   0,   0)
	GREY	 = (  50,  50,  50)
	LIGTGREY = (  80,  80,  80)

	@staticmethod
	def getRandomColor(self):
		#return (255,0,0)
		return (random.randint(0,255),random.randint(0,255),random.randint(0,255))