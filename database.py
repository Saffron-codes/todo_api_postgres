import databases
import sqlalchemy
# DATABASE_URL = 'postgresql://postgres:1480@localhost:5432/svik_todo'
DATABASE_URL = "postgresql://mdjnomabkuyoia:c72646976db2aa6442194944f156f6ba653a2cf1985b216943061ed56b369e2d@ec2-52-71-69-66.compute-1.amazonaws.com:5432/d2tn02fcccm2mf"


database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(
DATABASE_URL,pool_size=3, max_overflow=0
)
conn = engine.connect()
metadata.create_all(engine)