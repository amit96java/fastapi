from fastapi import APIRouter,Depends,status,HTTPException,Response
from sqlalchemy.orm import Session
from .. import database,dto,models,utils,oauth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from typing import List

router=APIRouter(tags=['Authentication'])

@router.post("/login")
def login(user_credentials:dto.UserLogin,db:Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.email).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalid Credentials")

    if not utils.verify(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalid Credentials")

    #create a token
    #return token
    access_token=oauth2.create_access_token(data={"user_id":user.id})
    return{"token":access_token,"token_type":"bearer"}

@router.post("/login1",response_model=dto.Token)
def login_(user_credentials:OAuth2PasswordRequestForm=Depends(),db:Session = Depends(database.get_db)):

    #it's going to return username and password
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Invalid Credentials")

    if not utils.verify(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Invalid Credentials")

    #create a token
    #return token
    access_token=oauth2.create_access_token(data={"user_id":user.id})
    return{"access_token":access_token,"token_type":"bearer"}