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
			cur.execute("""INSERT INTO students VALUES""", info)

	def add_professor(self, info):
		""" Will allow the user to add a professor to the professors table."""

		with self.connection.cursor() as cur:
			cur.execute("""INSERT INTO professors VALUES""", info)

	def add_course(self, info):
		""" Will allow the user to add a course to the courses table."""

		with self.connection.cursor() as cur:
			cur.execute("""INSERT INTO courses VALUES""", info)

	def add_department(self, info):
		""" Will allow the user to add a department to the departments table."""

		with self.connection.cursor() as cur:
			cur.execute("""INSERT INTO courses VALUES""", info)

	def view_