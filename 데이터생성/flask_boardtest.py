import os
import sys
from flask import Flask, request, render_template
import pymysql
from datetime import datetime
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('board.html')


@app.route('/post', methods=['POST'])
def create_post():
    data = request.form
    title = data.get("title")
    content = data.get("content")

    current_time = datetime.now()

    db = pymysql.connect(host='localhost', user='root', password='root',
                         db='baseball_db', charset='utf8')

    curs = db.cursor()
    sql = "INSERT INTO post (user_id, title, content, create_time, update_time) VALUES (%s, %s, %s, %s, %s)"
    curs.execute(sql, (123, title, content, current_time, current_time))

    db.commit()
    db.close()

    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'

    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'File uploaded successfully'


    return f"Post created with title: {title} and content: {content}"









if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)