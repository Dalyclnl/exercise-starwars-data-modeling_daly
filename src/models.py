import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er
import enum  


##class User(Base):
   ## __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
   ## id = Column(Integer, primary_key=True)
    ##name = Column(String(250), nullable=False)

## class Address(Base):
   ## __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    ##id = Column(Integer, primary_key=True)
   ## street_name = Column(String(250))
   ## street_number = Column(String(250))
    ##post_code = Column(String(250), nullable=False)
   ## person_id = Column(Integer, ForeignKey('person.id'))
   ## person = relationship(Person)

Base = declarative_base()

class Media_enum(enum.Enum):
    imagen = "imagen",
    video = "video"

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user = Column(String(250),primary_key=True)
    name = Column(String(250))
    pasword = Column(String(250))
    email = Column(String(250))

class Followers (Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    user_from = Column(Integer,primary_key=True)
    user_to  = Column(Integer,primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))
    followers = relationship("user")


class Comment (Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True) 
    author_id = Column(Integer, ForeignKey('author.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(String(250))
    created = Column(String(250))
    comment = relationship("user")

class Media (Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    type = Column(String(250))
    url = Column(String(250))
    media = Column(String(250))
    media = relationship("post")

class Post (Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))  
    comment_id =Column(Integer,ForeignKey('comment.id'))
    date = Column(String(250))
    text = Column(String(250))
    media = Column(String(250))
    post = relationship("user")
    post = relationship("comment")
  


    def to_dict(self):
        return {}


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
