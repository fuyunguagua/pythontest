#!/usr/bin/env python

def displaynumtype(num):
	print num,'is',
	if isinstance(num, (int, long, float, complex)):
		print 'a number of: ',type(num).__name__
	else:
		print 'not a number at all!!'
def main():
	displaynumtype(11)
	displaynumtype(44.3)
	displaynumtype(44+5j)
	displaynumtype('ss')
if __name__ == '__main__':
	main()