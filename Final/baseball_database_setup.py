import sys
import pymysql
from sqlalchemy.dialects.mysql import JSON
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean , ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    password = Column(String(1000), nullable=False)
    email = Column(String(50), nullable=False)
    like_post = Column(JSON, default=[])


class Post(Base):
    __tablename__ = 'post'

    post_id = Column(Integer, primary_key=True, autoincrement=True) 
    user_id = Column(Integer, primary_key=True)
    username = Column(String(20), primary_key=True)

    title = Column(String(80), nullable=False)
    location = Column(String(250))
    place = Column(String(80))
    main_dish = Column(String(250))
    content = Column(String(1000))
    like_count = Column(Integer, default=0)
    image_exist = Column(Integer, default=0)


engine = create_engine('mysql+pymysql://root:root@localhost/baseball_db')
Base.metadata.create_all(engine)
