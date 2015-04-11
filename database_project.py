import psycopg2

connection = psycopg2.connection(host='hostname', database ='databasename', user='username', password='password')

cur = connection.cursor()

def del_professor():
	""" This function will allow the user to delete a professor from
	the professor table."""
	# first ask who to delete.
	# execute delete statement on the professor
	delete = ""
	str(delete)
	while delete != "":
		# delete the professor the user has entered



def update_department():
	""" The user will choose what department they would like to update."""
	
	update_department = ""
	str(update_department)
	while update_department != ''
pp
#update the professor part of the database
def update_professor():
	""" The user will be able to update a professor in the database."""

	update_professor = ""
	str(update_professor)
	while update_course != ''

# now update the courses part of the database
def update_course():
	""" The user will choose what course he or she wants to update in the courses part
	of the database."""
	update_course = ""
	str(update_course)
	# need to be able to see what courses i can search from.
	# how do i search for courses?
	while update_course != ''
		update_course = input('What course would you like to update?\n')
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
	str(update)
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
	str(first_action)
	while first_action = 'update' or 'add' or 'view' or 'delete':

		first_action = input('Would you like to add, update, view, or delete?')
		
		if first_action = 'add':
			# add what?
			pass
		elif first_action = 'update':
			# update what
			update_table()
		elif first_action = 'delete':
			# delete what
			pass
		elif first_action = 'view':
			# view what
			pass
		else:
			first_action()