﻿#!usr/bin/env python
'''����һ���ı��зǿհ׵��ʵ�����'''
f = open('words.txt','r')
print len([word for line in f for word in line.split()])
f.close()