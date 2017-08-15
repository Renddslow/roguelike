import pymongo
import redis
import uuid

client = pymongo.MongoClient()
db = client.roguelike


class Players:
	def __init__(self):
		self.players = db.players

	
	def get(self, phone):
		return self.players.find_one({"phoneNumber": phone})

	
	def post(self, player_data):
		return self.players.insert_one(player_data).inserted_id


class PlayerSessions:
	def __init__(self):
		self.r = redis.StrictRedis(host='localhost', port=6379, db=3)
		self.players = db.players
		self.saved_maps = db.savedMaps

	
	def post(self, player, map_, level):
		flat_map = json.dumps(map_)
		save_key = str(uuid.uuid4()).replace('-','')
		self.saved_maps.insert({
			"key": save_key,
			"map": flat_map,
			"player": player['id'],
			"level": level
		})
		self.r.set(
			"player:{}:currentLevel".format(player['id']),
			flat_map
		)
		
