DROP DATABASE IF EXISTS psw_9;

CREATE DATABASE psw_9;

USE psw_9;

CREATE TABLE users
(
   id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
   username VARCHAR(32) NOT NULL UNIQUE,
   email VARCHAR(32) NOT NULL UNIQUE,
   password VARCHAR(255) NOT NULL
);

INSERT INTO users (username, email, password) VALUES ('Volodymyr', 'helloworld1@gmail.com', '$2y$08$M1xQyujnNcuaXzUn8S4ytuUjvxxG6iDdgvWnGY1BxSgWPCKViJRLS');
INSERT INTO users (username, email, password) VALUES ('Illia', 'helloworld2@gmail.com', '$2y$08$M1xQyujnNcuaXzUn8S4ytuUjvxxG6iDdgvWnGY1BxSgWPCKViJRLS');
INSERT INTO users (username, email, password) VALUES ('Someone', 'helloworld3@gmail.com', '$2y$08$M1xQyujnNcuaXzUn8S4ytuUjvxxG6iDdgvWnGY1BxSgWPCKViJRLS');
