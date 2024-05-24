import pymysql

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Post, Base

engine = create_engine('mysql+pymysql://root:6625@localhost/baseball_db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Menu for UrbanBurger
post1 = Post(post_id=1, user_id=111, title="통밥", location="잠실", place="3루 2층", main_dish='김치말이국수')

session.add(post1)
session.commit()


post2 = Post(post_id=2, user_id=222, title="와팡", location="잠실", place="1,3루 내야", main_dish='와플 아이스크림')

session.add(post2)
session.commit()


post3 = Post(post_id=3, user_id=333, title="이가네떡볶이", location="잠실", place="3루 게이트", main_dish='떡볶이')

session.add(post3)
session.commit()


post4 = Post(post_id=4, user_id=444, title="허갈닭강정", location="문학", place="1루 1층", main_dish='닭강정')

session.add(post4)
session.commit()


post5 = Post(post_id=5, user_id=555, title="와인샵", location="문학", place="1루 1층", main_dish='나쵸')

session.add(post5)
session.commit()


print ("added menu items!")