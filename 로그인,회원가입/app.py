from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base, User as UserModel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1108@localhost/baseball_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# SQLAlchemy 연결
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = session.query(UserModel).filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            return "로그인 성공"
        else:
            return "로그인 실패"
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        confirm_password = request.form['confirm_password']
        
        if password != confirm_password:
            return "비밀번호가 일치하지 않습니다."
        
        try:
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            new_user = UserModel(username=username, password=hashed_password, email=email)
            session.add(new_user)
            session.commit()
            return redirect(url_for('login'))
        except Exception as e:
            session.rollback()
            return f"회원가입 중 오류가 발생했습니다: {str(e)}"
    
    return render_template('register.html')

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app.run(debug=True)
