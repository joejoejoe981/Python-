# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 21:34:30 2019

@author: ASUS
"""

# 引用 NLTK 英文版本的 stopwords
from nltk.corpus import inaugural
from nltk.corpus import stopwords
import nltk

print(stopwords.words('english'))

# 定義函式：計算 inaugural 語料庫不含 stopwords 的比例
def content_fraction(text):
    stopwords = nltk.corpus.stopwords.words('english')
    content = [w for w in text if w.lower() not in stopwords]
    return len(content)/len(text)
print(content_fraction(inaugural.words()))