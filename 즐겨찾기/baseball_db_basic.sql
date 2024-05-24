
DROP DATABASE IF EXISTS baseball_db;
CREATE DATABASE baseball_db default CHARACTER SET UTF8MB4;
USE baseball_db;

drop table IF EXISTS user;

CREATE TABLE user (
  user_id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(50) NOT NULL,
  password VARCHAR(50) NOT NULL,
  email VARCHAR(100) NOT NULL
) ENGINE=INNODB;

drop table IF EXISTS post;

CREATE TABLE post (
  post_id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT NOT NULL,   -- VARCHAR(50) NOT NULL,
  title VARCHAR(50) NOT NULL,
  location VARCHAR(50) NOT NULL,
  place VARCHAR(50) NOT NULL,
  main_dish VARCHAR(50) NOT NULL,
  -- content VARChAR(4000) NOT NULL,
  create_time TIMESTAMP(6) NOT NULL,
  update_time TIMESTAMP(6) NOT NULL,
  FOREIGN KEY (user_id) REFERENCES user(user_id)  -- 외래 키 설정 추가
) ENGINE=INNODB;

drop table IF EXISTS post_like;

CREATE TABLE post_like (
  like_id INT AUTO_INCREMENT PRIMARY KEY,
  post_id INT,
  user_id INT,
  FOREIGN KEY (post_id) REFERENCES post(post_id),
  FOREIGN KEY (user_id) REFERENCES user(user_id)
) ENGINE=INNODB;

-- 초기 데이터 삽입
INSERT INTO user (username, password, email) VALUES ('user1', 'password1', 'user1@example.com');
INSERT INTO user (username, password, email) VALUES ('user2', 'password2', 'user2@example.com');

INSERT INTO post (user_id, title, location, place, main_dish, create_time, update_time) VALUES (1, '통밥', '잠실', '3루2층', '김치말이국수', NOW(), NOW());
INSERT INTO post (user_id, title, location, place, main_dish, create_time, update_time) VALUES (2, '와팡', '잠실', '1,3루 내야', '와플 아이스크림', NOW(), NOW());

INSERT INTO post_like (post_id, user_id) VALUES (1, 2);  -- user2가 post_id가 1인 게시물에 좋아요를 누름
INSERT INTO post_like (post_id, user_id) VALUES (2, 1);  -- user1이 post_id가 2인 게시물에 좋아요를 누름


COMMIT;
