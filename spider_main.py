#coding:utf8
#
import url_manager,html_downloader,html_parser,htmloutputer
class SpiderMain(object):
	def __init__(self):
		#初始化，创建url管理，url下载，url解析，数据处理输出模块对象
		self.urls = url_manager.UrlManager()
		self.downloader = html_downloader.HtmlDownloader()
		self.parser = html_parser.HtmlParser()
		self.outputer = htmloutputer.HtmlOutputer()

	def craw(self,root_url):
		#爬虫主函数
		count = 1
		self.urls.add_new_url(root_url)#添加入口URl

		while self.urls.has_new_url():
			try:				
				new_url = self.urls.get_new_url()#取出一条url
				print 'craw %d : %s' % (count,new_url)

				html_count = self.downloader.download(new_url)#下载url网页资源

				#print html_count
				new_urls,new_data = self.parser.parser(new_url,html_count)#实现两个功能：返回网页解析得到的数据，返回网页上的新url组
				#print new_data

				self.urls.add_new_urls(new_urls)#把新URL组添加到url管理器
				#print new_data
				self.outputer.collect_data(new_data)#解析数据收集
				if count == 100:
					break

				count = count + 1
			except:
				print 'craw failed'

		self.outputer.output_html()#按照格式输出解析数据

if __name__=='__main__':
	root_url = 'http://baike.baidu.com/view/21087.htm'
	obj_spider = SpiderMain()
	obj_spider.craw(root_url)
