import sqlite3
import requests


try :
	conection = sqlite3.connect('todo.db')
except error as e:
	print(e)

class Task(object):
	"""this is where all magic happen , create task , show all task ,......"""
	def __init__(self, title, id,userid):
		self.title = title
		self.id = id
		self.state = 'pending' # pending, done, deleted
		self.userid = userid

	def create(self):
		'''
		this send given information to server ( create task) .
		title : task ( we got from user )
		userid : this tell server which user create this task ( we got this from token file from user os)
		'''
		
		data = {
				'task' : self.title,
				'userid' : self.userid
		}
		req = requests.post('http://api.imgod.ir/todo/task/add',data=data).json()
		parse_json = req
		print(parse_json['message'])
		

	def update(self) -> list:
		data = {
				'task' : self.title,
				'id'	: self.id,
				'userid' : self.userid
		}
		req = requests.post('http://api.imgod.ir/todo/task/update',data=data).json()
		parse_json = req
		print(parse_json)




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
		data = {
				'id'	: self.id,
				'userid' : self.userid
		}
		req = requests.post('http://api.imgod.ir/todo/task/delete',data=data).json()
		parse_json = req
		print(parse_json)

		
	@staticmethod
	def delete_all():
		cursor = conection.cursor()
		cursor.execute("DELETE FROM all_task")
		conection.commit()
		conection.close()
		print("All task are successfully deleted")

	def get_all(self) -> list:
		data = {
				'userid' : self.userid
		}
		req = requests.post('http://api.imgod.ir/todo/task/show',data=data).json()
		parse_json = req
		return parse_json

class User(object):
	"""handle all information about user , such as :
	1. register user
	2. login user
	3. check user

	"""
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
		parse_json = req
		if parse_json['message'] == 'user found':
			print('user found . your now loging')
			return parse_json['tokenn'][0]['token']
		if 	parse_json['message'] == 'user not found':
			print("user not found")
	

	def check(self):
		data = data = {
				'token':self.token,
		}

		req = requests.post('http://api.imgod.ir/todo/check/check',data=data).json()
		parse_json = req
		if parse_json['message'] == 'token found':
			return parse_json['tokenn'][0]['username']
		elif parse_json['message'] == 'token not found':
			print('token not found . please login')	
		else:
			print('something wrong')
			
		