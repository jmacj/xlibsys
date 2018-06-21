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

class Acquisition(BaseModel):
    bn = CharField(primary_key=True)
    title = CharField(max_length=255)
    author = CharField(max_length=255)
    publisher = CharField(max_length=255)
    published_on = DateField()
    tags = CharField(max_length=100)
    no_of_copies = IntegerField()

    class Meta:
    	table_name = 'acquisition'

class Inventory(BaseModel):
	inventory_id = CharField(primary_key=True)
	title = CharField(max_length=255)
	author = CharField(max_length=255)
	publisher = CharField(max_length=255)
	published_on = DateField()
	tags = CharField(max_length=100)
	status = CharField(default='On Shelf')

class Circulation(BaseModel):
	id = PrimaryKeyField()
	copy = ForeignKeyField(Inventory, related_name='circulations')
	user = ForeignKeyField(User, related_name='borrowed_books')
	borrowed_date = DateField()
	due_date = DateField()
	returned_date = DateField()
	status = SmallIntegerField(default=0)

class Reservation(BaseModel):
	id = PrimaryKeyField()
	book = ForeignKeyField(Inventory, related_name='reservations')
	user = ForeignKeyField(User, related_name='book_reservations')
	reservation_date = DateField()
	due_date = DateField(null=True)
	status = CharField(default='Pending')

def initialize_db():
    db.connect()
    db.create_tables([User, Acquisition, Inventory, Reservation], safe=True)
    create_admin_users()

def close_db():
	db.close()