import sys
import json
import sqlite3
from prettytable import PrettyTable
from task import Task
from task import User
import getpass

def user_create():
	username = input("please enter username : ")
	password = getpass.getpass('please enter password :')
	email = input("please enter email : ")
	check_user()
	create = User(username=username,password=password,email=email,token=None)
	create.register()

def check_user():
	with open(f'.token.json','r') as f:
		token = f.read()
	#print(token)
	cke = User(username=None, password=None, email=None,token=token)
	cke.check()

def user_login():
	username = input('please enter your username : ')
	password = getpass.getpass('please enter password :')
	create = User(username=username, password=password, email=None,token=None)
	token = create.login()

	with open(f'.token.json','w+') as f:
		f.write(token)

def insert(title:str):
	if len(title) > 89:
		print("entry task too much big , please enter summary of task")
		return
	task = Task(title=title,id=None)
	task.create()


def list_all():
	rows = Task.get_all()
	x = PrettyTable()
	x.field_names = ['id','task','state']
	for i in range(len(rows)):
		tuple_task = rows[i]
		id = tuple_task[0]
		task = tuple_task[1]
		state = tuple_task[2]
		x.add_row([id,task,state])	
	print(x)
	
			
def edit(id: int,title: str):
	if len(title) > 89 :
		print("entry task too much big , please enter summary of task")
	task = Task(title=title,id=id)
	rows = task.update()
	x = PrettyTable()
	x.field_names = ['id','task','state']
	t = rows[0]
	id = t[0]
	task = t[1]
	state = t[2]
	x.add_row([id,task,state])	
	print(x)
	 
	
def delete(id:int):
	try:
		task = Task(title=None,id=id)
		task.delete()
		print("successfully deleted itme")
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
elif sys.argv[1] == "-check":
	check_user()	
elif sys.argv[1] == "-login":
	user_login()	
elif sys.argv[1] == "-list":
	list_all()
elif sys.argv[1] == "-edit":
	idd = sys.argv[2]
	task = str(sys.argv[3])
	edit(idd,task)
elif sys.argv[1] == "-delete":
	id = sys.argv[2]
	delete(id)
elif sys.argv[1] == "-clear":
	delete_all()
elif sys.argv[1] == "-done":
	id = sys.argv[2]
	done(id)		

