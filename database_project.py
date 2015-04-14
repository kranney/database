import psycopg2
connection = psycopg2.connection(host='localhost', database ='cs350', user='kranney', password='kranney')
cur = con.cursor()

def print_null_statement():
	""" Will tell the user to print null if the user has no value to enter for a attribute."""

	print("If you do not have a value to enter please enter 'null'.\n")

def add_course():
	""" This will allow the user to add a course to the courses table."""

	print_null_statement()
	time = input("What is the time the course will run?\n")
	id_number = input("What is the id number of the course?\n")
	name = input("What is the name of the course?\n")
	professor_id = input("What is the id number of the professor teaching the course?\n")

	cur.execute(""" INSERT INTO courses VALUES time = %s, id = %s, name = %s, professor_id = %s""" 
		[time, id_number, name, professor_id])

def add_department():
	""" This will allow the user to add a department to the departments table."""

	print_null_statement()
	department_id = input("What is the department id number?\n")
	director_id = input("What is the id of the director of the department?\n")
	name = input("What is the name of the department?\n")

	cur.execute(""" INSERT INTO departments VALUES id = %s, director_id = %s, name = %s""" 
		[department_id, director_id, name])

def add_professor():
	""" This wll allow the user to add a professor to the professors table."""

	print_null_statement()
	degree = input("What is the degree the professor has?\n")
	pay = input("What is the pay the professor is earning?\n")
	last_name = input("What is the last name of the professor?\n")
	first_name = input("What is the first name of the professor?\n")
	professor_id = input("What is the id number of the professor?\n")
	department_id = input("What is the department number the professor belongs to?\n")

	cur.execute(""" INSERT INTO professors VALUES degree = %s, pay = %s, last_name = %s, first_name = %s, 
		id = %s, department_id = %s""" [degree, pay, last_name, first_name, professor_id, department_id])

def add_student():
	""" This will allow the user to add a student to the students table."""

	print_null_statement()
	first_name = input("What is the students first name?\n")
	middle_name = input("What is the students middle name?\n")
	last_name = input("What is the students last name?\n")
	major01 = input("What is the students first major?\n")
	major02 = input("What is the students second major?\n")
	minor01 = input("What is the students first minor?\n")
	minor02 = input("What is the students second minor?\n")
	gpa = input("What is the students current gpa?\n")
	id_number = input("What is the students id number?\n")
	graduation_year = input("What is the scheduled graduation year of the student?\n")
	advisor_number = input("What is the id number of the advisor of the student?\n")
	course01 = input("What is the first course id the student is taking?\n")
	course02 = input("What is the second course id the student is taking?\n")
	course03 = input("What is the third course id the student is taking?\n")
	course04 = input("What is the fourth course id the student is taking\n")
	course05 = input("What is the fifth course id the student is taking?\n")
	course06 = input("What is the sixth course id the student is taking?\n")
	course07 = input("What is the seventh course id the student is taking?\n")
	course08 = input("What is the eighth course id the student is taking?\n")

	cur.execute(""" INSERT INTO students VALUES first_name = %s, middle_name = %s, last_name = %s, 
		major01 = %s, major02 = %s, major03 = %s, major04 = %s, major05 = %s, major06 = %s, 
		major07 = %s, major08 = %s""" [first_name, middle_name, last_name, major01, major02,
		 major03, major04, major05, major06, major07, major08])


def add_minor():
	""" This function will allow the user to add a minor to the minors table."""

	print_null_statement()
	minor_name = input("What is the name of the minor?\n")
	minor_id = input("What is id number of the minor?\n")
	department_id = input("What is the department number this minor belongs to?\n")

	cur.execute(""" INSERT INTO minors VALUES name = %s, id = %s, department_id = %s""" [minor_name,
	 minor_id, department_id])

