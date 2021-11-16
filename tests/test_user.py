import pytest
from .database import engine
from .database import Base
from .database import TestClient
from .database import app
from app import dto

@pytest.fixture
def client():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    #run our code before we return our testClient
    yield TestClient(app)
    #run our code after our test finishes
    # Base.metadata.drop_all(bind=engine)

def test_root(client):
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

def test_create_user_with_pydantic(client):
    res = client.post("/u/users",json={"id":120,"email":"120@gmail.com","password":"root"})
    new_user=dto.UserResponse(**res.json())
    assert new_user.email=="120@gmail.com"
    assert res.status_code == 201