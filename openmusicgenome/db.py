from pymongo import MongoClient

DATABASE_URL_PREFIX = 'mongodb://'
DATABASE_URL_SUFFIX = '@ds043447.mongolab.com:43447/openmusicgenome'
READ_ONLY_USER = 'read'
READ_ONLY_PASSWORD = '123'

class OpenMusicDB(Object):
	def __init__(self, user, password):
		dburl = DATABASE_URL_PREFIX + user + ':' + password + DATABASE_URL_SUFFIX
		client = MongoClient(dburl)
		self.db = client['openmusicdata']