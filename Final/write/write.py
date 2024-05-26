import os
import sys
from flask import Flask, request, render_template
import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from werkzeug.utils import secure_filename
from baseball_database_setup import Base, User, Post

app = Flask(__name__)
engine = create_engine('mysql+pymysql://root:root@localhost/baseball_db')
Base.metadata.bind = engine

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

DBSession = sessionmaker(bind=engine)
session = DBSession()






@app.route('/')
def index():
    return render_template('write.html')

 
@app.route('/post', methods=['POST'])
def create_post():
    new_post = Post(user_id=111, username='asd', title=request.form['title'], location=request.form['mapOptions'],
                     place=request.form['place'],main_dish=request.form['main_dish'],content=request.form['content'],
                     like_count = 0, image_exist=0)
    

    file = request.files['file']
    if file.filename == '':
        session.add(new_post)
        session.commit()

    if file:
        latest_post = session.query(Post).order_by(Post.post_id.desc()).first()
        if latest_post:
            latest_post.post_id = latest_post.post_id + 1
        else:
            latest_post.post_id = 1

        fileattribute = secure_filename(file.filename)
        fileattribute = fileattribute[-4:]
        filename = str(latest_post.post_id) + fileattribute
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        session.add(new_post)
        session.commit()

    return render_template('main.html',new_post=new_post)




if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)