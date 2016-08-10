#!usr/bin/python
#-*-coding:utf-8-*-
#conding:utf8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')#这一部分是为了解决encode乱码问题，找了很久，终于解决~~

class HtmlOutputer(object):
	def __init__(self):
		self.datas = []

	def collect_data(self,data):
		if data is None:
			return 
		self.datas.append(data)

	def output_html(self):
		fout = open("aaa.html","w")
		fout.write("<html>")
		fout.write("<head><meta http-equiv=\"content-type\" content=\"text/html;charset=utf-8\"></head>")	
		fout.write("<body>")
		fout.write("<table border='1 solid red'>")
		#print self.datas
		for data in self.datas:
			# fout.write(data['url'])
			# fout.write(data['title'])
			# fout.write(data['summary'].encode('utf-8'))			
			fout.write("<tr>")
			fout.write("<td>%s</td>"% data['url'])
			fout.write("<td>%s</td>"% data['title'].encode('utf-8'))
			fout.write("<td>%s</td>"% data['summary'].encode('utf-8'))
			fout.write("</tr>")

		fout.write("</table>")
		fout.write("</body>")
		fout.write("</html>")
		fout.close()
		
		