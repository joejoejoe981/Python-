import re

from Lab10.element import Tag

class Htmlparser:
    @staticmethod
    def string_to_tag(string):
        p = r'(<.*?>)(.*)(</.*?>)'
        match = m = re.search(p, string)
        if match:
            print('解析成功')
            g1 = m.group(1)
            print(g1)
            g2 = m.group(2)
            print(g2)
        else:
            print('解析失敗')


