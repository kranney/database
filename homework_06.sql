CREATE TABLE hotel
(
	hotelNo INTEGER NOT NULL PRIMARY KEY,
	hotelName VARCHAR(10) NOT NULL FOREIGN KEY, -- do i need to make sure this is a foreign key?
	city VARCHAR(20) NOT NULL FOREIGN KEY
);

CREATE TABLE room
(
	roomNo, INTEGER NOT NULL PRIMARY KEY,
	hotelNo INTEGER NOT NULL PRIMARY KEY,
	type CHAR(10) NOT NULL FOREIGN KEY,
	price MONEY NOT NULL FOREIGN KEY,
	CHECK (type = 'Single' OR type = 'Double' OR type = 'Family'),
	CHECK (price >= MONEY(10) AND price <= MONEY(100)),
	CHECK (roomNo >= 1 AND roomNo <= 100),
);

CREATE TABLE