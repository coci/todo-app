import sys
import json
import sqlite3
from prettytable import PrettyTable
from task import Task
from task import User
import getpass



def user_create():
	'''
	this create username on our server
	'''
	username = input("please enter username : ")
	password = getpass.getpass('please enter password :')
	email = input("please enter email : ")
	check_user()
	create = User(username=username,password=password,email=email,token=None)
	create.register()


def user_login():
	'''
	this function get username and password as input
	and send them to server , if username and password exist on server then server return a token to client 
	and this function save token on file
	'''
	username = input('please enter your username : ')
	password = getpass.getpass('please enter password :')
	create = User(username=username, password=password, email=None,token=None)
	token = create.login()

	with open(f'.token.json','w+') as f:
		f.write(token)


def check_user():
	'''
	for each request to server we must send username to server so i wrote this function :
		read token from file if exist , its send token into server and then if token exist on server :
		server return username to client
	'''
	try:
		with open(f'.token.json','r') as f:
			token = f.read()
	except :
		print("i think you are not in same directory with project file, token will save in the project directory or you must login in .")

	instance_check_user = User(username=None, password=None, email=None,token=token)
	userid = instance_check_user.check()
	return str(userid)

def insert(title:str):
	'''
	this will insert task to server with given information :
	title = task
	to get what user insert this task we create function check_user() and its return what is the username from token .
	userid now contain username and we send task title and username into server
	'''
	if len(title) > 89: # when we create a table of all task , its not good idea task have bigger than 89 character .
		print("entry task too much big , please enter summary of task")
		return
	userid = check_user()
	task = Task(title=title,id=None,userid=str(userid))
	task.create()


def list_all():
	
	userid = check_user()
	task = Task(title=None,id=None,userid=userid)
	rows = task.get_all()
	x = PrettyTable()
	x.field_names = ['id','task','state']
	for i in range(len(rows)):
		tuple_task = rows[i]
		id = tuple_task['id']
		task = tuple_task['task']
		state = tuple_task['state']
		x.add_row([id,task,state])	
	print(x)

def edit(idd: int,title: str):
	if len(title) > 89 :
		print("entry task too much big , please enter summary of task")
	userid = check_user()	
	task = Task(title=title,id=idd,userid=userid)
	message = task.update()
	
	 
	
def delete(idd:int):
	try:
		userid = check_user()
		task = Task(title=None,id=idd,userid=userid)
		task.delete()
	except Error as e:
		print(e)	


def delete_all():
	try:
		Task.delete_all()
	except Error :
		print(Error)

def done(id:int):
	task = Task(title=None,id=id)
	rows = task.done()
	x = PrettyTable()
	x.field_names = ['id','task','state']
	t = rows[0]
	id = t[0]
	task = t[1]
	state = t[2]
	x.add_row([id,task,state])
	print(x)
		


if sys.argv[1] == "-insert":
	task = sys.argv[2]
	insert(task)
elif sys.argv[1] == "-create":
	user_create()	
elif sys.argv[1] == "-login":
	user_login()	
elif sys.argv[1] == "-list":
	list_all()
elif sys.argv[1] == "-edit":
	idd = sys.argv[2]
	task = str(sys.argv[3])
	edit(idd,task)
elif sys.argv[1] == "-delete":
	idd = sys.argv[2]
	delete(idd)
elif sys.argv[1] == "-clear":
	delete_all()
elif sys.argv[1] == "-done":
	id = sys.argv[2]
	done(id)		

