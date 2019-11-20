#!/usr/bin/env python
# coding: utf-8

# In[5]:


from gensim.models import word2vec
import jieba


# In[8]:


text = u"勞工是心中最軟的一塊"

sentence = []
sentences = []


for word in jieba.cut(text, cut_all=False ):
    sentence.append(word)
    
sentences.append(sentence)

print(sentences)


# In[3]:


model = word2vec.Word2Vec(sentences, size=10, min_count=1, window=1)


# In[4]:


print(model)


# In[5]:


print(model['勞工'])


# In[6]:


print(model["勞工"])


# In[7]:


print(model['勞基法'])


# In[15]:


x = model.most_similar(u"勞工", topn=1)


# In[18]:


for i in x:
    print(i[0], i[1])


# In[19]:


y=model.doesnt_match(u"勞工 最軟 的".split())


# In[20]:


print(y)


# In[ ]:




