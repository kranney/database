import psycopg2

# need to import my sql file

connection = psycopg2.connection(host='cs350', database ='kranney_project', user='kranney', password='password')

cur = connection.cursor()

# view details about a student
def view_student():
	""" This function will allow users to view details on a particular student."""

	# prompt user what student to view
	student = ""

	while student != 'exit':
		student = input('What student would you like to view details on?'
			"Enter 'exit' to exit")
		#user will then enter a students name
		# what if they get the wrong name
		# use the student variable in the select statment
		# is the user entering an integer or a string?
		# make it up to me or have them choose.
		if student == int:
			# search using the student's id_number
			pass
		elif student == str:
			# search using the students last name
			pass
		else:
			# start back over
			view_student()


# view details about a professor
def view_professor():
	""" This function will allow the user to view the details about a particular
	professor."""

	# first search for the professor?
	# enter the professors name
	# present all the details on the present?

	professor = ""

	while view != "exit":
		# enter the professors name that you would like to view the details on
		professor = input('What professor would you like to view?')
		# select the professor from the table

def del_professor():
	""" This function will allow the user to delete a professor from
	the professor table."""
	# first ask who to delete.
	# execute delete statement on the professor
	delete = ""
	
	while delete != "exit":
		# how will the user know what professor to enter?
		# what happens when the user enters the wrong name?
		# somehow search the table for the professor name?
		# delete the professor the user has entered
		pass


def update_department():
	""" The user will choose what department they would like to update."""
	
	update_department = ""
	
	while update_department != 'exit':
		pass

#update the professor part of the database
def update_professor():
	""" The user will be able to update a professor in the database."""

	update_professor = ""
	
	while update_course != 'exit':
		pass

# now update the courses part of the database
def update_course():
	""" The user will choose what course he or she wants to update in the courses part
	of the database."""
	update_course = ""
	
	# need to be able to see what courses i can search from.
	# how do i search for courses?
	while update_course != 'exit':
		update_course = input('What course would you like to update?\n')
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
	
	while update != 'courses' or 'professors' or 'department' or 'students':
		update = input('Would you like to update courses, professors, department, or students?\n')

		if update == 'courses':
			update_course()
		elif update == 'professors':
			# go update professors table
			pass
		elif update == 'department':
			# go update department table
			pass
		elif update == 'students':
			# go update students table
			pass
		else:
			update_table()

update_table()

def first_action():
	first_action = ""
	
	while first_action != 'exit':

		first_action = input('Would you like to add, update, view, or delete?')
		
		if first_action == 'add':
			# add what?
			pass
		elif first_action == 'update':
			# update what
			update_table()
		elif first_action == 'delete':
			# delete what
			pass
		elif first_action == 'view':
			# view what
			pass
		else:
			first_action()