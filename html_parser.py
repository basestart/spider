#conding:utf8
#使用BS4解析下载网页
from bs4 import BeautifulSoup
import re
import urlparse

class HtmlParser(object):
	def _get_new_urls(self,page_url,soup):
		#获取网页中所有链接，返回set，备用入url管理器
		new_urls = set()
		links = soup.find_all('a',href=re.compile(r"/view/\d+\.htm"))
		
		for link in links:
			new_url = link['href']
			new_full_url = urlparse.urljoin(page_url,new_url)

			new_urls.add(new_full_url)
		
		return new_urls

	def _get_new_data(self,page_url,soup):
		#根据页面结构获取指定位置的数据，以键值对的形式添加到res_data对象，并返回res_data
		res_data = {}
		res_data['url'] = page_url
		title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find("h1")		
		res_data['title'] = title_node.get_text()		
		summary_node = soup.find('div',class_="lemma-summary")
		#print 'a'
		res_data['summary'] = summary_node.get_text()
		#print res_data
		return res_data


	def parser(self,page_url,html_cont):
		#接收url以及url资源，实现数据解析，新url提取功能，返回解析数据和新url组
		#print page_url
		if page_url is None or html_cont is None:
			return 
		
		soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
		new_urls = self._get_new_urls(page_url,soup)
		new_data = self._get_new_data(page_url,soup)
		#print new_data
		return new_urls,new_data