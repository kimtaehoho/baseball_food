from flask import Flask, jsonify, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Post

app = Flask(__name__)

engine = create_engine('mysql+pymysql://root:6625@localhost/baseball_db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def post():
    post = session.query(Post).all()
    return render_template('mainpage.html', post=post)

@app.route('/jamsil')
def jamsil():
    data = session.query(Post).filter(Post.location=='잠실')
    output = ''
    for i in data:
        output += i.title
        output += '</br>'
        output += i.location
        output += '</br>'
        output += i.place
        output += '</br>'
        output += i.main_dish
        output += '</br>'
        output += '</br>'
    return output

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)

