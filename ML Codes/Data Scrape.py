#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


# In[2]:


driver = webdriver.Chrome('D:/Downloads/Sabre Hack/chromedriver_win32/chromedriver')


# In[3]:


category = []
description = []
title = []

driver.get('https://www.trawell.in/andaman-nicobar/andaman-islands/places-to-visit-things-to-do')


# In[4]:


content = driver.page_source
soup = BeautifulSoup(content)


# In[5]:


for a in soup.findAll('div'):#, href=True):
    category_sc = a.find('span', attrs={'class':'destTitleType'})
    description_sc = a.find('p', attrs={'class':'destDesc'})
    title_sc = a.find('h3', attrs={'class':'destTitle'})
    if category_sc != None:
        category.append(category_sc.text)
    if description_sc != None:
        description.append(description_sc.text)
    if title_sc != None:
        title.append(title_sc.text)


# In[6]:


len(description)


# In[7]:


s1 = pd.Series(title, name='Title')
s2 = pd.Series(description, name='Description')
s3 = pd.Series(category, name='Category')


# In[8]:


df=pd.concat([s1, s2, s3], axis=1)
df = df.drop_duplicates(subset=['Title'])
df.reset_index(drop=True, inplace=True)


# In[9]:


df.shape


# In[10]:


# df.to_csv('D:/Downloads/Sabre Hack/Andaman.csv', index=False)


# In[ ]:




