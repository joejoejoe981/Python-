# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 14:08:01 2019

@author: ASUS
"""
import nltk

from nltk.tokenize import word_tokenize
# 測試字句
sent = "the the the dog, dog some other words that we do not care about"
# 取出每個單字
list=[word for word in word_tokenize(sent)]
#得到結果為 ['the', 'the', 'the', 'dog', ',', 'dog', 'some', 'other', 'words', 'that', 'we', 'do', 'not', 'care', 'about']
# 去除重複，並排序
vacabulary = sorted(set(list)) 
#得到結果為 [',', 'about', 'care', 'do', 'dog', 'not', 'other', 'some', 'that', 'the', 'we', 'words']
# 求得每個單字的出現頻率

freq = nltk.FreqDist(list)
#得到結果為 FreqDist({'the': 3, 'dog': 2, 'care': 1, 'some': 1, 'other': 1, ',': 1, 'we': 1, 'that': 1, 'words': 1, 'about': 1, ...})

# 作圖
freq.plot()