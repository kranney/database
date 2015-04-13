CREATE TABLE courses
(
	time char(16) NOT NULL,
	id int NOT NULL,
	name varchar(100) NOT NULL,
	number_of_students int NOT NULL,
	professor_id int NOT NULL,
	PRIMARY KEY (number, name),
	FOREIGN KEY (professor_id)
		REFERENCES professors (id)
	CHECK (number > 0 AND number_of_students > 0)
	
);

CREATE TABLE professors
(
	degree varchar(50) NOT NULL,
	pay money NOT NULL,
	last_name varchar(250) NOT NULL,
	first_name varchar(250) NOT NULL,
	id int NOT NULL,
	department_id varchar(250) NOT NULL,
	PRIMARY KEY (full_name, number),
	FOREIGN KEY (department_id)
		REFERENCES departments (id)
	CHECK (id > 0 AND department_id > 0)
);

CREATE TABLE departments
(
	id int NOT NULL,
	director_id int, -- will have a name from professors
	name varchar(50) NOT NULL,
	PRIMARY KEY (majors, name, minors),
	FOREIGN KEY (professor_id)
		REFERENCES professors (id)
	FOREIGN KEY (director_id)
		REFERENCES professors (id)
	CHECK (id > 0 AND professor_id > 0)
);

CREATE TABLE students
(
	first_name varchar(250) NOT NULL,
	middle_name varchar(250) NOT NULL,
	last_name varchar(250) NOT NULL,
	major01 varchar(50) NOT NULL, --foreign key
	major02 varchar(50),
	minor01 varchar(50), --foreign key could be null
	minor02 varchar(50), --foregin key could be null
	gpa number NOT NULL,
	id int NOT NULL,
	graduation_year int NOT NULL,
	advisor_number int NOT NULL,
	course_id01 int NOT NULL,
	course_id02 int,
	course_id03 int,
	course_id04 int,
	course_id05 int,
	course_id06 int,
	course_id07 int,
	course_id08 int,
	PRIMARY KEY (number),
	FOREIGN KEY (advisor_number)
		REFERENCES professors (id)
	FOREIGN KEY (course_id01, course_id02, course_id03, course_id04, course_id05, course_id06, course_id07,course_id08)
		REFERENCES courses (id)
	CHECK (id > 0 AND graduation_year > 1860 AND advisor_number > 0)
);

CREATE TABLE professors_courses
(
	professor_id int NOT NULL,
	course_id int NOT NULL,
	FOREIGN KEY (professor_id)
		REFERENCES professors (id)
	FOREIGN KEY (course_id)
		REFERENCES courses (id)
	CHECK (professor_id > 0 AND course_id > 0)
);

CREATE TABLE majors
(
	name varchar(250) NOT NULL,
	id int NOT NULL,
	department_id int NOT NULL,
	PRIMARY KEY (name, id, department_id),
	FOREIGN KEY (department_id)
		REFERENCES departments (id)
	CHECK (id > 0)
);

CREATE TABLE minors
(
	name varchar(250) NOT NULL,
	id int NOT NULL,
	department_id int NOT NULL,
	PRIMARY KEY (name, id),
	FOREIGN KEY (department_id)
		REFERENCES departments (id)
	CHECK (id > 0)
);