from peewee import SqliteDatabase

database = SqliteDatabase('database.db')

def conect_db()->SqliteDatabase:
   if database.is_closed():
      database.connect()
   return database

def disconnect_db()->None:
   if not database.is_closed():
      database.close()