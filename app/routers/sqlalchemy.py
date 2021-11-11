from .. import models,dto,utils,oauth2
from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List,Optional
from fastapi.params import Body
import cx_Oracle as db

router=APIRouter(
    prefix="/alchemy",
    tags=['Alchemy']
)

#http://127.0.0.1:8000/alchemy/sqlalchemy/getAll

@router.get("/sqlalchemy/getAll",response_model=List[dto.Post])
def test_posts(db: Session = Depends(get_db),limit:int=10,skip:int=0,search:Optional[str]=""):
    print("limit is ",limit)
    # posts=db.query(models.Post).all()#models represent table and all means return all data
    posts=db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    return posts

##http://127.0.0.1:8000/alchemy/sqlalchemy/post
#Note:
#     before creating the post user should have the jwt token
@router.post("/sqlalchemy/post",status_code=status.HTTP_201_CREATED,response_model=List[dto.Post])
def save_posts(post:dto.PostCreate,db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    # new_post=models.Post(id=post.id,title=post.title,content=post.content,published=post.published)
    #instead using above line , we can use below one to reduce the large fields iteration
    print("current user id ",current_user.id)#this id is coming get_current_user method and this method extracting id from jwt
    print("current user is ",current_user)
    new_post=models.Post(owner_id=current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {new_post}

#ttp://127.0.0.1:8000/alchemy/sqlalchemy/getById/8
@router.get("/sqlalchemy/getById/{id}")
def get_by_id(id:int , db:Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first() #filter works as where clause
    return {post}

@router.delete("/sqlalchemy/deleteById/{id}")
def deleteById(id:int , db:Session = Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    post_query=db.query(models.Post).filter(models.Post.id==id)
    post=post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not authorized to perform requested action")
    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/sqlalchemy/updateById/{id}")
def updateById(id:int ,updated_post:dto.PostCreate, db:Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    # post_query.update({'title':'hey','content':'this'},synchronize_session=False)
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return {"data":"successfull"}