
DROP DATABASE IF EXISTS baseball_db;
CREATE DATABASE baseball_db DEFAULT CHARACTER SET UTF8MB4;
USE baseball_db;

DROP TABLE IF EXISTS user;

CREATE TABLE user (
  user_id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(50) NOT NULL,
  password VARCHAR(50) NOT NULL,
  email VARCHAR(100) NOT NULL
) ENGINE=INNODB;

DROP TABLE IF EXISTS post;

CREATE TABLE post (
  post_id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT NOT NULL,
  title VARCHAR(50) NOT NULL,
  location VARCHAR(50) NOT NULL,
  place VARCHAR(50) NOT NULL,
  main_dish VARCHAR(50) NOT NULL,
  content VARCHAR(1000),  -- content 컬럼 추가
  create_time TIMESTAMP(6) NOT NULL,
  update_time TIMESTAMP(6) NOT NULL,
  FOREIGN KEY (user_id) REFERENCES user(user_id)
) ENGINE=INNODB;

DROP TABLE IF EXISTS post_like;

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

INSERT INTO post (user_id, title, location, place, main_dish, content, create_time, update_time) VALUES 
(1, '통밥', '잠실', '3루2층', '김치말이국수', '김치말이국수가 정말 맛있어요!', NOW(), NOW()),
(2, '와팡', '잠실', '1,3루 내야', '와플 아이스크림', '와플과 아이스크림 조합이 일품이에요!', NOW(), NOW()),
(2, '이가네떡볶이', '잠실', '3루 게이트', '떡볶이', '떡볶이 맛있다', NOW(), NOW()),
(1, '허갈닭강정', '문학', '1루 1층', '닭강정', '닭강정 먹고싶음', NOW(), NOW()),
(2, '와인샵', '문학', '1루 1층', '나쵸', '나-쵸!', NOW(), NOW());

INSERT INTO post_like (post_id, user_id) VALUES (1, 2);  -- user2가 post_id가 1인 게시물에 좋아요를 누름
INSERT INTO post_like (post_id, user_id) VALUES (2, 1);  -- user1이 post_id가 2인 게시물에 좋아요를 누름
INSERT INTO post_like (post_id, user_id) VALUES (3, 1);
INSERT INTO post_like (post_id, user_id) VALUES (5, 1);

COMMIT;
