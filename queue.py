#!usr/bin/env python
'''模拟一个队列数据结构'''
queue = []

def enQ():
	queue.append(raw_input("Please enter a string:	").strip())
def deQ():
	if len(queue) == 0:
		print "Can not pop a element from a empty queue!"
	else:
		print "removed a element [",queue.pop(0),"]"
def viewQ():
	print queue
def showmenu():
	pr = '''
	(E)nqueue
	(D)equeue
	(V)iewqueue
	(Q)uit
	
	Enter a word to make a choice:	'''
	
	COMMANDS = {'e':enQ, 'd':deQ, 'v':viewQ}
	while True:
		while True:
			try:
				choice = raw_input(pr).strip()[0].lower()
			except(EFOError,KeyboardInterrupt,IndexError):
				choice = 'q'
				
			print '\nYou picked: [%s]' % choice

			if choice not in 'edvq':
				print "invalid option,please try again!"
			else:
				break
		if choice == 'q':
			break
		else:
			COMMANDS[choice]()
			
if __name__ == "__main__":
	showmenu()