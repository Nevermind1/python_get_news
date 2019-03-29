# -*- coding:utf-8 -*-

# 996ICU公司点赞数据
# 网址：https://feathub.com/LinXueyuanStdio/996.ICU
# python: v3.8.0a1
# OS: Windows10 专业版

import re
import os
import urllib.request
from bs4 import BeautifulSoup
import time

def get_content(url):

	# 存放写入数据
	aa=[]
	# 打开链接
	res=urllib.request.urlopen(url)
	html=res.read()
	soup=BeautifulSoup(html,'html.parser')
	content_list=soup.find_all("div", class_="active feature")
	# 遍历数据
	for i in content_list:
		# 临时存放数组
		tmp=[]
		tmp.append(i.find("span").get_text())
		tmp.append(i.find(class_="text-muted").find("a").get_text())
		tmp.append(i.find("h4").get_text())
		
		aa.append(tmp)
	# 写入
	with open('996ICU.txt','a') as f:
		# f.writelines("%-8s%5s%36s\n"%("点赞数","贡献者","公司名称"))
		for i in aa:
			f.writelines(" %-10s%-25s%-20s\n" % (i[0],i[1],i[2]))




# 格式合适，不修改
# with open('996ICU.txt','w') as f:
# 	f.writelines("%-8s%5s%36s\n"%("点赞数","贡献者","公司名称"))
# 	for i in aa:
# 		f.writelines(" %-10s%-25s%20s\n" % (i[0],i[1],i[2]))

with open('996ICU.txt','w') as f:
	# 写入当前时间
	f.writelines("时间: "+time.strftime('%Y-%m-%d_%H:%M:%S',time.localtime())+"\n")
	# 写入头部导航
	f.writelines("%-8s%5s%36s\n"%("点赞数","贡献者","公司名称"))


for i in range(1,15):
	url='https://feathub.com/LinXueyuanStdio/996.ICU?page='

	# 拼凑url
	url=url+str(i)

	# 传递url
	get_content(url)
	# print(url)

	# 睡眠1s
	time.sleep(1)
