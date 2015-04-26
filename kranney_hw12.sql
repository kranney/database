--18.4

--The physical database is the process of producing a description of the implementation of the database. 
--It will describe the relations and storage stuctures. The physical database is concerned with the how. 
--The logical database design is concerned with the what. The conceptual model expalins what tables will have what.
CREATE TABLE supervisor
(
	name varchar(250) NOT NULL,
	id INT NOT NULL,
	address varchar(250) NOT NULL,
	position varchar(250) NOT NULL,
	salary money NOT NULL,
	assistant01 varchar(250),
	assistant02 varchar(250),
	assistant03 varchar(250),
	assistant04 varchar(250),
	assistant05 varchar(250),
	assistant06 varchar(250),
	assistant07 varchar(250),
	assistant08 varchar(250),
	assistant09 varchar(250),
	assistant10 varchar(250)
	--PRIMARY KEY (id),
	--FOREIGN KEY (assistant01, assistant02, assistant03, assistant04, assistant04, 
	--	assistant05, assistant06, assistant07, assistant08, assistant09, assistant10)
	--	REFERENCES member (name)
);

CREATE TABLE member
(
	id INT NOT NULL,
	name varchar(250) NOT NULL,
	address varchar(250) NOT NULL,
	position varchar(250) NOT NULL,
	salary money NOT NULL,
	supervisor_name varchar(250) NOT NULL,
	branch_details varchar(500),
	PRIMARY KEY (id),
	FOREIGN KEY (supervisor_name)
		REFERENCES supervisor (name)
);

CREATE TABLE manager
(
	id INT NOT NULL,
	name varchar(250) NOT NULL,
	address varchar(250) NOT NULL,
	position varchar(250) NOT NULL,
	salary money NOT NULL,
	date_started varchar(50) NOT NULL,
	bouns_pay money,
	PRIMARY KEY (id)
);

CREATE TABLE branch
(
	id INT NOT NULL,
	address varchar(250) NOT NULL,
	telephone01 varchar(15) NOT NULL,
	telephone02 varchar(15) NOT NULL,
	telephone03 varchar(15) NOT NULL,
	manager_id int NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (manager_id)
		REFERENCES manger (id)
);

