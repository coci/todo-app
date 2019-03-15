import sqlite3
import requests


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
		
		data = {
				'task' : self.title,
				'userid' : userid
		}
		req = requests.post('http://api.imgod.ir/todo/task/add',data=data).json()
		parse_json = req
		print(parse_json['message'])
		

	def update(self) -> list:
		conection = sqlite3.connect('todo.db')
		cursor = conection.cursor()
		cursor.execute("UPDATE all_task SET task='%s' WHERE rowid = %s"%(self.title,self.id))
		conection.commit()
		print("task successfully updated and here is approval :")
		cursor.execute("SELECT rowid,task,state FROM all_task WHERE rowid = %s"%(self.id))
		rows = cursor.fetchall()
		conection.close()
		return rows

	def done(self) -> list:
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
	def get_all() -> list:
		try:
			cursor = conection.cursor()
			cursor.execute("SELECT rowid,task,state FROM all_task")
			rows = cursor.fetchall()
			return rows	
		except Error as e:
			print(e)

class User(object):
	"""docstring for user"""
	def __init__(self, username,password,email,token):
		self.username = username
		self.password = password
		self.email = email
		self.token = token

	def register(self):
		data = {
				'username':self.username,
				'password':self.password,
				'email':self.email
		}

		req = requests.post('http://api.imgod.ir/todo/register/register',data=data).json()
		parse_json = req
		print(parse_json[0]['message'])

	def login(self):
		data = {
				'username':self.username,
				'password':self.password,
		}
		req = requests.post('http://api.imgod.ir/todo/login/login',data=data).json()
		json = req
		if json['message'] == 'user found':
			print('user found . your now loging')
			return json['tokenn'][0]['token']
		if 	json['message'] == 'user not found':
			print("user not found")
	

	def check(self):
		data = data = {
				'token':self.token,
		}

		req = requests.post('http://api.imgod.ir/todo/check/check',data=data).json()
		json = req
		if json['message'] == 'token found':
			return json['tokenn'][0]['username']
		elif json['message'] == 'token not found':
			print('token not found . please login')	
		else:
			print('something wrong')
			
		