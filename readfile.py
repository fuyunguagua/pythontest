#!/usr/bin/env Python

'readTextFile.py -- read and display text file'

#get file name
filename  = raw_input('Enter filename:')

# attempt to open file for reading
try:
    fobj = open(filename,'r')
except IOError, e:
    print '*** file open error:',e
else:
    #display contents to the screen
    for eachLine in fobj:
        print eachLine,
    fobj.close()