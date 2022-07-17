import os
import dotenv

username = os.environ.get("USERNAME")
password = os.environ.get("PASSWORD")
host = os.environ.get("HOST")
database_name = os.environ.get("DATABASE_NAME")

if(password ==None):
    username = dotenv.get_key("./.env","USERNAME")
    password = dotenv.get_key("./.env","PASSWORD")
    host = dotenv.get_key("./.env","HOST")
    database_name = dotenv.get_key("./.env","DATABASE_NAME")

print("Username",username)
print("Password",password)
print("Host",host)
print("Database Name",database_name)

# [global]
# target = /Users/Saffron/pyver/py3105/Lib/site-packages