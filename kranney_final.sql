-- Problem 2

-- vehicles (make, model, year, color, numberOfDoors, VIN, branch_id)
-- PRIMARY KEY: (VIN)
-- FOREIGN KEY: (branch_id)

-- clients (name, address, phone_number, client_id, branch_id)
-- PRIMARY KEY (client_id)
-- ALTERNATE KEY (phone_number, address)
-- FOREIGN KEY (branch_id)

-- invoices (id, client_id, branch_id, VIN, sale_date)
-- PRIMARY KEY: (id)
-- ALTERNATE KEY (VIN)
-- FOREIGN KEY: (client_id, branch_id, VIN)

-- branches (id, address, phone_number, manager_id)
-- PRIMARY KEY (id)
-- ALTERNATE KEY (phone_number)
-- FOREIGN KEY (manger_id)

-- client_invoices (invoice_id, client_id)
-- PRIMARY KEY (invoice_id)
-- FOREIGN KEY (invoice_id, client_id)

-- managers (id, name, salary, branch_id)
-- PRIMARY KEY (id)
-- ALTERNATE KEY (branch_id)
-- FOREIGN KEY (branch_id)

-- Problem 3
-- ON PAPER!!!

-- Problem 4

CREATE TABLE managers
(
	id int NOT NULL,
	name varchar(250) NOT NULL,
	salary money NOT NULL,
	branch_id int NOT NULL,
	PRIMARY KEY (id)
	FOREIGN KEY (branch_id)
		REFERENCES branches (id)
);

CREATE TABLE branches
(
	id int NOT NULL,
	address varchar(250) NOT NULL,
	phone_number varchar(20) NOT NULL,
	manager_id int NOT NULL
	PRIMARY KEY (id),
	FOREIGN KEY manager_id
		REFERENCES managers (id)
);

CREATE TABLE vehicles
(
	make varchar(100) NOT NULL,
	model varchar(100) NOT NULL,
	year int NOT NULL,
	number_of_doors int,
	VIN char(40) NOT NULL,
	branch_id int NOT NULL,
	PRIMARY KEY (VIN),
	FOREIGN KEY (branch_id)
		REFERENCES branches (id)
);

CREATE TABLE clients
(
	name varchar(250) NOT NULL,
	address varchar(250) NOT NULL,
	phone_number varchar(20) NOT NULL,
	id int NOT NULL,
	branch_id int NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (branch_id)
		REFERENCES branches (branch_id)
);

CREATE TABLE invoices
(
	id int NOT NULL,
	client_id int NOT NULL,
	branch_id int NOT NULL,
	VIN char(40) NOT NULL,
	sale_date date NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (client_id)
		REFERENCES clients (id),
	FOREIGN KEY (branch_id)
		REFERENCES branches (id),
	FOREIGN KEY (VIN)
		REFERENCES (vehicles)
);

CREATE TABLE client_invoices
(
	invoice_id int NOT NULL,
	client_id int NOT NULL,
	PRIMARY KEY (invoice_id),
	FOREIGN KEY (invoice_id),
		REFERENCES invoices (id),
	FOREIGN KEY (client_id)
		REFERENCES clients (id)
);

CREATE TABLE client_cars
(
	client_id int NOT NULL,
	VIN int NOT NULL,
	PRIMARY KEY (client_id),
	FOREIGN KEY (client_id)
		REFERENCES clients (id),
	FOREIGN KEY (VIN)
		REFERENCES vehicles (VIN)
);

-- Problem 5
SELECT sale_date, make
FROM invoices LEFT OUTER JOIN VIN ON vehicles.VIN = VIN
WHERE (sale_date = date(2014))--sales date = 2014

-- Problem 6

CREATE VIEW total_makes_per_branch
SELECT COUNT * AS my_count
FROM vehicles
WHERE (branch_id = --given branch) 

-- Problem 7

CREATE TRIGGER insert_duplicat_record
AFTER INSERT ON vehicles
REFERENCING audit_table
FOR EACH ROW
update_duplicate_table()

CREATE TRIGGER delete_vehicle
AFTER DELETE ON vehicles
REFERENCES audit_table
FOR EACH ROW
update_duplicate_table

-- Problem 8
CREATE PROCEDURE no_problems

CURSOR duplicat_cursor
	SELECT VIN
	FROM audit_table 
	WHERE --marked as deleted

-- Problem 9

GRANT INSERT, UPDATE
ON audit
TO manager

GRANT SELECT
ON audit
TO PUBLIC

GRANT INSERT
ON invoices
TO sales

GRANT ALL PRIVILEGES
ON invoices
TO manager

GRANT SELECT
ON invoices
TO PUBLIC

GRANT INSERT, DELETE
ON vehicles
TO inventory

GRANT SELECT
ON total_makes_per_branch
TO inventory

GRANT --stored procedure
ON

-- Problem 10
-- 1NF
invoice (name, id, VIN)

-- invoice (first_name, last_name, VIN, sale_date, client_id, client_phone)