# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 11:47:23 2020

@author: ASUS
"""

# 引用詞幹提取器
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer
# 初始化
pst = PorterStemmer()
lst = LancasterStemmer()
snow = SnowballStemmer('english')  #需定義語言

# 使用 (以Porter Stemmer為例）
print(pst.stem('eating'))
print(pst.stem('eats'))
