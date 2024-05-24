from flask import Flask, request, jsonify, render_template, redirect, url_for
import mysql.connector
from datetime import datetime

app = Flask(__name__)


def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='baseball_db'
    )


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


@app.route('/edit_post/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        data = request.get_json()
        new_title = data.get('title')
        new_location = data.get('location')
        new_place = data.get('place')
        new_main_dish = data.get('main_dish')
        new_content = data.get('content')
        update_time = datetime.now()

        try:
            cursor.execute("""
                UPDATE post
                SET title = %s, location = %s, place = %s, main_dish = %s, content = %s, update_time = %s
                WHERE post_id = %s
            """, (new_title, new_location, new_place, new_main_dish, new_content, update_time, post_id))
            conn.commit()
            conn.close()
            return jsonify({'success': True})
        except Exception as e:
            conn.close()
            print(e)
            return jsonify({'success': False})
    else:
        cursor.execute("SELECT * FROM post WHERE post_id = %s", (post_id,))
        post = cursor.fetchone()
        conn.close()
        return render_template('edit_post.html', post=post)


@app.route('/delete_post/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM post_like WHERE post_id = %s", (post_id,))
        cursor.execute("DELETE FROM post WHERE post_id = %s", (post_id,))
        conn.commit()
        conn.close()
        return jsonify({'success': True})
    except Exception as e:
        conn.rollback()
        conn.close()
        print(f"Error deleting post: {e}")
        return jsonify({'success': False, 'error': str(e)})


@app.route('/')
def index():
    return render_template('mypage.html')


if __name__ == '__main__':
    app.run(debug=True)
