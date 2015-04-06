CREATE TABLE courses
(
	time char(16) NOT NULL,
	number int NOT NULL PRIMARY KEY,
	name varchar(100) NOT NULL PRIMARY KEY,
	counts_to_majors varchar(200) NOT NULL,
	number_of_students int NOT NULL,
	CHECK (number < 0)
	CHECK (number_of_students > 0)
);

CREATE TABLE professors
(
	degree varchar(50) NOT NULL,
	pay money NOT NULL,
	full_name varchar(250) NOT NULL,
	number int NOT NULL,
	department
	PRIMARY KEY (full_name, number)
);

CREATE TABLE department
(
	director varchar, -- will have a name from professors
	majors varchar(50) NOT NULL PRIMARY KEY,
	name varchar(50) NOT NULL PRIMARY KEY,
	minors varchar(50) NOT NULL PRIMARY KEY,
	professors, -- foreign key and primary key NOT NULL
	PRIMARY KEY (majors, name, minors)
	FOREIGN KEY (professors)
		REFERENCES professors (full_name)
);

CREATE TABLE students
(
	major01 varchar(50) NOT NULL, --foreign key
	major02 varchar(50)
	gpa int char(4) NOT NULL,
	number int NOT NULL PRIMARY KEY,
	minor01 varchar(50), --foreign key could be null
	minor02 varchar(50), --foregin key could be null
	graduation_year int NOT NULL,
	advisor varchar(250) NOT NULL, --foreign key
	PRIMARY KEY (number)
	FOREIGN KEY (major01, major02, minor01, minor02)
		REFERENCES courses (major01, major02, minor01)
	FOREIGN KEY (advisor)
		REFERENCES professors (full_name)
);

