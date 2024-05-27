from flask import Flask, jsonify, redirect, render_template, request, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Post

app = Flask(__name__)

engine = create_engine('mysql+pymysql://root:root@localhost/baseball_db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
def post():
    post = session.query(Post).all()
    return render_template('main.html', post=post)


@app.route('/<string:location>')
def goToLocation(location):
    post = session.query(Post).filter(Post.location==location)
    return render_template('main.html', post=post)


@app.route('/<string:post_id>',
           methods=['POST'])
def likeAction(post_id):
    thisPost = session.query(Post).filter_by(post_id=post_id).one()
    if request.method == 'POST':
        if thisPost.like_count==0:
            thisPost.like_count = 1
        elif thisPost.like_count==1:
            thisPost.like_count = 0
        session.add(thisPost)
        session.commit()
        return redirect(request.referrer)


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)

