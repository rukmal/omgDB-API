from pymongo import MongoClient

DATABASE_URL_PREFIX = 'mongodb://'
DATABASE_URL_SUFFIX = '@ds043447.mongolab.com:43447/openmusicgenome'
READ_ONLY_USER = 'read'
READ_ONLY_PASSWORD = '123'

class OpenMusicDB(Object):
	def __init__(self, **kwargs):
		'''Function to initialize a new omgDB session
		Args:
			
		'''
		dburl = ''
		try:
			dburl = DATABASE_URL_PREFIX + kwargs['user'] + ':' + kwargs['password'] + DATABASE_URL_SUFFIX
		except:
			dburl = DATABASE_URL_PREFIX + READ_ONLY_USER  + ':' + READ_ONLY_PASSWORD + DATABASE_URL_SUFFIX
		client = MongoClient(dburl)
		self.db = client['openmusicdata']
		print kwargs

	def authenticate()