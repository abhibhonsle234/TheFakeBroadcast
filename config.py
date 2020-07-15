import os

class Config(object):
	SECRET_KEY = os.environ.get("SECRET_KEY") or b'*\xaa\xe7T\xae\xe9:|!\x00\xefk\x87<0\x8c'

	MONGODB_SETTINGS = { 'db': 'UTA_Enrollment' }