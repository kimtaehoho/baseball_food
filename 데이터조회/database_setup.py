import sys
import pymysql

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine


# declarative_base() : Table 생성을 위한 부모 class인 Base 생성하는 함수
Base = declarative_base()


# class Restaurant(Base):
#     __tablename__ = 'restaurant'

#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)


class Post(Base):
    __tablename__ = 'post'

    post_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, primary_key=True)
    title = Column(String(80), nullable=False)
    location = Column(String(250))
    place = Column(String(80))
    main_dish = Column(String(250))
    # restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    # restaurant = relationship(Restaurant)


##### insert at end of file #####
## mysql+pymysql://루트:비밀번호@localhost/restaurant
engine = create_engine('mysql+pymysql://root:6625@localhost/baseball_db')

Base.metadata.create_all(engine)
