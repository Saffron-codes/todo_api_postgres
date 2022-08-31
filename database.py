import databases
import dotenv
import sqlalchemy
import os

username = os.environ.get("USERNAME")
password = os.environ.get("PASSWORD")
host = os.environ.get("HOST")
database_name = os.environ.get("DATABASE_NAME")

if(password ==None):
    username = dotenv.get_key("./.env","USERNAME")
    password = dotenv.get_key("./.env","PASSWORD")
    host = dotenv.get_key("./.env","HOST")
    database_name = dotenv.get_key("./.env","DATABASE_NAME")



DATABASE_URL = 'postgresql://{username}:{password}@{host}:7848/{database_name}'.format(username=username,password=password,host=host,database_name=database_name)


database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(
DATABASE_URL,pool_size=3, max_overflow=0
)
conn = engine.connect()
metadata.create_all(engine)