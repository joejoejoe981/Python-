
class Tag:
    def __init__(self,name=None,content=None, **attrs):
        self.name = name
        self.content = content
        self.attrs = attrs #attrs是自動（內建）將資料裝箱的字典
        self.creat_object_attr()

    #定義初始輸入的值是什麼屬性
    # def __str__(self):
    #         s = '<{0}><{1}></{0}>'.format(self.name,self.content)
    #         return s
    #定義輸出的值是什麼屬性
    def creat_object_attr(self):
        for k,v in self.attrs.items():
            self.__setattr__(k,v)   #__setattr__為python內建函示,可動態產生物件屬性

    def __str__(self):
        #產生屬性字串
        #id = "special"class = "headline"
        s_attrs = ''
        for k,v in self.attrs.items():
            s_attrs += '{}="{}"'.format(k,v)
        s = '<{0}{2}>{1}</{0}>'.format(self.name,self.content,s_attrs)
        #                                 {0}        {1}         {2}
        return s
