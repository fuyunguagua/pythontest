#!usr/bin/env python
'''计算一段文本中非空白单词的数量'''
f = open('words.txt','r')
print len([word for line in f for word in line.split()])
f.close()