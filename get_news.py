# -*- coding:utf-8 -*-
import re
import os
import urllib.request
from bs4 import BeautifulSoup
import webbrowser
import time

arr=[]
urls=[]

# 目标url
url=[]

target_url='http://cai.163.com/'

def get_url_content(url):
	res=urllib.request.urlopen(url)
	html=res.read()
	soup=BeautifulSoup(html,'html.parser')
	content_list=soup.select(".headLine")

	# 写入文件以便后续操作
	with open('url.txt','w') as f:
		f.writelines(str(content_list))


def get_target_url():
	recom='href=\".*html'
	with open('url.txt','r') as u:
		for i in u:
			t=i.split(' ')
			arr.extend(t)

	for j in arr:
		temp=re.search(recom,j)
		if(temp):
			urls.append(j)
		# print(j)
	for i in urls:
		url.append(i.split('\"')[-2])

def open_url(url):
	# 调用浏览器打开网页
	webbrowser.open(url)
	# 睡眠时间
	time.sleep(1)


get_url_content(target_url)
get_target_url()

for i in url:
	open_url(i)
