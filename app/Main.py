import datetime
from typing import Optional,List
from fastapi import FastAPI , Response , status , HTTPException , Depends
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
from . import models,dto,utils
from .database import engine, get_db
from sqlalchemy.orm import Session
from .routers import post,user,auth,sqlalchemy,vote

#below line tells alchemy to create all table
models.Base.metadata.create_all(bind=engine)

#fast api instance
app = FastAPI()

app.include_router(vote.router)
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(sqlalchemy.router)

@app.get("/")
async def root():
    return {"message":"Hello World!!!!"}


