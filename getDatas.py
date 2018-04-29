import sqlite3


def get_con(func):
    data_path = r"sources2_using.db"

    def sql_exc():
        conn = sqlite3.connect(data_path, check_same_thread=False)
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


def get_Nsakuhinn(_name):
    """根据ID获取某一作品数据"""
    try:
        print("正在查询第 {} 个作品信息！".format(_name))
        data_path = r"sources2_using.db"
        conn = sqlite3.connect(data_path, check_same_thread=False)
        conn.text_factory = str
        cur = conn.cursor()
        data = (_name, )
        ins = 'select * from sakuhinndata where SAKUHINNID = ?'
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
        return ["没获取到数据"]


def get_Nsakusya(_name):
    """根据ID获取某一作品数据"""
    try:
        print("正在查询第 {} 个作者信息！".format(_name))
        data_path = r"sources2_using.db"
        conn = sqlite3.connect(data_path, check_same_thread=False)
        conn.text_factory = str
        cur = conn.cursor()
        data = (_name, )
        ins = 'select * from SAKUSYADATA where SAKUSYAID = ?'
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
        return ["没获取到数据"]


def get_onesakuhinn(_name):
    """根据作品名获取某一作品数据"""
    try:
        print("正在查询作品信息： " + _name)
        data_path = r"sources2_using.db"
        conn = sqlite3.connect(data_path, check_same_thread=False)
        conn.text_factory = str
        cur = conn.cursor()
        data = (_name, )
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
    """根据作者名获取某一作者数据"""
    try:
        print("正在查询作者信息： " + _name)
        data_path = r"sources2_using.db"
        conn = sqlite3.connect(data_path, check_same_thread=False)
        conn.text_factory = str
        cur = conn.cursor()
        data = (_name, )
        # ins = 'select * from sakusyadata where sakusyaname = ?'
        ins = 'select * from sakusyadata where sakusyadata.sakusyaname = ?'
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
        data_path = r"sources2_using.db"
        conn = sqlite3.connect(data_path, check_same_thread=False)
        conn.text_factory = str
        cur = conn.cursor()
        data = (_sakuhinncatalog, )
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
        data_path = r"sources2_using.db"
        conn = sqlite3.connect(data_path, check_same_thread=False)
        conn.text_factory = str
        cur = conn.cursor()
        data = (_sakusyacatalog, )
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


def get_sakuhinnCa():
    """获取作品假名分类列表"""
    a = [i[1] for i in get_sakuhinn()]
    b = sorted(set(a), key=a.index)
    return b


def get_sakusyaCa():
    """获取作者假名分类列表"""
    a = [i[1] for i in get_sakusya()]
    b = sorted(set(a), key=a.index)
    return b