CREATE TABLE property_for_rent
(
	id int NOT NULL,
	address varchar(250) NOT NULL,
	type varchar(50) NOT NULL,
	number_of_room int NOT NULL,
	monthly_rent money NOT NULL,
	owner_details varchar(250),
	manager_id INT NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE property_owner
(
	id INT NOT NULL,
	name varchar(250) NOT NULL,
	address varchar(250) NOT NULL,
	phone varchar(15) NOT NULL,
	email varchar(250) NOT NULL,
	password varchar(25) NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE client
(
	id INT NOT NULL,
	name varchar(250) NOT NULL,
	phone varchar(15) NOT NULL,
	email varchar(250),
	preferred_accommodation varchar(250) NOT NULL,
	max_rent money NOT NULL,
	date_joined date NOT NULL,
	branch_details varchar(500),
	PRIMARY KEY (id)
);

CREATE TABLE leases
(
	id INT NOT NULL,
	client_id INT NOT NULL,
	name varchar(250) NOT NULL,
	address varchar(250) NOT NULL,
	property_id INT NOT NULL,
	monthly_rent money NOT NULL,
	payment_method varchar(100) NOT NULL,
	deposit_paid INT NOT NULL,
	lease_duration varchar(50) NOT NULL,
	start_date date NOT NULL,
	end_date date,
	PRIMARY KEY (id),
	FOREIGN KEY (property_id)
		REFERENCES property (id)
);

CREATE TABLE property_details
(
	id INT NOT NULL,
	address varchar(250) NOT NULL,
	type varchar(50) NOT NULL,
	number_rooms int NOT NULL,
	rent money NOT NULL,
	date_advertised date NOT NULL,
	newspaper_name varchar(250) NOT NULL,
	cost money NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (newspaper_name)
		REFERENCES newspaper (newspaper_name)
);

CREATE TABLE newspaper
(
	name varchar(250) NOT NULL,
	address varchar(250) NOT NULL,
	phone varchar (15) NOT NULL,
	contact_name varchar(250) NOT NULL,
	PRIMARY KEY (phone)
);

CREATE TABLE students 
(
	banner_id int NOT NULL,
	first_name varchar(250) NOT NULL,
	last_name varchar(250) NOT NULL,
	street varchar(250) NOT NULL,
	city varchar(250) NOT NULL,
	postcode int,
	mobile_phone varchar(15) NOT NULL,
	email varchar(250) NOT NULL,
	date_of_birth date NOT NULL,
	gender char(1) NOT NULL,
	class_standing int NOT NULL,
	nationality varchar(250) NOT NULL,
	special_needs char(1) NOT NULL,
	status varchar(250) NOT NULL,
	major01 varchar(250) NOT NULL,
	major02 varchar(250) NOT NULL,
	minor01 varchar(250) NOT NULL,
	minor02 varchar(250) NOT NULL,
	advisor varchar(250) NOT NULL,
	room int,
	PRIMARY KEY (banner_id)
);

CREATE TABLE advisors
(
	first_name varchar(250) NOT NULL,
	last_name varchar(250) NOT NULL,
	position varchar(250) NOT NULL,
	department_name varchar(250) NOT NULL,
	internal_phone varchar(15) NOT NULL,
	email varchar(250) NOT NULL,
	office_id int,
	PRIMARY KEY (email),
	ALTERNATE KEYS (office_id, internal_phone)
);

CREATE TABLE email
(
	id int,
	last_name varchar(250) NOT NULL,
	first_name varchar(250) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (last_name, first_name)
		REFERENCES students (last_name, first_name)
);

CREATE TABLE hall_of_residence
(
	name varchar(250) NOT NULL,
	address varchar(250) NOT NULL,
	telephone_number varchar(15) NOT NULL,
	hall_manager varchar(250) NOT NULL,
	PRIMARY KEY (name)
);

CREATE TABLE room
(
	id int,
	place_id int,
	rent money,
	PRIMARY KEY (id)
);

CREATE TABLE apartments
(
	holds_number_of_students int,
	id int,
	address varchar(250) NOT NULL,
	singles_available int,
	flat_id int,
	PRIMARY KEY (id)
);

CREATE TABLE leases
(
	id int,
	price money,
	duration int,
	student_first_name varchar(250) NOT NULL,
	student_last_name varchar(250) NOT NULL,
	banner_id int,
	place_id int,
	room_id int,
	address_details varchar(250) NOT NULL,
	enter_date date,
	leave_date date,
	PRIMARY KEY (id),
	FOREIGN KEY (student_first_name, student_last_name)
		REFERENCES students(first_name, last_name)
);

CREATE TABLE invoice
(
	id int,
	lease_id int,
	semester varchar(250) NOT NULL,
	payment_due date,
	student_last_name varchar(250) NOT NULL,
	student_first_name varchar(250) NOT NULL,
	banner_id int,
	place_id int,
	room_id int,
	hall_address varchar(250) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (lease_id)
		REFERENCES leases (lease_id),
	FOREIGN KEY (student_last_name, student_first_name, banner_id)
		REFERENCES students (last_name, first_name, banner_id),
	FOREIGN KEY (place_id, room_id)
		REFERENCES room (place_id, id)
);

CREATE TABLE inspection
(
	id int,
	inspector varchar(250) NOT NULL,
	date date,
	satisfactory_condition char(1) NOT NULL,
	comments varchar(250) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (inspector)
		REFERENCES hall_of_residence (hall_manager)
);

CREATE TABLE residence_staff
(
	id int,
	first_name varchar(250) NOT NULL,
	last_name varchar(250) NOT NULL,
	email varchar(250) NOT NULL,
	street varchar(250) NOT NULL,
	city varchar(250) NOT NULL,
	postcode int,
	dob date,
	gender char(1),
	position varchar(250) NOT NULL,
	location varchar(250) NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE courses
(
	id int,
	title varchar(250) NOT NULL,
	year int,
	instructor varchar(250) NOT NULL,
	instructor_phone_number varchar(15) NOT NULL,
	email varchar(250) NOT NULL,
	room_id int,
	department_name varchar(250) NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE professors
(
	first_name varchar(250) NOT NULL,
	last_name varchar(250) NOT NULL,
	id int,
	email varchar(250) NOT NULL,
	courses varchar(250) NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE professor_courses
(
	course_id int,
	professor_id int,
	PRIMARY KEY (course_id)
);

CREATE TABLE staff
(
	id int,
	name varchar(250) NOT NULL,
	phone_extension int,
	PRIMARY KEY (id)
);

CREATE TABLE space
(
	id int,
	PRIMARY KEY (id)
);

CREATE TABLE parking_lot
(
	name varchar(250) NOT NULL,
	location varchar(250) NOT NULL,
	capacity varchar(250) NOT NULL,
	number_of_floors int,
	PRIMARY KEY (name)
);

CREATE TABLE test
(
	date date,
	visitor_license_id int,
	PRIMARY KEY (visitor_license_id)
)