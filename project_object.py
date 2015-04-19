import psycopg2
con = psycopg2.connect(host='localhost', database='cs350', user='postgres', password='')
cur = con.cursor()

class College:
	""" Information about students, professors, courses, and departments"""

	def __init__(self, connection):
		self.connection = connection

	def add_student(self, info):
		"""Will allow the user to add a student to the students table."""

		with self.connection.cursor() as cur:
			cur.execute("""INSERT INTO students VALUES""", [info])

	def add_professor(self, info):
		""" Will allow the user to add a professor to the professors table."""

		with self.connection.cursor() as cur:
			cur.execute("""INSERT INTO professors VALUES""", [info])

	def add_course(self, info):
		""" Will allow the user to add a course to the courses table."""

		with self.connection.cursor() as cur:
			cur.execute("""INSERT INTO courses VALUES""", [info])

	def add_department(self, info):
		""" Will allow the user to add a department to the departments table."""

		with self.connection.cursor() as cur:
			cur.execute("""INSERT INTO courses VALUES""", [info])

	def add_major(self, info):
		""" Will allow the user to add a major to the majors table."""

		with self.connection.cursor() as cur:
			cur.execute("""INSERT INTO majors VALUES""", [info])

	def add_minor(self, info):
		""" Will allow the user to add a minor to the minors table."""

		with self.connection.cursor() as cur:
			cur.execute("""INSERT INTO minors VALUES""", [info])

	def view_student(self, student_id):
		""" Will allow the user to view a student from the table."""

		with self.connection.cursor() as cur:
			cur.execute("""SELECT * FROM students WHERE name = %s""", [student_id])

	def view_professor(self, professor_id):
		""" Will allow the user to view a professor from the table."""

		with self.connection.cursor() as cur:
			cur.execute("""SELECT * FROM students WHERE id = %s""", [professor_id])

	def view_course(self, course_id):
		""" Will allow the user to view a course from the courses table."""

		with self.connection.cursor() as cur:
			cur.execute("""SELECT * FROM students WHERE id = %s""", [course_id])

	def view_department(self, department_id):
		""" Will allow the user to viwe a department from the table."""

		with self.connection.cursor() as cur:
			cur.execute("""SELECT * FROM departments WHERE id = %s""", [department_id])

	def view_major(self, major_id):
		""" Will allow the user to view a major from the majors table."""

		with self.connection.cursor() as cur:
			cur.execute("""SELECT * FROM majors WHERE id = %s""", [major_id])

	def view_minor(self, minor_id):
		""" Will allow the user to view a minor from the minors table."""

		with self.connection.cursor() as cur:
			cur.execute("""SELECT * FROM minors WHERE id = %s""", [minor_id])

	def delete_student(self, student_id):
		""" Will allow the user to delete a student from the students table."""

		with self.connection.cursor() as cur:
			cur.execute("""DELETE * FROM students WHERE id = %s""", [student_id])

	def delete_professor(self, professor_id):
		""" Will allow the user to delete a professor from the professors table."""

		with self.connection.cursor() as cur:
			cur.execute("""DELETE * FROM professors WHERE id = %s""", [professor_id])

	def delete_course(self, course_id):
		""" Will allow the user to delete a course from the courses table."""

		with self.connection.cursor() as cur:
			cur.execute("""DELETE * FROM courses WHERE id = %s""", [course_id])

	def delete_department(self, department_id):
		""" Will allow the user to delete a department from the table."""

		with self.connection.cursor() as cur:
			cur.execute("""DELETE * FROM departments WHERE id = %s""", [department_id])

	def delete_major(self, major_id):
		""" Will allow the user to delete a major from the majors table."""

		with self.connection.cursor() as cur:
			cur.execute("""DELETE * FROM majors WHERE id = %s""", [major_id])

	def delete_minor(self, minor_id):
		""" Will allow the user to delete a minor from the minors table."""

		with self.connection.cursor() as cur:
			cur.execute("""DELETE * FROM minors WHERE id = %s""", [minor_id])

	def update_student(self, info):
		""" Will allow the user to enter the studnet's id and update that
		student in the student table."""

		with self.connection.cursor() as cur:
			cur.execute("""UPDATE students SET column = %s WHERE id = %s""", [info])

	def update_professor(self, info):
		""" Will allow the user to enter the professor's id and update that
		particular professor in the table."""

		with self.connection.cursor() as cur:
			cur.execute("""UPDATE professors SET column = %s WHERE id = %s""", [info])

	def update_course(self, info):
		""" Will allow the user to enter a course id and update that particular course."""

		with self.connection.cursor() as cur:
			cur.execute("""UPDATE courses SET column = %s WHERE id = %s""", [info])

	def update_department(self, info):
		""" Will allow the user to enter a department id and update that particular department."""

		with self.connection.cursor() as cur:
			cur.execute("""UPDATE departments SET column = %s WHERE id = %s""", [info])

	def update_major(self, info):
		""" Will allow the user to enter a major id and update a particular major."""

		with self.connection.cursor() as cur:
			cur.execute("""UPDATE majors SET column = %s WHERE id =%s""", [info])

	def update_minor(self, info):
		""" Will allow the user to enter a minor id and update a particular minor."""

		with self.connection.cursor() as cur:
			cur.execute("""UPDATE minors SET column = %s WHERE id =%s""", [info])

	