def add_major():
	""" This will allow the user to add a major to the majors table."""

	print_null_statement()
	major_name = input("What is the name of the major?\n")
	major_id = input("What is the id number of the major?\n")
	department_id = input("What is department number this major belongs to?\n")

	cur.execute(""" INSERT INTO majors VALUES name = %s, id = %s, department_id = %s"""
		 [major_name, major_id, department_id])

def add():
	""" This will allow the user to choose what database to add to."""

	table = ""

	while table != 'exit':
		table = input("Would you like to add to the 'courses', 'professors', 'students,'"
			" major, minor, or 'departments' table?\n")
		table = str(table)

		if table == 'courses':
			add_course()
		elif table == 'professors':
			add_professor()
		elif table == 'students':
			add_student()
		elif table == 'departments':
			add_department()
		elif table == 'minor':
			add_minor()
		elif table == 'major':
			add_major()

def view_minor():
	""" This will allow the user to view all of the details for a minor."""

	minor_name = input("Enter the name of the minor you would like to view.\n")
	cur.execute("""SELECT * FROM majors WHERE name = %s""" [minor_name])

def view_major():
	""" This will allow the user to view all of the details for a major."""

	major_name = input("Enter the name of the major you would like to view.\n")
	cur.execute("""SELECT * FROM majors WHERE name = %s""" [major_name])

def view_department():
	""" The user will be able to view details on a particular department."""

	department_name = input("Enter the name of the department you would like to view.\n")
	cur.execute("""SELECT * FROM departments WHERE name = %s""" [department_name])
	
def view_course():
	""" The user will be able to view details about a particular course."""

	course_name = input("Enter the name of the course you would like to view.\n")
	cur.execute("""SELECT * FROM courses WHERE name = %s""" [course_name])

# view details about a student
def view_student():
	""" This function will allow users to view details on a particular student."""

	student_id = input("Enter the id of the student you would like to view.\n")
	cur.execute("""SELECT * FROM students WHERE id = %s""" [student_id])


# view details about a professor
def view_professor():
	""" This function will allow the user to view the details about a particular
	professor."""

	professor_id = input("Enter the id of the professor you would like to view.\n")
	cur.execute("""SELECT * FROM professors WHERE id = %s""", [professor_id])

def view():
	" The user will be able to choose what table he/she would like to view."

	table = ''

	while table != 'exit':
		table = input("What table would you like to view? Choose from"
			" 'courses', 'students', 'professors', 'major', 'minor', or 'department'.")
		if table == 'courses':
			view_course()
		elif table == 'students':
			view_student()
		elif table == 'professors':
			view_professor()
		elif table == 'department':
			view_department()

def delete_department():
	""" This function will allow the user to delete a department from the departments table."""

	delete_department = input("What department would you like to entirely delete?\n")

	cur.execute(""" DELETE * FROM departments WHERE name = %s""", [delete_department])

def delete_course():
	""" This function will allow the user to delete a course from the course table"""

	delete_course = input("Enter the course id of the course that you would like to delete?\n")

	cur.execute("""DELETE * FROM courses WHERE id = %s""", [delete_course])

def delete_minor():
	""" This function will allow the user to delete an entire minor and all of its attributes."""

	minor_name = input('What major would you like to delete?')

	cur.execute("""DELETE * FROM minors WHERE name = %s""",[minor_name])

def delete_major():
	""" This function will allow the user to delete an entire major and all of its attributes."""

	major_name = input('What major would you like to delete?')

	cur.execute("""DELETE * FROM majors WHERE name = %s""",[major_name])

def delete_student():
	"""This function will allow the user to delete a student form the students table"""

	delete_student = input("Enter the student id of the student that you would like to delete.\n")

	cur.execute("""DELETE * FROM students WHERE id = %s""", [delete_student])
		

def delete_professor():
	""" This function will allow the user to delete a professor from
	the professor table."""
	
	delete_professor = input("Enter the id number of the professor that you would like to delete.\n")

	cur.execute("""DELETE * FROM professors WHERE id = %s""", [delete_professor])

