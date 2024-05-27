DROP DATABASE IF EXISTS baseball_db;
CREATE DATABASE baseball_db default CHARACTER SET UTF8MB4;
USE baseball_db;

CREATE TABLE user (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(200) NOT NULL,
    email VARCHAR(50) NOT NULL UNIQUE,
    like_post TEXT DEFAULT '[]'
);

CREATE TABLE post (
    post_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    username VARCHAR(20),
    title VARCHAR(80) NOT NULL,
    location VARCHAR(250),
    place VARCHAR(80),
    main_dish VARCHAR(250),
    content VARCHAR(1000),
    like_count INT DEFAULT 0,
    image_exist BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);
