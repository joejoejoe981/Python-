# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 21:27:35 2019

@author: ASUS
"""

import nltk
import matplotlib.pyplot as plt

# 英文範例
sentence = """At eight o'clock on Thursday morning
... Arthur didn't feel very good."""

'''
print(sentence.split())
print(nltk.word_tokenize(sentence))
'''

from nltk.corpus import inaugural
'''
print(inaugural.fileids())

sent = inaugural.raw('1789-Washington.txt')
print(nltk.sent_tokenize(sent))
'''

cfd = nltk.ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in inaugural.fileids() # 取出年份
    for w in inaugural.words(fileid)  # 歷屆文本的字詞
    for target in ['america', 'citizen'] # 篩選字詞
    if w.lower().startswith(target)) # 字詞 American’s 也能納入計算
plt.figure(figsize=(20,10))
cfd.plot()