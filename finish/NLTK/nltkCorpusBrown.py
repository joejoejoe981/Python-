# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 20:48:32 2019

@author: ASUS
"""

from nltk.corpus import brown
import nltk
'''
print(brown.categories())

print(brown.categories("cc01"))

print(brown.words(categories='reviews'))



reviews_text = brown.words(categories='reviews')
fdist = nltk.FreqDist(w.lower() for w in reviews_text)
modals = ['can', 'could', 'may', 'might', 'must', 'will']
for m in modals:
    print(m + ':', fdist[m], end=' ')

'''
cfd = nltk.ConditionalFreqDist((genre, word) 
    for genre in brown.categories()
    for word in brown.words(categories=genre))
genres = ['reviews', 'hobbies', 'romance', 'humor']
modals = ['can', 'could', 'may', 'might', 'must', 'will']
cfd.tabulate(conditions=genres, samples=modals)
