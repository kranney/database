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
	CHECK (number < 0 AND number_of_students > 0)
	
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
);

CREATE TABLE departments
(
	id int NOT NULL,
	director_id int, -- will have a name from professors
	majors varchar(50) NOT NULL,
	name varchar(50) NOT NULL,
	minors varchar(50) NOT NULL,
	professor_id int NOT NULL,
	PRIMARY KEY (majors, name, minors),
	FOREIGN KEY (professor_id)
		REFERENCES professors (id)
	FOREIGN KEY (director_id)
		REFERENCES professors (id)
);

CREATE TABLE students
(
	first_name varchar(250) NOT NULL,
	middle_name varchar(250) NOT NULL,
	last_name varchar(250) NOT NULL,
	major01 varchar(50) NOT NULL, --foreign key
	major02 varchar(50),
	gpa number NOT NULL,
	id int NOT NULL,
	minor01 varchar(50), --foreign key could be null
	minor02 varchar(50), --foregin key could be null
	graduation_year int NOT NULL,
	advisor_number int NOT NULL,
	PRIMARY KEY (number),
	FOREIGN KEY (advisor_number)
		REFERENCES professors (number)
);

CREATE TABLE professors_courses
(
	professor_id int NOT NULL,
	course_id int NOT NULL,
	FOREIGN KEY (professor_id)
		REFERENCES professors (id)
	FOREIGN KEY (course_id)
		REFERENCES courses (id)
);

CREATE TABLE majors
(
	name varchar(250) NOT NULL,
	id int NOT NULL,
	department_id int NOT NULL,
	PRIMARY KEY (name, id, department_id),
	FOREIGN KEY (department_id)
		REFERENCES departments (id)
);

CREATE TABLE minors
(
	name varchar(250) NOT NULL,
	id int NOT NULL,
	department_id int NOT NULL,
	PRIMARY KEY (name, id),
	FOREIGN KEY (department_id)
		REFERENCES departments (id)
);