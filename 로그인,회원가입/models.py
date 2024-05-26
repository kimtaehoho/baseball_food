from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, ARRAY
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(200), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    like_post = Column(ARRAY(Integer), default=[])

class Post(Base):
    __tablename__ = 'post'

    post_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    username = Column(String(20))

    title = Column(String(80), nullable=False)
    location = Column(String(250))
    place = Column(String(80))
    main_dish = Column(String(250))
    content = Column(String(1000))
    like_count = Column(Integer, default=0)
    image_exist = Column(Boolean, default=False)
