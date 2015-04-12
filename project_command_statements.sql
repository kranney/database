INSERT INTO students 
VALUES ('Kyle', 'Jacob', 'Ranney', 'insurance', NULL, 3.22, 93988, NULL, NULL, 2016, 'Breed')

INSERT INTO students
VALUES -- all user entered
--(first_name, middle_name, last_name, major01, major02, gpa, id, minor01, minor02, graduation year, advisor)

INSERT INTO professors
VALUES -- all user entered
-- (degree, pay, last_name, first_name, id, department_id)

INSERT INTO departments
VALUES -- all user entered
-- (id, director_id, majors, name, minors, professor_id)

INSERT INTO courses
VALUES -- all user entered
-- time, id, name, number_of students, professor_id

DELETE *
FROM students
WHERE id = --the variable the user puts (student)

DELETE *
FROM professors
WHERE id = -- professor

DELETE *
FROM courses
WHERE id = -- course

DELETE *
FROM departments
WHERE id = -- department

UPDATE students
SET column = new_attribute
WHERE id = -- student

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
WHERE id = -- the id the user entered

SELECT *
FROM professors
WHERE id = -- the id the user entered

SELECT *
FROM departments
WHERE id = -- the id the user entered

SELECT *
FROM courses
WHERE id = -- the id the user entered