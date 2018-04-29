"""#### bulid_db()
#### get_sakusya()
#### get_sakuhinn()
#### sakusyainsert(_sakusyacatalog,_sakusyaname,_sakuhinn,_sakusyalink)
#### sakuhinninsert(_sakuhinncatalog,_sakuhinnname,_sakusya,_sakuyhinnlink)
#### get_onesakuhinn(_name)
#### get_onesakusya(_name)
#### get_kanasakuhinn(_sakuhinncatalog)
#### get_kanasakusya(_sakusyacatalog)"""
import sqlite3

def get_con(func):
    data_path = r"sources.db"

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
"""sakuhinnid,sakuhinncatalog,sakuhinnname,sakusya,sakuyhinnlink"""

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
        
def sakuhinninsert(_sakuhinncatalog,_sakuhinnname,_sakusya,_sakuyhinnlink):
    """插入一行sakuhinn数据"""
    try:
        print("正在插入作品列表： " + _sakuhinnname)
        data_path = r"sources.db"
        conn = sqlite3.connect(data_path, check_same_thread = False)
        conn.text_factory = str
        cur = conn.cursor()
        data = (_sakuhinncatalog,_sakuhinnname,_sakusya,_sakyhinnlink)
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
        data_path = r"sources.db"
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
        data_path = r"sources.db"
        conn = sqlite3.connect(data_path, check_same_thread = False)
        conn.text_factory = str
        cur = conn.cursor()
        data = (_name,)
        ins = 'select * from sakuhinndata where sakushinnname = ?'
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
        data_path = r"sources.db"
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
        data_path = r"sources.db"
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
        data_path = r"sources.db"
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

