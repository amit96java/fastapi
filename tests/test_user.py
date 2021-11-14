from fastapi.testclient import TestClient
from app.main import app
from app import dto
from app.config import settings
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import  create_engine
from app.database import get_db
from app.database import Base

SQLALCHEMY_DATABASE_URL = 'oracle://amit_test:abcd1234@127.0.0.1:1521/xe'
# SQLALCHEMY_DATABASE_URL = f'oracle://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:' \
#                           f'{settings.database_port}/xe'

engine = create_engine(SQLALCHEMY_DATABASE_URL,echo=True,max_identifier_length=30)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush= False, bind=engine)

Base.metadata.create_all(bind=engine)



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

client = TestClient(app)

def test_root():
    res = client.get("/")
    print("result of end point ",res.json())
    print("result of end point ",res.json().get("message"))
    assert res.json().get("message") == 'Hello World!!!!'
    assert res.status_code == 201

# def test_create_user():
#     res = client.post("/u/users",json={"id":118,"email":"118@gmail.com","password":"root"})
#     print(res.json())
#     assert res.json().get("email")=="118@gmail.com"
#     assert res.status_code == 201

def test_create_user_with_pydantic():
    res = client.post("/u/users",json={"id":120,"email":"120@gmail.com","password":"root"})
    new_user=dto.UserResponse(**res.json())
    assert new_user.email=="119@gmail.com"
    assert res.status_code == 201