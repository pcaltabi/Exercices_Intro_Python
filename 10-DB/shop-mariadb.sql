DROP DATABASE IF EXISTS shop;
CREATE DATABASE shop DEFAULT CHARACTER SET 'utf8';
use shop

-- A table for the articles of the shop
CREATE TABLE articles (
	id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(100),
	collection TEXT,
	price FLOAT UNSIGNED,
	stock INT UNSIGNED
) ENGINE = InnoDB;


INSERT INTO articles VALUES 
	(NULL, 'HARMONIEUSE', '2018 SpringSummer', 140.0, 10),
	(NULL, 'SCOTTISH', '2018 SpringSummer', 105.0, 4),
	(NULL, 'SISTEM SOLAIRE', '2017 XMasCollection', 230, 6),
	(NULL, 'PIEGE' ,'2017 Winter' , 120.0, 12);


