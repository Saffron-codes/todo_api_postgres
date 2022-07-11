import sqlalchemy

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('user_id',sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('name',sqlalchemy.TEXT(200)),
    sqlalchemy.Column('email',sqlalchemy.TEXT(200)),
    sqlalchemy.Column('password',sqlalchemy.TEXT(6)),
)


todos = sqlalchemy.Table(
    'todos',
    metadata,
    sqlalchemy.Column('id',sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('description',sqlalchemy.TEXT),
    sqlalchemy.Column('user_id',sqlalchemy.Integer),
)