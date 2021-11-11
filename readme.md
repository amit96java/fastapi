Install FastApi:

    pip install fastapi[all]
    check if email-validator not come with fastapi than ->
    pip install email-validator
To Check Installed Libs:

    pip freeze
To Start The WebServer:

    uvicorn Main:app (app is instance of fastapi in Main file)

To Reload The WebServer:

    uvicorn Main:app --reload
    uvicorn app.Main:app --reload -> app is python package here


To define Shcema:

    pydantic (it should be with fastapi libs)

To View documentation page of fastapi:
    
    http://127.0.0.1:8000/docs -> fastapi has built in swagger api support
    http://127.0.0.1:8000/redoc

To Install Oracle Libs:

    C:\PycharmProjects\fastapi> pip install cx_Oracle

Python ORM:
    
    Sqlalchemy is one of the most popular python ORMs
    pip install sqlalchemy
    after install check driver for particular db

6:1:45
To Install passlib for hashing
    
     pip install passlib[bcrypt]

To install python-jose to generate and verify the JWT tokens in python

    pip install python-jose[cryptography]

8:17
8:38
9:05:
9:21
    how to set db password in env variable 
9:24:37
    composite keys
9:34:59
    vote route description
9:47:40
10:5
    very good join concept must revice time to time

10:15:30 
    join with sqlalchemy

10:31:50
    new tool to add column in table because sqlalchemy don't allow
to add new column

database tool migration

     pip install alembic
     PS C:\PycharmProjects\fastapi>alembic init alembic

CORS Concept

    11:14

To List Down all the libraries in a file

     pip freeze > requirement.txt
     pip install -r requirements.txt => to install all the libs


git remote add origin https://github.com/amit96java/fastapi.git
git branch -M main
git push -u origin main
