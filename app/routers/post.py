from .. import models,dto,utils,oauth2
from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session
from app.database import get_db,cur,conn
from typing import List
from fastapi.params import Body
import cx_Oracle as db

router=APIRouter(
    prefix="/p",
    tags=['Post']
)



my_post=[{"title":"title of post 1", "content":"content of post 1" , "id":1},
         {"title":"title of post 2","content":"content of post 2","id":2}]

def find_index_post(id):
    for i,p in enumerate(my_post):
        if p['id'] == id:
            return i


@router.get("/posts")
def getData():
    cur.execute(""" select * from posts """)
    posts=cur.fetchall()
    print(posts)
    return {"my_data":posts}

@router.post("/demoPost")
def demoPost(payload: dict=Body(...)):
    print(payload)
    return {"new_post": f"name: {payload['name']} api:{payload['api']}"}

@router.post("/createPost",status_code=status.HTTP_201_CREATED)
def createPost(new_post:dto.PostCreate):
    print(new_post)
    cur.execute(""" insert into posts(serial_id,title,content_data,published,create_at) values (102,'first post','content of first post','true',TO_DATE(sysdate, 'dd/mm/yyyy hh24:mi:ss')) """)
    conn.commit()
    return {"data":"inserted successfully"}

@router.get("/posts/{id}") #always keep in mind that path should be unique
def getPost(id:int,response:Response):
    print("id iss ",id)
    print(type(str(id)))
    cur.execute(""" select * from posts where serial_id = :id """,id=str(id))
    post=cur.fetchone()
    print(post)
    if not post:#means post is null
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND
                            ,detail=f"post with id: {id} was not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message":f"post with id: {id} was not found"}
    return {"post_detail": f"here is post {id}"}

# @app.get("/posts/latest") #this path can affect the call of above one
# def get_latest_post():
#     post = my_post[len(my_post)-1]
#     return {"detail":post}

# deleting post
# find the index in the array that has required id
@router.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_post(id)
    if index==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")

    my_post.pop(index)
    return {"message": "post was sucessfully deleted"}

@router.put("/posts/{id}")
def update_post(id:int , post: dto.PostCreate):
    cur.execute("""update posts set title = :title where serial_id =:id""",title="updated title",id=str(id))
    conn.commit()
    # print(post)
    # index = find_index_post(id)
    # if index == None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail=f"post with id: {id} does not exist")
    # post_dict = post.dict() #post is coming data from frontend
    # post_dict['id']=id
    # my_post[index] = post_dict
    return {"message":"updated successfully"}