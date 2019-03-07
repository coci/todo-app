import sys
import json
import sqlite3
from prettytable import PrettyTable
from task import Task




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
		


# try:
if sys.argv[1] == "-insert":
	task = sys.argv[2]
	insert(task)
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
elif sys.argv[1] == "-help":
	print('''
+----------------------------------------------------------------+
|                           ** help **                           |
+----------------------------------------------------------------+
|  for add task ==> python3 todo.py -insert 'task description'	 |
|                                                                |
|  for list all ==> python3 todo.py -list                        |
|                                                                |                                                                       |
|  for edit task ==> python3 todo.py -edit 'id' 'new text'       |
|                                                                |
|  for delete task ==> python3 todo.py -delete 'id'              |
|                                                                |
|  for clear all entry task ==> python3 todo.py -clear           |
|                                                                |
|  for set a task into done state ==> python3 todo.py -done 'id' |
+----------------------------------------------------------------+
		''')
# except Error as e:
# 	print(e)
# 	print('''
# 	+----------------------------------------------------------------+
# 	|                           ** help **                           |
# 	+----------------------------------------------------------------+
# 	|  for add task ==> python3 todo.py -insert 'task description'	 |
# 	|                                                                |
# 	|  for list all ==> python3 todo.py -list                        |
# 	|                                                                |
# 	|  for show specific task ==> python3 todo.py -show 'id'         |
# 	|                                                                |
# 	|  for edit task ==> python3 todo.py -edit 'id' 'new text'       |
# 	|                                                                |
# 	|  for delete task ==> python3 todo.py -delete 'id'              |
# 	|                                                                |
# 	|  for clear all entry task ==> python3 todo.py -clear           |
# 	|                                                                |
# 	|  for set a task into done state ==> python3 todo.py -done 'id' |
# 	+----------------------------------------------------------------+
# 		''')
