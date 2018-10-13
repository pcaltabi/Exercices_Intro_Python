-- A table for the articles of the shop
CREATE TABLE articles (
	id INTEGER PRIMARY KEY,
	name TEXT,
	collection TEXT,
	price REAL,
	stock INTEGER
);


INSERT INTO articles VALUES 
	(NULL, 'HARMONIEUSE', '2018 SpringSummer', 140.0, 10),
	(NULL, 'SCOTTISH', '2018 SpringSummer', 105.0, 4),
	(NULL, 'SISTEM SOLAIRE', '2017 XMasCollection', 230, 6),
	(NULL, 'PIEGE' ,'2017 Winter' , 120.0, 12);


