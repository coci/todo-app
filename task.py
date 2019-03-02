import sqlite3

try :
	conection = sqlite3.connect('todo.db')
except error as e:
	print(e)

class Task(object):
	"""docstring for Task"""
	def __init__(self, title, id):
		self.title = title
		self.id = id
		self.state = 'pending' # pending, done, deleted


	def create(self):
		try:
			cursor = conection.cursor()
			cursor.execute("insert into all_task (task, state) values (?,?)", (self.title,self.state))
			conection.commit()
			conection.close()
			print("Task successfult added .")
		except Error as e:
			print(e)



	def update(self):
		conection = sqlite3.connect('todo.db')
		cursor = conection.cursor()
		cursor.execute("UPDATE all_task SET task='%s' WHERE rowid = %s"%(self.title,self.id))
		conection.commit()
		print("task successfully updated and here is approval :")
		cursor.execute("SELECT rowid,task,state FROM all_task WHERE rowid = %s"%(self.id))
		rows = cursor.fetchall()
		conection.close()
		return rows

	def done(self):
		conection = sqlite3.connect('todo.db')
		cursor = conection.cursor()
		cursor.execute("UPDATE all_task SET state= 'done' WHERE rowid = %s"%(self.id))
		conection.commit()
		print("task successfully has been done and here is approval :")
		cursor.execute("SELECT rowid,task,state FROM all_task WHERE rowid = %s"%(self.id))
		rows = cursor.fetchall()	
		conection.close()
		return rows

	def delete(self):
		cursor = conection.cursor()
		cursor.execute("DELETE FROM all_task WHERE rowid = %s"%(self.id))
		conection.commit()
		conection.close()

		
	@staticmethod
	def delete_all():
		cursor = conection.cursor()
		cursor.execute("DELETE FROM all_task")
		conection.commit()
		conection.close()
		print("All task are successfully deleted")

	@staticmethod
	def get_all():
		try:
			cursor = conection.cursor()
			cursor.execute("SELECT rowid,task,state FROM all_task")
			rows = cursor.fetchall()
			return rows	
		except Error as e:
			print(e)
