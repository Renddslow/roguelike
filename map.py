from random import *
from math import *


class Dungeon:
	#  ----------------------
	# | KEY:                 |
	# | 0 = Stone            |
	# | 1 = Unlit floor      |
	# | 2 = Lit Empty Floor  |
	# | 3 = Wall             |
	# | 4 = Item             |
	# | 5 = Corridor Floor   |
	# | 6 = Door             |
	#  ----------------------

	def __init__(self, x, y):
		self.world_width = x
		self.world_height = y
		self.matrix = self.generate_map()


	def generate_map(self):
		matrix = []
		for y in range(self.world_height):
			matrix.append([])
			for x in range(self.world_width):
				matrix[y].append(0)
		return matrix


	def create_room(self):
		room_width = randrange(3, ceil(self.world_width * .1))
		room_height = randrange(3, ceil(self.world_height * .1))
		return room_width, room_height


	def draw_room(self, coords):
		room = []
		for y in range(coords[1]):
			room.append([])
			for x in range(coords[0]):
				if y == 0 or y == (coords[1] - 1):
					room[y].append(3)
				elif x == 0 or x == (coords[0] - 1):
					room[y].append(3)
				else:
					room[y].append(1)
		return room


	def get_map_location(self, x, y):
		return self.matrix[y][x]


	def get_first_room_coords(self, first_room, dungeon):
		first_room_position_y = len(dungeon) - len(first_room)
		first_room_position_x = len(dungeon[0]) / 2  - len(first_room[0]) / 2
		first_room_position_y_end = len(dungeon)
		first_room_position_x_end = len(first_room[0]) + first_room_position_x
		return [first_room_position_y, first_room_position_y_end,
				first_room_position_x, first_room_position_x_end, first_room]

	def place_features(self, y_start, y_end, x_start, x_end, feature):
		y_iter = 0
		for y in range(y_start, y_end):
			x_iter = 0
			for x in range(x_start, x_end):
				self.matrix[y][x] = feature[y_iter][x_iter]
				x_iter = x_iter + 1
			y_iter = y_iter + 1


if __name__ == '__main__':
	d = Dungeon(40, 40)
	first_room = d.draw_room(d.create_room())
	d.place_features(*d.get_first_room_coords(first_room, d.matrix))
	print(d.matrix)
