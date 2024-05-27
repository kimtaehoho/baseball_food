from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from baseball_database_setup import Base, User, Post

app = Flask(__name__)

engine = create_engine('mysql+pymysql://root:root@localhost/baseball_db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
db_session = DBSession()


@app.route('/mypage')
def mypage():

    user_id = session.get('user_id')

    # 내가 작성한 글 가져오기
    my_posts = db_session.query(Post).filter(Post.user_id == user_id).all()

    # 좋아요한 글 가져오기
    liked_post_ids = db_session.query(User.like_post).filter(User.user_id == user_id).scalar()

    # liked_post_ids가 None인 경우 빈 리스트로 설정
    if not liked_post_ids:
        liked_post_ids = []

    liked_posts = db_session.query(Post).filter(Post.post_id.in_(liked_post_ids)).all()

    my_posts_data = [
        {
            'post_id': post.post_id,
            'title': post.title,
            'location': post.location,
            'place': post.place,
            'main_dish': post.main_dish,
            'content': post.content,
            'image_exist': post.image_exist  # 추가된 이미지 존재 여부 필드
        } for post in my_posts
    ]

    liked_posts_data = [
        {
            'post_id': post.post_id,
            'title': post.title,
            'location': post.location,
            'place': post.place,
            'main_dish': post.main_dish,
            'content': post.content,
            'image_exist': post.image_exist  # 추가된 이미지 존재 여부 필드
        } for post in liked_posts
    ]

    return jsonify({
        'success': True,
        'my_posts': my_posts_data,
        'liked_posts': liked_posts_data
    })


@app.route('/mypage/location/<location>')
def get_posts_by_location(location):

    user_id = session.get('user_id')

    my_posts = db_session.query(Post).filter_by(user_id=user_id, location=location).all()

    liked_posts = db_session.query(Post).join(Post.like_post).filter(User.user_id == user_id, Post.location == location).all()

    return jsonify({
        'success': True,
        'posts': [post.serialize for post in my_posts + liked_posts]
    })


@app.route('/edit_post/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post = db_session.query(Post).filter_by(post_id=post_id).first()

    if request.method == 'POST':
        post.title = request.form['title']
        post.location = request.form['location']
        post.place = request.form['place']
        post.main_dish = request.form['main_dish']
        post.content = request.form['content']

        db_session.commit()
        return redirect('/')
        # return redirect(url_for('mypage'))

    return render_template('edit_post.html', post=post)


@app.route('/delete_post/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    post = db_session.query(Post).filter_by(post_id=post_id).first()

    try:
        db_session.delete(post)
        db_session.commit()
        return jsonify({'success': True})
    except Exception as e:
        print(e)
        return jsonify({'success': False})


@app.route('/')
def index():
    return render_template('mypage.html')


if __name__ == '__main__':
    app.run(debug=True)