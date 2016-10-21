#!usr/bin/env python
from string import Template
s = Template('There are ${howmany} ${lang} Quotation Symbols')

print s.substitute(lang='Python',howmany=4)
print s.safe_substitute(lang='chinese')