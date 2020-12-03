# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 20:42:00 2019

@author: ASUS
"""

from nltk.corpus import gutenberg

#print(gutenberg.fileids())

'''
print(gutenberg.raw('austen-emma.txt'))
print(gutenberg.words('austen-emma.txt'))
print(gutenberg.sents('austen-emma.txt'))
'''

for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))

    num_vocab = len(set(w.lower() for w in gutenberg.words(fileid)))

    #print(num_chars, num_words, num_sents)
    
    print(round(num_chars/num_words),
          round(num_words/num_sents),
          round(num_words/num_vocab), fileid)