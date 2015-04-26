import psycopg2
from project_object import *

command = ""
edit_table = ""

def main(database):
	""" The entire program collects data from the user."""

	while command != 'exit':

		print("Enter 'exit' to exit the program at any time.")

		first_action = input("Would you like to add, update, view, or delete?\n")
		first_action = first_action.lower()

		if first_action == 'add':
			edit_table = input("What table would you like to add to? 'Majors', 'Minors',"
				" 'Courses', 'Students', 'Professors', or 'Departments'?\n")
			edit_table = edit_table.lower()
	
			if edit_table == 'majors':
				info = []
				info.append(input("What is the name of the major?\n"))
				info.append(input("What is the id number of the major?\n"))
				info.append(input("What is the department number this major belongs to?\n"))
				# collect the information needed
				# run the add majors method
				info = info.lower()
				add_major()

			elif edit_table == 'minors':
				info = []
				info.append(input("What is the name of the minor?\n"))
				info.append(input("What is the id number of the minor?\n"))
				info.append(input("What is the department number this minor belongs to?\n"))
				info = info.lower()
				add_minor()

			elif edit_table == 'courses':
				info = []
				info.append("What is the time the course will run?\n")
				info.append("What is the id number of the course?\n")
				info.append("What is the name of the course?\n")
				info.append("What is the id number of the professor teaching the course?\n")
				info = info.lower()
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
				info = info.lower()

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
				info = []
				info.append(input("What is the degree the profesor has?\n"))
				info.append(input("What is the pay the profesor is earning?\n"))
				info.append(input("What is the last name of the professor?\n"))
				info.append(input("What is the first name of the professor?\n"))
				info.append(input("What is the id number of the professor?\n"))
				info.append(input("What is the department number the professor belogns to?\n"))
				info = info.lower()
				add_professor()

			elif edit_table == 'departments':
				info = []
				info.append(input("What is the department id number?\n"))
				info.append(input("What si the id of the director of the department?\n"))
				info.append(input("What is the name of the department?\n"))
				info = info.lower()
				add_department()

		elif first_action == 'update':
			edit_table = input("What table would you like to update? 'Majors,"
				" Minors, Courses, Students, Professors, or Departments?\n")
			edit_table = str.lower(edit_table)

			if edit_table == 'majors':
				info = []
				info.append(input("What major would you like to update?\n"))
				info.append(input("What column would you like to update? 'name', 'id', or 'department'?\n"))
				info.append(input("What would you like to change it to?\n"))
				info = info.lower()
				update_major()

			elif edit_table == 'minors':
				info = []
				info.append(input("What minor would you like to update?\n"))
				info.append(input("What column would you like to update? 'name', 'id', or 'department'?\n"))
				info.append(input("What would you like to change it to?\n"))
				info = info.lower()
				update_minors()

			elif edit_table == 'courses':
				info = []
				info.append(input("What course would you like to update?\n"))
				info.append(input("What column would you like to update? 'time, id, name, professor_id?\n"))
				info.append(input("What would you like to change it to?\n"))
				info = info.lower()
				update_course()

			elif edit_table == 'students':
				info = []
				info.append(input("Ener the id number of the student that you would "
					"like to update.\n"))
				info.append(input("What column would you like to update? 'first_name', "
					"'last_name', 'major01', 'major02', 'minor01', minor02', 'gpa', "
					"'id', 'graduation_year', 'advisor number', 'course01', "
					"'course02', 'course03', 'course04', 'course05', 'course06',"
					" course07', 'course08'\n"))
				info.append(input("What would you like to change it to?\n"))
				info = info.lower()
				update_student()

			elif edit_table == 'professors':
				info = []
				info.append(input("Enter the id number of the professor you would like to update\n"))
				info.append(input("What column would you like to update? 'degree', 'pay', "
					"'last_name, 'first_name', 'id', 'department_id'\n"))
				info.append(input("What would you like to change it to?\n"))
				info = info.lower()
				update_professor()

			elif edit_table == 'departments':
				update_department()

		elif first_action == 'view':
			edit_table = input("What table would you like to view? 'Majors', 'Minors',"
				" 'Courses', 'Students', 'Professors', or 'Departments'?\n")
			edit_table = edit_table.lower()

			if edit_table == 'majors':
				major_id = input("What is the id of the major you would like to view?\n"))
				major_id = int(major_id)
				# collect the information needed
				# run the add majors method
				view_major()
			elif edit_table == 'minors':
				minor_id = input("What is the id of the minor you would like to view?\n"))
				minor_id = int(minor_id)
				view_minor()
			elif edit_table == 'courses':
				course_id = input("What is the id of the course you would like to view?\n"))
				course_id = int(course_id)
				view_course()
			elif edit_table == 'students':
				student_id = input("What is the id of the student you would like to view?\n"))
				student_id = int(student_id)
				view_student()
			elif edit_table == 'professors':
				professor_id = input("What is the id of the professor you would like to view?\n"))
				professor_id = int(professor_id)
				view_professor()
			elif edit_table == 'departments':
				department_id = input("What is the id of the department you would like to view?\n"))
				department_id = int(department_id)
				view_department()

		elif first_action == 'delete':
			edit_table = input("What table would you like to view? 'Majors', 'Minors',"
			" 'Courses', 'Students', 'Professors', or 'Departments'?\n")
			edit_table = edit_table.lower()

			if edit_table == 'majors':
				major_id = input("What is the id of the major you would like to delete?\n"))
				major_id = int(major_id)
				# collect the information needed
				# run the add majors method
				delete_major()
			elif edit_table == 'minors':
				minor_id = input("What is the id of the minor you would like to delete?\n"))
				minor_id = int(minor_id)
				delete_minor()
			elif edit_table == 'courses':
				course_id = input("What is the id of the course you would like to delete?\n"))
				course_id = int(course_id)
				delete_course()
			elif edit_table == 'students':
				student_id = input("What is the id of the student you would like to delete?\n"))
				student_id = int(student_id)
				delete_student()
			elif edit_table == 'professors':
				professor_id = input("What is the id of the professor you would like to delete?\n"))
				professor_id = int(professor_id)
				delete_professor()
			elif edit_table == 'departments':
				department_id = input("What is the id of the department you would like to delete?\n"))
				department_id = int(department_id)
				delete_department()


if __name__ == '__main__':
	database = College(prompt_info())
	main()