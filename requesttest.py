import requests
import re
import sys
from bs4 import BeautifulSoup as bs4
reload(sys)
sys.setdefaultencoding('utf-8')
def test():
	url = "http://www.hao123.com"
	page_html = requests.get(url).text.decode('utf-8','ignore')
	print page_html
if __name__ == '__main__':
	print sys.getdefaultencoding()
	test()