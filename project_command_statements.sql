INSERT INTO students 
VALUES ('Kyle', 'Jacob', 'Ranney', 'insurance', NULL, 3.22, 93988, NULL, NULL, 2016, 'Breed')

INSERT INTO students
VALUES (first_name, middle_name, last_name, major01, major02, gpa, id, minor01, minor02, graduation year, advisor)

INSERT INTO professors
VALUES (degree, pay, last_name, first_name, id, department_id)

INSERT INTO departments
VALUES (id, director_id, majors, name, minors, professor_id)

INSERT INTO courses
VALUES (time, id, name, number_of students, professor_id)

DELETE *
FROM students
WHERE id = student

DELETE *
FROM professors
WHERE id = delete_professor

DELETE *
FROM courses
WHERE id = delete_course

DELETE *
FROM departments
WHERE id = delete_department

UPDATE students
SET column = new_attribute
WHERE id = student

UPDATE professors
SET column = new_attribute
WHERE id = professor

UPDATE courses
SET column = new_attribute
WHERE id = course

UPDATE department
SET column = new_attribute
WHERE id = department

SELECT * 
FROM students
WHERE id = student_id

SELECT *
FROM professors
WHERE id = professor_id

SELECT *
FROM departments
WHERE id = department_id

SELECT *
FROM courses
WHERE id = course_id

SELECT *
FROM majors
WHERE name = major_name

SELECT *
FROM minors
WHERE name = minor_name

DELETE *
FROM majors
WHERE name = -major_name

DELETE *
FROM minors
WHERE name = minor_name

UPDATE majors
SET column = new_attribute -- column and new_attribute are both set by the user
WHERE name = major_name

UPDATE minors
SET column = new_attribute -- column and new_attribute are both set by the user
WHERE name = minor_name

SELECT department.name, major.name
FROM department, majors
WHERE major.department_id = department.id

-- count how many students are in a course
