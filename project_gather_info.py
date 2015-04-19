command = ""
edit_table = ""

while command != 'exit':

	print("Enter 'exit' to exit the program at any time.")

	first_action = input("Would you like to add, update, view, or delete?\n")
	first_action = str.lower(first_action)

	if first_action == 'add':
		edit_table = input("What table would you like to add to? 'Majors', 'Minors',"
			" 'Courses', 'Students', 'Professors', or 'Departments'?")
		edit_table = str.lower(edit_table)

		if edit_table == 'majors':
			# collect the information needed
			# run the add majors method
			add_major()
		elif edit_table == 'minors':
			add_minor()
		elif edit_table == 'courses':
			info = []
			info.append("What is the time the course will run?\n")
			info.append("What is the id number of the course?\n")
			info.append("What is the name of the course?\n")
			info.append("What is the id number of the professor teaching the course?\n")
			add_course()
		elif edit_table == 'students':
			info = []
			info.append(input("What is the students first name?\n"))
			info.append(input("What is the students middle name?\n"))
			info.append(input("What is the students last name?\n"))
			info.append(input("What is the students first major?\n"))
			info.append(input("What is the students second major?\n"))
			info.append(input("What is the students first minor?\n"))
			info.append(input("What is the students second minor?\n"))
			info.append(input("What is the students current gpa?\n"))
			info.append(input("What is the students id number?\n"))
			info.append(input("What is the scheduled graduation year of the student?\n"))
			info.append(input("What is the id number of the advisor of the student?\n"))

			for item in range(8):
			    course = input('Course {} id: '.format(item))
			    if course.isdigit():
			        info.append(int(course))
			    else:
			        for num in range(8-item):
			            info.append(None)
			        break

	info.append(int(input('Course {} id:'.format(item))))))
			add_student()
		elif edit_table == 'professors':
			add_professor()
		elif edit_table == 'departments':
			add_department()

	elif first_action == 'update':
		edit_table = input("What table would you like to update? 'Majors,"
			" Minors, Courses, Students, Professors, or Departments?")
		edit_table = str.lower(edit_table)

		if edit_table == 'majors':
			update_major()
		elif edit_table == 'minors':
			update_minors()
		elif edit_table == 'courses':
			update_course()
		elif edit_table == 'students':
			update_student()
		elif edit_table == 'professors':
			update_professor()
		elif edit_table == 'departments':
			update_department()

	elif first_action == 'view':
		edit_table = input("What table would you like to view? 'Majors', 'Minors',"
			" 'Courses', 'Students', 'Professors', or 'Departments'?")
		edit_table = str.lower(edit_table)

		if edit_table == 'majors':
			# collect the information needed
			# run the add majors method
			view_major()
		elif edit_table == 'minors':
			view_minor()
		elif edit_table == 'courses':
			view_course()
		elif edit_table == 'students':
			view_student()
		elif edit_table == 'professors':
			view_professor()
		elif edit_table == 'departments':
			view_department()

	elif first_action == 'delete':
		edit_table = input("What table would you like to view? 'Majors', 'Minors',"
		" 'Courses', 'Students', 'Professors', or 'Departments'?")
		edit_table = str.lower(edit_table)

		if edit_table == 'majors':
			# collect the information needed
			# run the add majors method
			delete_major()
		elif edit_table == 'minors':
			delete_minor()
		elif edit_table == 'courses':
			delete_course()
		elif edit_table == 'students':
			delete_student()
		elif edit_table == 'professors':
			delete_professor()
		elif edit_table == 'departments':
			delete_department()