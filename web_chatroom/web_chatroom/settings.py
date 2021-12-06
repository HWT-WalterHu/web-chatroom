
# HOST = 'localhost'
# PORT = 3306
# USERNAME = 'walter'
# PASSWORD = 'walterdb123!'
# DB = 'webchatroom'
#
# class DebugConfig():
#     DEBUG = True
#     SQLALCHEMY_DATABASE_URI = f'sqlite:///{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB}'
#     SECRET_KEY = 'webchatroom'

DB = 'webchatroom.db'
DB_URI = f'sqlite:///{DB}'
class DebugConfig():
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = DB_URI
    SECRET_KEY = 'webchatroom'


# from sqlalchemy import create_engine
# engine = create_engine(DB_URI)
# conn = engine.connect()  # 连接)