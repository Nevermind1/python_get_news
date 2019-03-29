# -*- coding:utf-8 -*-

# url: https://www.did-you-knows.com/
# 冷知识


import re
import os
import urllib.request
from bs4 import BeautifulSoup


def get_url(url):
	content_list=[]
	#url=url
	res=urllib.request.urlopen(url)
	html=res.read()
	soup=BeautifulSoup(html,'html.parser')
	content_list=soup.select(".dykText")
	with open('./content.txt','a') as f:
		for i in content_list:
			# print(i.get_text())
			f.writelines(i.get_text()+'\n')

	# print(soup.select(".dykText"))
	# print(url)

#循环获取网址传递给get_url函数
for i in range(1,51):
	url=r"https://www.did-you-knows.com/?page="
	url = url+str(i)
	print(url)
	#print('%.2f...'%(i/100))
	print(str(i*2)+'%')

	get_url(url)


# url=r"https://www.did-you-knows.com/?page=2"
# get_url(url)
#get_url(url)
#res=urllib2.urlopen(url)
#res=urllib.request.urlopen(url)
#res.add_header("user-agent","Mozilla/5.0")
#res2=urllib2.urlopen(res)
#print res.read()
#f=open('1.txt','r')

#html=res.read()
#html=res.getcode()
#soup=BeautifulSoup(html, "lxml")
#soup=BeautifulSoup(html, "html5lib")
#print soup.get_text()
#s=soup.find(id='fact')
#for i in s:
#	print i
#print (s)
#f.close()
