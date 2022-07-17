import databases
import dotenv
import sqlalchemy
import os
# DATABASE_URL = 'postgresql://postgres:1480@localhost:5432/svik_todo'

username = os.environ.get("USERNAME")
password = os.environ.get("PASSWORD")
host = os.environ.get("HOST")
port = os.environ.get("PORT")
database_name = os.environ.get("DATABASE_NAME")


DATABASE_URL = 'postgresql://{username}:{password}@{host}:5432/{database_name}'.format(username=username,password=password,host=host,port=port,database_name=database_name)


database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(
DATABASE_URL,pool_size=3, max_overflow=0
)
conn = engine.connect()
metadata.create_all(engine)