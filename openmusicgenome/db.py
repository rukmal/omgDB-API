from pymongo import MongoClient

DATABASE_URL_PREFIX = 'mongodb://'
DATABASE_URL_SUFFIX = '@ds043447.mongolab.com:43447/openmusicgenome'

class OpenMusicDB(Object):
	def __init__(self, user, password):
		dburl = DATABASE_URL_PREFIX + user + ':' + password + DATABASE_URL_SUFFIX
		client = MongoClient(dburl)
		self.db = client['openmusicdata']