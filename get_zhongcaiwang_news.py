# -*- coding:utf-8 -*-
import re
import os
import urllib.request
from bs4 import BeautifulSoup
import webbrowser
import time

# 传入网址获取目标网址
def get_target_urls(url):
	# 三个数组存放字符串
	urls=[]
	newUrls=[]
	target=[]
	# 正则表达式匹配项
	comp='href.*html'
	# 打开链接
	res=urllib.request.urlopen(url)
	html=res.read()
	soup=BeautifulSoup(html,'html.parser')
	content_list=soup.select(".news_clist")
	# 遍历BS获取元素进行一系列拼接
	for i in content_list[0]:
		urls.extend(str(i).split(" "))
	for i in urls:
		temp=re.search(comp,i)
		if(temp):
			newUrls.append(i)
	for i in newUrls:
		target.append(i.split("\"")[-2])
	urls=[]
	for i in target:
		urls.append(url+i.split('/',2)[-1])
	for i in urls:
		# print(i)
		# 向open_url()传递网址
		open_url(i)


def open_url(url):
	# 调用浏览器打开网页
	webbrowser.open(url)
	# 睡眠1s
	time.sleep(1)

# 目标网址
url='http://www.zhcw.com/xinwen/'
get_target_urls(url)
