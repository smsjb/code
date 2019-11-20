#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests 
from bs4 import BeautifulSoup
 
url='https://www.medicaltravel.org.tw/Query.aspx?' ##要打搜索引擎!!!!!!!!!!

key={'q' : '癌症'} ##查詢參數
result=requests.get(url, params=key)
print(result.url)

if result.status_code == requests.codes.ok:
    soup=BeautifulSoup(result.text, 'html.parser')
    
items=soup.select('a[href^="Act"]')



for i in items:
    print("標題: " + i.text)


# In[1]:


from gensim.models import word2vec
import jieba
import requests 
from bs4 import BeautifulSoup
 
url='https://www.medicaltravel.org.tw/Query.aspx?' ##要打搜索引擎!!!!!!!!!!

key={'q' : '癌症'} ##查詢參數
result=requests.get(url, params=key)
print(result.url)

if result.status_code == requests.codes.ok:
    soup=BeautifulSoup(result.text, 'html.parser')
    
items=soup.select('a[href^="Act"]')



for i in items:
    sentence = []
    sentences = []


    for word in jieba.cut(i.text, cut_all=False ):
        sentence.append(word)
    
    sentences.append(sentence)
    print("標題: " + i.text)
    print(sentences)


# In[ ]:




