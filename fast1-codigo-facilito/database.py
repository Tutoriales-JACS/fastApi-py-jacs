from peewee import *

database = SqliteDatabase('customers.db')

class User(Model):
   username = CharField(max_length=50)
   email = CharField(max_length=50, null=True)

   class Meta:
      database = database
      table_name = 'users'
   
   def __str__(self):
      return self.username

