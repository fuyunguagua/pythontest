#!/usr/bin/env python
'makeTextFile.py--create test file'

import os
s = os.linesep

#get filename
while True:
    filename = raw_input('input filename:')
    if os.path.exists(filename):
        print "Error:'%s' already exists" % filename
    else :
        break
#get file content lines
all = []
print "\n Enter lines ('.' by itself to quit).\n"

#loop until user terminates input
while True:
    entry = raw_input('>')
    if entry == '.':
        break
    else:
        all.append(entry)

#write lines to file with proper line-ending
fobj = open(filename,'w')
print ["%s%s" % (x,s) for x in all]
fobj.writelines(["%s%s" % (x,s) for x in all])
fobj.close()
print 'Done'
        
