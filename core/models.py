from peewee import *
from core import config
from werkzeug.local import LocalProxy
from werkzeug.security import generate_password_hash
import datetime

db = MySQLDatabase(
	config.DB_NAME,
	user=config.DB_USER,
	password=config.DB_PASSWORD,
	host=config.DB_HOST
)

class BaseModel(Model):
	class Meta:
		database = db

class User(BaseModel):
	id = PrimaryKeyField(index=True)
	first_name = CharField(max_length=100)
	last_name = CharField(max_length=100)
	email_address = CharField(unique=True, index=True)
	password = CharField(default='password')
	role = SmallIntegerField(default=3)
	
	class Meta:
		table_name = 'user'

def create_admin_users():
    User.get_or_create(email_address='admin1@xlibsys.com',
        defaults={'password': generate_password_hash('secret'), 'role': 1})
    User.get_or_create(email_address='admin2@xlibsys.com',
        defaults={'password': generate_password_hash('secret'), 'role': 1})
    User.get_or_create(email_address='admin3@xlibsys.com',
        defaults={'password': generate_password_hash('secret'), 'role': 1})

def initialize_db():
    db.connect()
    db.create_tables([User], safe=True)
    create_admin_users()

def close_db():
	db.close()