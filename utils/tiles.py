import numpy as np
import scipy.misc as smp
from utils.colors import Colors
from utils.matrices import Matrices


class Tiles:
	def __init__(self):
		self.colors = Colors()
		self.matrices = Matrices()
		self.floor = self.create_tile_matrix(self.matrices.floor)

	
	def create_tile_matrix(self, matrix):
		tile = np.zeros( (16,16,3), dtype=np.uint8 )
		for y in range(16):
			for x in range(16):
				if matrix[y][x] == 0:
					tile[x, y] = self.colors.dark
				elif matrix[y][x] == 1:
					tile[x, y] = self.colors.mid
				elif matrix[y][x] == 2:
					tile[x, y] = self.colors.light
				else:
					matrix[x, y] = self.colors.white
		return tile


	def draw_tile(self, feature, filename):
		img = smp.toimage(feature)
		smp.imsave(filename, feature)
