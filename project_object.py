import psycopg2
con = psycopg2.connect(host='localhost', database='cs350', user='postgres', password='')
cur = con.cursor()

class College:
	""" Information about students, professors, courses, and departments"""

	def __init__(self, cur)