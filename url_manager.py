#coding:utf8
class UrlManager(object):
	#url管理模块，实现两个功能，接收新url以及依次提取url，供解析模块解析，内部分成两个set，已经爬取和未爬取部分
	def __init__(self):
		self.new_urls = set()
		self.old_urls = set()

	def add_new_url(self,url):
		if url is None:
			return
		if url not in self.new_urls and url not in self.old_urls:
		    self.new_urls.add(url) 

	def has_new_url(self):
		return len(self.new_urls) != 0

	def get_new_url(self):
		new_url = self.new_urls.pop()
		self.old_urls.add(new_url)
		return new_url

	def add_new_urls(self,urls):
		#网页解析出的url依次入管理器
		if urls is None or len(urls) == 0:
			return
		for url in urls:
			self.add_new_url(url)
