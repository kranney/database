CREATE TABLE hotel
(
	hotelNo INTEGER NOT NULL PRIMARY KEY,
	hotelName VARCHAR(10) NOT NULL FOREIGN KEY, -- do i need to make sure this is a foreign key?
	city VARCHAR(20) NOT NULL FOREIGN KEY
);

CREATE TABLE room
(
	roomNo, INTEGER NOT NULL PRIMARY KEY,
	hotelNo INTEGER NOT NULL PRIMARY KEY, -- can i have two primary keys?
	type CHAR(10) NOT NULL FOREIGN KEY, -- foreign key?
	price MONEY NOT NULL FOREIGN KEY,
	CHECK (type = 'Single' OR type = 'Double' OR type = 'Family'), -- this is makeing sure that the type of room must be single, double, or family
	CHECK (price >= MONEY(10) AND price <= MONEY(100)), -- making sure price is between 10 & 100
	CHECK (roomNo >= 1 AND roomNo <= 100), -- making sure roomNo are between 100 and 1 inclusive
);

CREATE TABLE booking
(
	hotelNo INTEGER NOT NULL PRIMARY KEY,
	guestNo INTEGER NOT NULL PRIMARY KEY,
	dateFrom DATE NOT NULL PRIMARY KEY,
	dateTo DATE NOT NULL FOREIGN KEY,
	roomNo INTEGER NOT NULL FOREIGN KEY,
	)