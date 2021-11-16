from fastapi.testclient import TestClient
from app.main import app
from app.config import settings
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from app.database import get_db
from app.database import Base
import pytest

SQLALCHEMY_DATABASE_URL = 'oracle://amit_test:abcd1234@127.0.0.1:1521/xe'
# SQLALCHEMY_DATABASE_URL = f'oracle://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:' \
#                           f'{settings.database_port}/xe'

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, max_identifier_length=30)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


"""
here below we are overriding the testing db with original db for testing purpose
"""
app.dependency_overrides[get_db] = override_get_db

# client = TestClient(app)
