# ex01
# import re
# p = '\d{4}-\d{1,2}-\d{1,2}'
# print(p)
# s = input('請輸入日期（yyyy-mm-dd):')
# match = re.search(p,s)
# if match:
#     print('格式正確')
# else:
#     print('你智障嗎？')

# ex02
# import re
# # s = 'It was the best of times'
# # p = r'w.s'
# s = input('請輸入資料內容：')
# p = input('請輸入找尋資料條件：')
# m = re.search(p,s)
# if m:
#     text = m.group()
#     print(text)

# ex03
# import re
# s = input('請輸入資料內容：')
# p = input('請輸入找尋資料條件：')
# a = re.findall(p,s)
# print(a)
# for x in a:
#     print(x)
#
# ex04
import re
s = '吳哲佑 email 是 joe355289@gmail.com'
p = r'(\S+?)\.(\S+?)\@(\S+)'
m = re.search(p, s)
print(s)
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
