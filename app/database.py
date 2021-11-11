from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import cx_Oracle as db
from .config import settings
# SQLALCHEMY_DATABASE_URL = 'oracle://amit_owner:abcd1234@127.0.0.1:1521/xe'
SQLALCHEMY_DATABASE_URL = f'oracle://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:' \
                          f'{settings.database_port}/xe'
#"oracle+cx_oracle://amit_owner:abcd1234@localhost:1521/xe",max_identifier_length=30
engine = create_engine(SQLALCHEMY_DATABASE_URL,echo=True,max_identifier_length=30)

SessionLocal = sessionmaker(autocommit=False, autoflush= False, bind=engine)

Base=declarative_base()

#db dependency referenced to database.py file
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#old way to connect with db
try:
    conn = db.connect("amit_owner/abcd1234@//localhost:1521/xe")
    cur = conn.cursor()
    print("connection was successfull")
except Exception as error:
    print("connecting to dattabse failed")
    print("error: ",error)