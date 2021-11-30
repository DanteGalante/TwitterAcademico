from peewee import *

user = 'root'
password = 'Pythonjavascript29.'
db_name = 'twitteracademico'

conn = MySQLDatabase(
    db_name, user=user,
    password=password,
    host='localhost'
)

class BaseModel(Model):
    class Meta:
        database = conn