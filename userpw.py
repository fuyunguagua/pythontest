#!/usr/bin/env python
'''提供用户管理的功能，像什么用户注册，就用户登陆'''
db = {}
def newUser():
	promprt = 'please enter your username:'
	username = raw_input(promprt)
	while True:
		if username in db.keys():
			print 'username existed,please try another'
		else:
			pwd = raw_input('input your password:')
			db[username] = pwd
			break
	print 'zhu ce cheng gong'
def olderUser():
	username = raw_input('your username:')
	pwd = raw_input('your password')
	value = db.get(username)
	if value == pwd:
		print 'loggin success',username
	else:
		print 'faild to log'
def showmenu():
	promprt = '''
	(N)ew user
	(O)lder user
	(Q)uit
	
	enter your option:'''
	COMMANDS = {'n':newUser,'o':olderUser}
	done = False
	while not done:
		chosen = False
		while not chosen:
			try:
				choice = raw_input(promprt).strip()[0].lower()
			except (EOFError,KeyboardInterrupt):
				choice = 'q'
			if choice not in 'noq':
				print 'invalid option,please try again!'
			else:
				chosen = True
		if choice == 'q':
			break
		COMMANDS[choice]()
if __name__ == "__main__":
	showmenu()
