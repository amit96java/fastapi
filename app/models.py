from .database import Base
from sqlalchemy import Column, Integer, String, Boolean,ForeignKey
from sqlalchemy.sql.expression import null
from sqlalchemy.dialects.oracle import VARCHAR2
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
class Post(Base):
    __tablename__ = "posts"

    id = Column('searial_id',Integer , primary_key=True)
    title = Column('title',String(128))
    content = Column('content_data',String(32))
    published = Column('published',Integer)
    owner_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False)
    # created_at = Column('created_at',TIMESTAMP(timezone=True),nullable=False,server_default=)
    owner=relationship("User")

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,nullable=False)
    email=Column(String(32),nullable=False,unique=True)
    password=Column(String(32),nullable=False)


class Vote(Base):
    __tablename__="votes"
    user_id= Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),primary_key=True)
    post_id=Column(Integer,ForeignKey("posts.searial_id",ondelete="CASCADE"),primary_key=True)

