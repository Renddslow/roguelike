import random


class Dungeon:
	def __init__(self, x, y):
		self.screen_width = x
		self.screen_height = y
		map_ = self.draw_map(
			self.screen_width,
			self.screen_height
		)
		room = self.create_room(
			self.screen_width * .1, 
			self.screen_height * .1
		)
		print(map_)
		print(room)


	def draw_map(self, max_x, max_y):
		arr = []
		for y in max_y:
			arr.append([])
			for x in max_x:
				arr[y].append(0)
		return arr

	
	def create_room_coords(self, max_x, max_y):
		x = random.randrange(max_x)
		y = random.randrange(max_y)
		return x, y
