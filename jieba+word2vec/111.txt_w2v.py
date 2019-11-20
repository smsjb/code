#!/usr/bin/env python
# coding: utf-8

# In[17]:


# -*- coding: utf-8 -*-# -*- coding: utf-8 -*-

import jieba
from gensim.models import word2vec

sentences = word2vec.LineSentence('111.txt')
model = word2vec.Word2Vec(sentences, hs=1,min_count=1,window=10,size=5)

for key in model.wv.similar_by_word('吃', topn =7):
    print(key)


# In[ ]:




