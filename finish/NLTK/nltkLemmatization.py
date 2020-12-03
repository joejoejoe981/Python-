# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 14:08:01 2019

@author: ASUS
"""
from nltk.tokenize import word_tokenize
# 記得載入 WordNet 語料庫
from nltk.stem import WordNetLemmatizer
wnl = WordNetLemmatizer()
# 要指定單字詞性(pos)
print(wnl.lemmatize('ate', pos='v')) # 得到 eat
print(wnl.lemmatize('better', pos='a')) # 得到 good
print(wnl.lemmatize('dogs')) # 得到 dog