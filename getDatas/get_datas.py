import requests
from bs4 import BeautifulSoup as bs
import re
import csv
from multiprocessing import Pool
headers = {'Referer':'http://www.aozora.gr.jp/',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
proxies = {'http': 'http://210.13.77.66:8080','https': 'http://210.13.77.66:8080'}

import sqlite3

def get_con(func):
	data_path = r"sources2.db"

	def sql_exc():
		conn = sqlite3.connect(data_path, check_same_thread = False)
		conn.text_factory = str
		cur = conn.cursor()
		data = func(cur)
		cur.close()
		conn.commit()
		conn.close()
		return data

	return sql_exc


@get_con
def get_sakuhinn(cur):
	# 查询sakuhinn
	print("正在查询作品列表")
	cur.execute("SELECT * FROM sakuhinndata")
	rows = cur.fetchall()
	return rows

@get_con
def get_sakusya(cur):
	# 查询sakusya
	print("正在查询作者列表")
	cur.execute("SELECT * FROM sakusyadata")
	rows = cur.fetchall()
	return rows

@get_con
def sakuhinntable(cur):
	cur.execute('''CREATE TABLE SAKUHINNDATA 
			  (
				SAKUHINNID INTEGER PRIMARY KEY autoincrement, SAKUHINNCATALOG CHAR(2) NOT NULL, SAKUHINNNAME TEXT NOT NULL, SAKUSYA CHAR NULL, SAKUHINNLINK CHAR(60) NULL
			  )''')
"""sakuhinnid,sakuhinncatalog,sakuhinnname,sakusya,sakuhinnlink"""

@get_con
def sakusyatable(cur):
	cur.execute('''CREATE TABLE SAKUSYADATA 
			  (
				SAKUSYAID INTEGER PRIMARY KEY autoincrement, SAKUSYACATALOG CHAR(2) NOT NULL, SAKUSYANAME TEXT NOT NULL, SAKUHINN CHAR NULL, SAKUSYALINK CHAR(60) NULL
			  )''')

def bulid_db():
	"""数据库初始化在此"""
	print("数据库初始化")
	try:
		print("正在创建作品列表。。")
		sakuhinntable()
		print("成功！")
	except Exception as e:
		print(e)
		print('已有work表或创建失败！')
		
	try:
		print("正在创建作者列表。。")
		sakusyatable()
		print("成功！")
	except Exception as e:
		print(e)
		print('已有SAKUSYA表或创建失败！')
		
def sakuhinninsert(_sakuhinncatalog,_sakuhinnname,_sakusya,_sakuhinnlink):
	"""插入一行sakuhinn数据"""
	try:
		print("正在插入作品列表： " + _sakuhinnname)
		data_path = r"sources2.db"
		conn = sqlite3.connect(data_path, check_same_thread = False)
		conn.text_factory = str
		cur = conn.cursor()
		data = (_sakuhinncatalog,_sakuhinnname,_sakusya,_sakuhinnlink)
		ins = 'INSERT INTO sakuhinndata (sakuhinncatalog,sakuhinnname,sakusya,sakuhinnlink) VALUES(?, ?, ?, ?)'
		cur.execute(ins, data)

	except Exception as e:
		print(e)
		print('eroo sakuhinninsert')
	finally:
		cur.close()
		conn.commit()
		conn.close()
		
def sakusyainsert(_sakusyacatalog,_sakusyaname,_sakuhinn,_sakusyalink):
	"""插入一行sakusya数据"""
	try:
		print("正在插入作者列表： " + _sakusyaname)
		data_path = r"sources2.db"
		conn = sqlite3.connect(data_path, check_same_thread = False)
		conn.text_factory = str
		cur = conn.cursor()
		data = (_sakusyacatalog,_sakusyaname,_sakuhinn,_sakusyalink)
		ins = 'INSERT INTO sakusyadata (sakusyacatalog,sakusyaname,sakuhinn,sakusyalink) VALUES(?, ?, ?, ?)'
		cur.execute(ins, data)

	except Exception as e:
		print(e)
		print('eroo sakusyainsert')
	finally:
		cur.close()
		conn.commit()
		conn.close()
		

def get_onesakuhinn(_name):
	"""获取某一作品数据"""
	try:
		print("正在查询作品信息： " + _name)
		data_path = r"sources2.db"
		conn = sqlite3.connect(data_path, check_same_thread = False)
		conn.text_factory = str
		cur = conn.cursor()
		data = (_name,)
		ins = 'select * from sakuhinndata where sakuhinnname = ?'
		cur.execute(ins, data)
		rows = cur.fetchall()
		cur.close()
		conn.commit()
		conn.close()
		return rows
	except Exception as e:
		print(e)
		cur.close()
		conn.commit()
		conn.close()
		return False
	
def get_onesakusya(_name):
	"""获取某一作者数据"""
	try:
		print("正在查询作者信息： " + _name)
		data_path = r"sources2.db"
		conn = sqlite3.connect(data_path, check_same_thread = False)
		conn.text_factory = str
		cur = conn.cursor()
		data = (_name,)
		ins = 'select * from sakusyadata where sakusyaname = ?'
		cur.execute(ins, data)
		rows = cur.fetchall()
		cur.close()
		conn.commit()
		conn.close()
		return rows
	
	except Exception as e:
		print(e)
		cur.close()
		conn.commit()
		conn.close()
		return False
	
def get_kanasakuhinn(_sakuhinncatalog):
	"""获取某一作品假名类数据"""
	try:
		print("正在获取 " + _sakuhinncatalog + "类作品列表")
		data_path = r"sources2.db"
		conn = sqlite3.connect(data_path, check_same_thread = False)
		conn.text_factory = str
		cur = conn.cursor()
		data = (_sakuhinncatalog,)
		ins = 'select * from sakuhinndata where sakuhinncatalog = ?'
		cur.execute(ins, data)
		rows = cur.fetchall()
		cur.close()
		conn.commit()
		conn.close()
		return rows
	except Exception as e:
		print(e)
		cur.close()
		conn.commit()
		conn.close()
		return False
	
def get_kanasakusya(_sakusyacatalog):
	"""获取某一作者假名类数据"""
	try:
		print("正在获取 " + _sakusyacatalog + "类作者列表")
		data_path = r"sources2.db"
		conn = sqlite3.connect(data_path, check_same_thread = False)
		conn.text_factory = str
		cur = conn.cursor()
		data = (_sakusyacatalog,)
		ins = 'select * from sakusyadata where sakusyacatalog = ?'
		cur.execute(ins, data)
		rows = cur.fetchall()
		cur.close()
		conn.commit()
		conn.close()
		return rows
	
	except Exception as e:
		print(e)
		cur.close()
		conn.commit()
		conn.close()
		return False

def get_catalog_links():
	"""返回作者分类目录和作品分类目录的标签项（每一项的["href"]获取网址后半段，需在前加homepage，每项的.text获取名称）"""
	homepage = 'http://www.aozora.gr.jp/'
	reg_homepage = requests.get(homepage,headers=headers)
	soup_homepage = bs(reg_homepage.content.decode("utf-8"),'lxml')
	links = soup_homepage.findAll(name='a',attrs={"href":re.compile(r'^index')})
	sakusyas = links[1:12]
	sakuhins = links[12:-3]
	#print(sakuhins[0]['href'])
	return sakusyas,sakuhins
	
def save_sakuhinn(_sakuhinncatalog,_sakuhinnname,_sakusya,_sakuhinnlink):
	try:
		if not get_onesakuhinn(_sakuhinnname):
			sakuhinninsert(_sakuhinncatalog,_sakuhinnname,_sakusya,_sakuhinnlink)
			print("已储存作品："+_sakuhinnname)
		else:
			print("该作品已存在： "+_sakuhinnname)
	except:
		pass
def save_sakusya(_sakusyacatalog,_sakusyaname,_sakuhinn,_sakusyalink):
	try:
		if not get_onesakusya(_sakusyaname):
			sakusyainsert(_sakusyacatalog,_sakusyaname,_sakuhinn,_sakusyalink)
			print("已储存作家："+_sakusyaname)
		else:
			print("该作家已存在： "+_sakusyaname)
	except:
		pass
		
def get_saka_links(catalog,url):
	"""输入作者类别链接，返回该类作品分类列表链接标签，（每一项的["href"]获取网址后半段，需在前加homepage，每项的.text获取名称）"""
	a = url[-7:-5]
	if '_' in a:
		p = a[1]
	else:
		p = a[0:2]
	url = "http://www.aozora.gr.jp/index_pages/person_"+p+".html"
	reg_saka = requests.get(url,headers=headers)
	soup_saka = bs(reg_saka.content.decode("utf-8"),'lxml')
	links = soup_saka.findAll(name='a',attrs={"href":re.compile(r'^person')})
	l = links[:-10]
	for i in range(len(l)):
		l[i] = {'catalog':catalog + '.'+ p,'sakusyaname':l[i].text,'link':'http://www.aozora.gr.jp/'+l[i]['href']}
		o = l[i]
		# save_sakusya(_sakusyacatalog,_sakusyaname,_sakuhinn,_sakusyalink)
		save_sakusya(o['catalog'],o['sakusyaname'],'Unknown',o['link'])

def flatten(a):
	"""列表降维"""
	for each in a:
		if not isinstance(each, list):
			yield each
		else:
			yield from flatten(each)
			
def get_sakuhin_links(catalog,url):
	"""获取假名作品排序列表"""
	a = url[-8:-5]
	if '_' in a:
		p = a[1]
	else:
		p = a[0:2]
	reg_saka = requests.get(url,headers=headers)
	soup_saka = bs(reg_saka.content.decode("utf-8"),'lxml')
	links = soup_saka.findAll(name='a',attrs={"href":re.compile(r'^../card')})
	link = soup_saka.findAll(name='a',attrs={"href":re.compile(r'^sakuhin')})
	try:
		for j in range(2,int(link[-2].text)+1):
			l = list(flatten(links))
			for i in range(len(l)):
				l[i] = {'catalog':catalog + '.'+ p,'sakuhinnname':l[i].text,'link':'http://www.aozora.gr.jp/'+l[i]['href']}
				o = l[i]
				# save_sakuhinn(_sakuhinncatalog,_sakuhinnname,_sakusya,_sakuyhinnlink):
				save_sakuhinn(o['catalog'],o['sakuhinnname'],'Unknown',o['link'])
				
			print("Getting page of "+p+str(j))
			url = "http://www.aozora.gr.jp/index_pages/sakuhin_"+ p + str(j) +".html"
			reg_saka = requests.get(url,headers=headers)
			soup_saka = bs(reg_saka.content.decode("utf-8"),'lxml')
			links = soup_saka.findAll(name='a',attrs={"href":re.compile(r'^../card')})
		
	except Exception as e:
		with open("error_log.txt",'wt') as f:
			f.write(str(e))
		try:
			for j in range(1,5):
				l = list(flatten(links))
				for i in range(len(l)):
					l[i] = {'catalog':catalog + '.'+ p,'sakuhinnname':l[i].text,'link':'http://www.aozora.gr.jp/'+l[i]['href']}
					o = l[i]
					# save_sakuhinn(_sakuhinncatalog,_sakuhinnname,_sakusya,_sakuyhinnlink):
					save_sakuhinn(o['catalog'],o['sakuhinnname'],'Unknown',o['link'])
					
				print("Getting page of "+p+str(j))
				url = "http://www.aozora.gr.jp/index_pages/sakuhin_"+ p + str(j) +".html"
				reg_saka = requests.get(url,headers=headers)
				soup_saka = bs(reg_saka.content.decode("utf-8"),'lxml')
				links = soup_saka.findAll(name='a',attrs={"href":re.compile(r'^../card')})
		except:
			pass
			
def get_work(url):
	"""根据作品详情页网址获取作品原文链接"""
	#url = 'http://www.aozora.gr.jp/cards/001540/card53885.html'
	q = 'card'+url.split('card')[-1]
	reg_work_homepage = requests.get(url,headers=headers)
	soup_work_homepage = bs(reg_work_homepage.content.decode("utf-8"),'lxml')
	links = soup_work_homepage.findAll(name='a',attrs={"href":re.compile(r'^./files/')})[-1]['href']
	link = url.replace(q,'')+links[2:]
	return link


def main():
	import time
	sakusyas,sakuhins = get_catalog_links()
	print("You have links about "+str(len(sakuhins)))
	for i in range(len(sakuhins)):
		print("Getting link "+str(i))
		sakuhins[i] =  {'catalog':sakuhins[i].text,'link':'http://www.aozora.gr.jp/' + sakuhins[i]['href']}
	for i in range(len(sakusyas)):
		print("Getting link "+str(i))
		sakusyas[i] = {'catalog':sakusyas[i].text,'link':'http://www.aozora.gr.jp/' + sakusyas[i]['href']}
	for i in sakusyas:
		print("开始时间： "+str(time.localtime(time.time())))
		#get_saka_links(i['catalog'],i['link'])
		print("结束时间： "+str(time.localtime(time.time())))
	print("<<<<<<<<_____完成作者列表更新_____>>>>>>>>")
	sakuhins = sakuhins[17]#[-4:]#[17]
	for i in sakuhins:
		print("开始时间： "+str(time.localtime(time.time())))
		get_sakuhin_links(i['catalog'],i['link'])
		print("结束时间： "+str(time.localtime(time.time())))
	print("<<<<<<<<_____完成作品列表更新_____>>>>>>>>")
		
if __name__ == "__main__":
	try:
		bulid_db()
	except:
		pass
	finally:
		main()