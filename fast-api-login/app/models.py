
from peewee import (
   Model, 
   CharField, 
   BooleanField, 
   ForeignKeyField, 
)
from app import db

class User(Model):
   username = CharField(max_length=255, unique=True)
   password = CharField(max_length=255)
   email = CharField(max_length=255, unique=True, null=True)
   first_name = CharField(max_length=255, null=True)
   last_name = CharField(max_length=255, null=True)
   phone = CharField(max_length=255, null=True)
   address = CharField(max_length=255, null=True)
   city = CharField(max_length=255, null=True)
   is_active = BooleanField(default=True)

   class Meta:
      database = db.database

class Token(Model):
   user = ForeignKeyField(User, backref='tokens')
   token = CharField(max_length=255, unique=True)

   class Meta:
      database = db.database