import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er


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

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250),primary_key=True)
    name = Column(String(250))
    firstname = Column(String(250))
    lastname = Column(String(250))
    email = Column(String(250))


class Favorites (Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    followers_id = Column(Integer, ForeignKey('followers.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    media_id = Column(Integer, ForeignKey('media.id'))
    favorites = relationship("user")


class Followers (Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    last_name = Column(String(250))
    details = Column(String(250))
    followers = relationship("user")


class Post (Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    post = Column(String(250))
    post = relationship("user")
 


class Media (Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    media = Column(String(250))
    media = relationship("user")
    media = relationship("favorites")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
