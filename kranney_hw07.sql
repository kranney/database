-- 1)

CREATE OR REPLACE PROCEDURE Hotels
	AS
	SELECT hotelNo, hotelName
	FROM Hotel
	WHERE city = 'London';

-- 2)
-- List all double or family rooms with a price below 40 per night, in ascending order of price
CREATE OR REPLACE PROCEDURE singles_and_doubles_<40
	AS
	SELECT roomNo, hotelNo, type, price
	WHERE price < MONEY(40)
		AND (type = 'Double' OR type = 'Family')
	ORDER BY price;
--3)

CREATE TRIGGER double_rooms_>100
	BEFORE INSERT ON Room
	REFERENCING NEW AS new_room
	BEGIN
		IF new_room.type = 'Double' AND new_room.price > MONEY(100)
			raise_application_error('')
		END IF;
	END;