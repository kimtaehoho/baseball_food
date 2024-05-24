# 나오긴함(내가 쓴 글에 글 다 나옴, 좋아요 글 X)
# from flask import Flask, request, jsonify, render_template
# import mysql.connector
#
# app = Flask(__name__)
#
#
# def get_db_connection():
#     return mysql.connector.connect(
#         host='localhost',
#         user='root',
#         password='root',
#         database='baseball_db'
#     )
#
#
# @app.route('/mypage')
# def mypage():
#     conn = get_db_connection()
#     cursor = conn.cursor(dictionary=True)
#
#     cursor.execute("SELECT * FROM post")
#     my_posts = cursor.fetchall()
#
#     cursor.execute("SELECT * FROM post_like")
#     liked_posts = cursor.fetchall()
#
#     conn.close()
#
#     return jsonify({
#         'success': True,
#         'my_posts': my_posts,
#         'liked_posts': liked_posts
#     })
#
#
# @app.route('/')
# def index():
#     return render_template('mypage.html')
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

# 2. + 내가 쓴 글 나옴
# from flask import Flask, request, jsonify, render_template
# import mysql.connector
#
# app = Flask(__name__)
#
# def get_db_connection():
#     return mysql.connector.connect(
#         host='localhost',
#         user='root',
#         password='root',
#         database='baseball_db'
#     )
#
# @app.route('/mypage')
# def mypage():
#     user_id = 1  # 로그인한 사용자의 ID (나중에 로그인 기능을 추가하여 동적으로 설정하세요)
#
#     conn = get_db_connection()
#     cursor = conn.cursor(dictionary=True)
#
#     cursor.execute("SELECT * FROM post WHERE user_id = %s", (user_id,))
#     my_posts = cursor.fetchall()
#
#     cursor.execute("SELECT * FROM post_like WHERE user_id = %s", (user_id,))
#     liked_posts = cursor.fetchall()
#
#     conn.close()
#
#     return jsonify({
#         'success': True,
#         'my_posts': my_posts,
#         'liked_posts': liked_posts
#     })
#
# @app.route('/')
# def index():
#     return render_template('mypage.html')
#
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)


def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='baseball_db'
    )

# 내가 쓴 글, 좋아요 글 잘 불러옴!!(수정, 삭제는 안되는듯)
@app.route('/mypage')
def mypage():
    user_id = 1  # 로그인한 사용자의 ID (나중에 로그인 기능을 추가하여 동적으로 설정하세요)

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT p.* 
        FROM post p
        JOIN post_like pl ON p.post_id = pl.post_id
        WHERE pl.user_id = %s
    """, (user_id,))
    liked_posts = cursor.fetchall()

    cursor.execute("SELECT * FROM post WHERE user_id = %s", (user_id,))
    my_posts = cursor.fetchall()

    conn.close()

    return jsonify({
        'success': True,
        'my_posts': my_posts,
        'liked_posts': liked_posts
    })


@app.route('/delete_post/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM post WHERE post_id = %s", (post_id,))
        conn.commit()
        return jsonify({'success': True})
    except Exception as e:
        print(e)
        return jsonify({'success': False})

    finally:
        conn.close()



@app.route('/')
def index():
    return render_template('mypage.html')


if __name__ == '__main__':
    app.run(debug=True)
