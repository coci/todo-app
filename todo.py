import sys
import fire
import json
import sqlite3
from prettytable import PrettyTable


def insert(task):
	
	try:
		conection = sqlite3.connect('todo.db')
		cursor = conection.cursor()
		entry_task = task
		state= 'pending'
		cursor.execute("insert into all_task (task, state) values (?,?)", (entry_task,state))
		conection.commit()
		conection.close()
		print("Task successfult added .")
	except Error as e:
		print(e)


def list_all():
	try:
		conection = sqlite3.connect('todo.db')
		cursor = conection.cursor()
		cursor.execute("SELECT rowid,task,state FROM all_task")
		rows = cursor.fetchall()
		x = PrettyTable()
		x.field_names = ['id','task','state']
		for i in range(len(rows)):
			t = rows[i]
			id = t[0]
			task = t[1]
			state = t[2]
			x.add_row([id,task,state])	
		print(x)	
	except Error as e:
		print(e)
	
			

		
def show(id):
	try:
		conection = sqlite3.connect('todo.db')
		cursor = conection.cursor()
		cursor.execute("SELECT rowid,task,state FROM all_task WHERE rowid = %s"%(id))
		rows = cursor.fetchall()
		x = PrettyTable()
		x.field_names = ['id','task','state']
		t = rows[0]
		id = t[0]
		task = t[1]
		state = t[2]
		x.add_row([id,task,state])	
		print(x)	
	except Error as e:
		print(e)

def edit(id,task):
	conection = sqlite3.connect('todo.db')
	cursor = conection.cursor()
	cursor.execute("UPDATE all_task SET task='%s' WHERE rowid = %s"%(task,id))
	conection.commit()
	print("task successfully updated and here is approval :")
	cursor.execute("SELECT rowid,task,state FROM all_task WHERE rowid = %s"%(id))
	rows = cursor.fetchall()
	x = PrettyTable()
	x.field_names = ['id','task','state']
	t = rows[0]
	id = t[0]
	task = t[1]
	state = t[2]
	x.add_row([id,task,state])	
	print(x)
	conection.close()


	
def delete(id):
	conection = sqlite3.connect('todo.db')
	cursor = conection.cursor()
	cursor.execute("DELETE FROM all_task WHERE rowid = %s"%(id))
	conection.commit()
	conection.close()
def delete_all():
	conection = sqlite3.connect('todo.db')
	cursor = conection.cursor()
	cursor.execute("DELETE FROM all_task")
	conection.commit()
	conection.close()
	print("All task are successfully deleted")
def done(id):
	conection = sqlite3.connect('todo.db')
	cursor = conection.cursor()
	cursor.execute("UPDATE all_task SET state= 'done' WHERE rowid = %s"%(id))
	conection.commit()
	print("task successfully has been done and here is approval :")
	cursor.execute("SELECT rowid,task,state FROM all_task WHERE rowid = %s"%(id))
	rows = cursor.fetchall()
	x = PrettyTable()
	x.field_names = ['id','task','state']
	t = rows[0]
	id = t[0]
	task = t[1]
	state = t[2]
	x.add_row([id,task,state])	
	print(x)
	conection.close()
		


try:
	if sys.argv[1] == "-insert":
		task = sys.argv[2]
		insert(task)
	elif sys.argv[1] == "-list":
		list_all()
	elif sys.argv[1] == "-show":
		id = sys.argv[2]
		show(id)
	elif sys.argv[1] == "-edit":
		id = sys.argv[2]
		task = str(sys.argv[3])
		edit(id,task)
	elif sys.argv[1] == "-delete":
		id = sys.argv[2]
		delete(id)
	elif sys.argv[1] == "-clear":
		delete_all()
	elif sys.argv[1] == "-done":
		id = sys.argv[2]
		done(id)		
	elif sys.argv[1] == "-help":
		print('''
	+----------------------------------------------------------------+
	|                           ** help **                           |
	+----------------------------------------------------------------+
	|  for add task ==> python3 todo.py -insert 'task description'	 |
	|                                                                |
	|  for list all ==> python3 todo.py -list                        |
	|                                                                |
	|  for show specific task ==> python3 todo.py -show 'id'         |
	|                                                                |
	|  for edit task ==> python3 todo.py -edit 'id' 'new text'       |
	|                                                                |
	|  for delete task ==> python3 todo.py -delete 'id'              |
	|                                                                |
	|  for clear all entry task ==> python3 todo.py -clear           |
	|                                                                |
	|  for set a task into done state ==> python3 todo.py -done 'id' |
	+----------------------------------------------------------------+
			''')
except:
	print('''
	+----------------------------------------------------------------+
	|                           ** help **                           |
	+----------------------------------------------------------------+
	|  for add task ==> python3 todo.py -insert 'task description'	 |
	|                                                                |
	|  for list all ==> python3 todo.py -list                        |
	|                                                                |
	|  for show specific task ==> python3 todo.py -show 'id'         |
	|                                                                |
	|  for edit task ==> python3 todo.py -edit 'id' 'new text'       |
	|                                                                |
	|  for delete task ==> python3 todo.py -delete 'id'              |
	|                                                                |
	|  for clear all entry task ==> python3 todo.py -clear           |
	|                                                                |
	|  for set a task into done state ==> python3 todo.py -done 'id' |
	+----------------------------------------------------------------+
		''')
