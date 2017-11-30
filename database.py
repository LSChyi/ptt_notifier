from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase
from config import ptt_config
import os.path
import logging

created = os.path.isfile(ptt_config['checked_posts_db'])
db = SqliteExtDatabase(ptt_config['checked_posts_db'])

class Post(Model):
    title = CharField()
    url = CharField(unique=True)
    class Meta:
        database = db

db.connect()
if not created:
    logging.info('Create new table')
    db.create_tables([Post])
