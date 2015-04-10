def update_department():
	""" The user will choose what department they would like to update."""
	
	update_department = ""
	str(update_department)
	while update_department != ''

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
def update_section():
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
			update_section()

update_section()