def delete():
	""" This will prompt the user to choose what table to delete information from."""

	table = ''

	while table != 'exit':
		table = input('What would you like to delete?' " A 'student', 'professor',"
			" 'department' 'major', 'minor' or a 'course'?")

		if table == 'student':
			delete_student()
		elif table == 'professor':
			delete_professor()
		elif table == 'department':
			delete_department()
		elif table == 'course':
			delete_course()
		else:
			delete()

def update_minor():
	""" The user will be able to choose what minor he/she would like to update."""

	# first i choose what table to update # i choose number
	# i want to change the name # 
	# change name to llama
	# 

	minor = input("What minor would you like to update?\n")
	column = input("What column would you like to update? name, id, or department_id")
	new_attribute = input("What would you like to change it to?")

	cur.execute("""UPDATE majors SET column = %s WHERE name = %s""", [new_attribute, name])


def update_major():
	""" The user will be able to choose what major he/she would like to update."""

	# first i choose what table to update # i choose number
	# i want to change the name # 
	# change name to llama
	# 

	major = input("What major would you like to update?\n")
	column = input("What column would you like to update? name, id, or department_id")
	new_attribute = input("What would you like to change it to?")

	cur.execute("""UPDATE majors SET column = %s WHERE name = %s""", [new_attribute, major])


def update_student():
	""" The user will be able to choose what student he/she would like to update."""

	student = input("Enter the id of the student that you would like to update.\n")
	column = input("What column would you like to update? first name?, middle name, "
		"last name, major01, major02, minor01, minor02, gpa, id number, graduation_year"
		" advisor number, couse01, course02, course03, course04, course05, course06 "
		"course07, course08")
	new_attribute = input("What would you like to change it to?\n")

	cur.execute("""UPDATE students SET column = %s WHERE name = %s""", [new_attribute])

def update_department():
	""" The user will choose what department they would like to update."""
	
	department = ""
	
	while department != 'exit':
		department = input("What department would you like to update?")
		department = str(department)
		# what attribute to update about the particular department.

#update the professor part of the database
def update_professor():
	""" The user will be able to update a professor in the database."""

	professor = ""
	
	while course != 'exit':
		professor = input("What professor would you like to update?")
		professor = str(professor)
		pass
		# update the professor
		# choose what to update about the particular professor

# now update the courses part of the database
def update_course():
	""" The user will choose what course he or she wants to update in the courses part
	of the database."""
	update_course = ""
	
	# need to be able to see what courses i can search from.
	# how do i search for courses?
	while update_course != 'exit':
		update_course = input('What course would you like to update?\n')
		update_course = str(update_course)
		pass
		# provide options of what course to update or search for a course name
		# how do i do that?
		# then run an update statement in sql and tell the database to update
		# a particular course attribute

# what would you like to update?
def update_table():
	""" Will allow the user to choose what they will want to update. 
	User can choose from different tables. Tables will be courses,
	professors, department, and students."""

	update = ""
	
	while update != 'exit':
		
		update = input('Would you like to update courses, professors, department, or students?\n')
		update = str(update)

		if update == 'courses':
			update_course()
		elif update == 'professors':
			# go update professors table
			update_professor()
		elif update == 'department':
			# go update department table
			update_department
		elif update == 'students':
			# go update students table
			up
		else:
			update_table()



def first_action():
	""" This is the first actiont the user will have. The user will choose if he/she would like to
	add, update, view, or delete something."""

	first_action = ""
	
	while first_action != 'exit':

		first_action = input('Would you like to add, update, view, or delete?')
		first_action = str(first_action)
		
		if first_action == 'add':
			add()
		elif first_action == 'update':
			# update what
			update_table()
		elif first_action == 'delete':
			delte()
			pass
		elif first_action == 'view':
			# view what
			view_table()
		else:
			first_action()

# start the program
first_action()