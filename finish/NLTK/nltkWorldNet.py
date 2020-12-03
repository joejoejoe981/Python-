# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 11:33:13 2020

@author: ASUS
"""

# 找synset，以 motorcar 為例
from nltk.corpus import wordnet as wn

'''
print(wn.synsets('motorcar'))

# 也可以替換改找卡車的synset
print(wn.synsets('trunk'))

# synset 裡的字詞
print(wn.synset('car.n.01').lemma_names())

# 列舉多義字的同義字
for synset in wn.synsets('trunk'):
    print(synset.lemma_names())
'''    
'''
# 查找 motorcar 所屬的 synset 定義
print(wn.synset('car.n.01').definition())

# 查找 trunk 所屬的 synset 定義
print(wn.synset('trunk.n.01').definition())
'''

'''
# 尋找 motorcar 的上位詞組
motorcar = wn.synset('car.n.01')
types_of_motorcar = motorcar.hypernyms()
print(types_of_motorcar)
'''

'''
# 尋找 motorcar 的下位詞組
motorcar = wn.synset('car.n.01')
types_of_motorcar = motorcar.hyponyms()
print(types_of_motorcar)


# 找到下位詞組後後，再從 synset 找出單詞（以詞為中心）
print(sorted(lemma.name() for synset in types_of_motorcar for lemma in synset.lemmas()))
'''

'''
# 完整路徑（上位詞組再往上走）
motorcar = wn.synset('car.n.01')
print(motorcar.hypernym_paths())
'''

'''
# 直指頂端上位詞組
motorcar = wn.synset('car.n.01')
print(motorcar.root_hypernyms())
'''

'''
# 以鯨魚為例
right = wn.synset("right_whale.n.01") 
minke = wn.synset("minke_whale.n.01")
# 「露脊鯨」與「小鬚鯨」在上位詞組中最低位的詞組
print(right.lowest_common_hypernyms(minke))

# 露脊鯨 vs 虎鯨
orca = wn.synset("orca.n.01")
print(right.lowest_common_hypernyms(orca))
    
# 露脊鯨 vs 陸龜
tortoise = wn.synset("tortoise.n.01")
print(right.lowest_common_hypernyms(tortoise))

# 露脊鯨 vs 小說
novel = wn.synset("novel.n.01")
print(right.lowest_common_hypernyms(novel))



# 計算由當前 synset 而上的階層數
print(wn.synset('baleen_whale.n.01').min_depth())
print(wn.synset('whale.n.02').min_depth())
print(wn.synset('vertebrate.n.01').min_depth())
print(wn.synset('entity.n.01').min_depth())

# 上下位詞組結構的相似程度 (數字接近1代表path越像)
print(right.path_similarity(right))    #露脊鯨和自己本身
print(right.path_similarity(minke))    #露脊鯨和小鬚鯨
print(right.path_similarity(orca))     #露脊鯨和虎鯨
print(right.path_similarity(tortoise)) #露脊鯨和陸龜
print(right.path_similarity(novel))    #露脊鯨和小說
'''