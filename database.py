import databases
import dotenv
import sqlalchemy
import os
# DATABASE_URL = 'postgresql://postgres:1480@localhost:5432/svik_todo'

username = dotenv.get_key("./.env","USERNAME")
password = dotenv.get_key("./.env","PASSWORD")
host = dotenv.get_key("./.env","HOST")
port = dotenv.get_key("./.env","PORT")
database_name = dotenv.get_key("./.env","DATABASE_NAME")


DATABASE_URL = 'postgresql://{username}:{password}@{host}:5432/{database_name}'.format(username=username,password=password,host=host,port=port,database_name=database_name)


database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(
DATABASE_URL,pool_size=3, max_overflow=0
)
conn = engine.connect()
metadata.create_all(engine)