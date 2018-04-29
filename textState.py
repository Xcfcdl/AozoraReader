from getDatas import (get_kanasakuhinn, get_kanasakusya, get_Nsakuhinn,
                      get_sakuhinn, get_sakuhinnCa, get_sakusya, get_sakusyaCa,
                      get_onesakuhinn, get_onesakusya)


class LN():
    # 上中下状态机？？
    def __init__(
            self,
            location,
            url,
    ):
        self.location = location
        self.url = url

    def get_info(self):
        return {'location': self.location}


class TextState():
    # 文章状态维护类
    def __init__(self):
        self.sakuhinndatas = get_sakuhinn()
        self.sakusyadatas = get_sakusya()
        self.sakuhinncount = len(self.sakuhinndatas)
        self.sakusyacount = len(self.sakusyadatas)
        self.now = LN(0, '没有文章！')
        self.last = LN(-1, '没有文章！')
        self.next = LN(1, '没有文章')
        self.status = "正常运行"
        self.set_now(1)
        self.update_text_url()

    def set_now(self, N=0):
        self.now.location = N
        if self.now.location > self.sakuhinncount:
            self.status = "数量超出作品数：{}".format(self.sakuhinncount)
            print(self.status)
            self.now.location = self.sakuhinncount
        if self.now.location < 1:
            self.status = "数量小于0"
            print(self.status)
            self.now.location = 1
        self.last.location = self.now.location - 1
        self.next.location = self.now.location + 1
        self.update_text_url()

    def last_text(self):
        self.set_now(self.last.location)

    def next_text(self):
        self.set_now(self.next.location)

    def update_text_url(self):
        try:
            self.now.url = get_Nsakuhinn(self.now.location)[0][-1].replace(
                '../', '')
        except Exception as e:
            print(e)
            pass
        try:
            self.last.url = get_Nsakuhinn(self.last.location)[0][-1].replace(
                '../', '')
        except Exception as e:
            print(e)
            self.last.url = "http:\\www.baidu.com"
        try:
            self.next.url = get_Nsakuhinn(self.next.location)[0][-1].replace(
                '../', '')
        except Exception as e:
            print(e)
            self.next.url = "http:\\www.baidu.com"

    def get_url(self):
        return self.now.url

    def get_l_item(self, name=None):
        # 接入作品名，查出文章数据项，更新状态机
        if name is not None:
            print(get_onesakuhinn(name))
            try:
                id_n = get_onesakuhinn(name)[0][0]
            except Exception:
                id_n = get_onesakusya(name)[0][0]
                id_n = 1
            self.set_now(id_n)
        else:
            print("2无法 接入作品名，查出文章数据项，更新状态机")
            pass
