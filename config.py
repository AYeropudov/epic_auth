import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://epicrpg:e36BbwM2x6Tm@127.0.0.1:3307/epic'
    JWT_KEY = 's9A1NDxIkPAqEIQHThy5Oh'
    BASE_DIR = basedir
