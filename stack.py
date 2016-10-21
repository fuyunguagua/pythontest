#!/usr/bin/env python
'''模拟一个栈数据结构'''
stack = []

def pushit():
	stack.append(raw_input("Enter a string:	").strip())

def popit():
	if len(stack) == 0:
		print "stack len is 0"
	else:
		print "Removed element [",stack.pop(),']'

def viewstack():
	print stack

COMMANDS = {'u':pushit,'o':popit, 'v':viewstack}

def showmenu():

	pr = '''
	p(U)sh
	p(O)P
	(V)iew
	(Q)uit
	
	Make a choice:'''
	#这两个for循环简直精妙
	while True:
		while True:#when user choice a quit,we should end this script
			try:
				choice = raw_input(pr).strip()[0].lower()
			except(EOFError,KeyboardInterrupt,IndexError):
				choice = 'q'
			if choice not in 'uovq':
				print 'Invalid option,please try again!'
			else:
				break
		if choice == 'q':
			break
		COMMANDS[choice]()

if __name__ == "__main__":
	showmenu()