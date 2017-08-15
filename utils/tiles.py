import numpy as np
import scipy.misc as smp
from utils.colors import Colors

class Tiles:
	def __init__(self):
		self.colors = Colors()
		self.floor = self.create_floor_tile()

	
	def create_floor_tile(self):
		tile = np.zeros( (16,16,3), dtype=np.uint8 )
		for y in range(16):
			for x in range(16):
		return tile


	def create_tile(self, feature, filename):
		img = smp.toimage(feature)
		smp.imsave(filename, feature)
