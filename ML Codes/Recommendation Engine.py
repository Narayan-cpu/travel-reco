#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import re, math
from collections import Counter
import warnings
warnings.filterwarnings('ignore')


# In[2]:


metadata = pd.read_csv('D:/Downloads/Sabre Hack/Datasets/complete_all_data.csv')
metadata['Category'] = metadata['Category'].str.strip()
metadata.dropna(subset=['State'], inplace=True)
metadata.head(3)


# In[3]:


metadata.columns


# In[4]:


metadata["Category"].unique()


# In[5]:


user_df = pd.DataFrame()


# In[6]:


user_df['Category'] = ['heritage', 'beach']
user_df['n_days'] = 8
user_df['State']='Himachal Pradesh'
user_df['Budget'] = 15000


# In[7]:


user_df


# In[8]:


res_df = metadata[metadata['State'].str.strip().apply(lambda x: x.lower()).isin((user_df['State'].apply(lambda x: x.lower())))]
res_df = res_df[res_df['Category'].str.strip().apply(lambda x: x.lower()).isin((user_df['Category'].apply(lambda x: x.lower())))]


# In[9]:


res_df.head(2)


# In[10]:


res_df = res_df.sort_values(['Rating','Place_sentiment', 'Expense (Per Head in Rs.)', 'n_days'], ascending=False)
res_df.reset_index(drop=True, inplace=True)


# In[15]:


n_days_mean = res_df['n_days'].mean()
budget_mean = res_df['Expense (Per Head in Rs.)'].mean()

n_days_mean_l = user_df['n_days'].unique()/n_days_mean
budget_mean_l = user_df['Budget'].unique()/budget_mean

tot_mean = int((n_days_mean_l+budget_mean_l)/2)


# In[17]:


res_df = res_df[:tot_mean]


# In[19]:


res_df = res_df[['Title', 'Description', 'Category','Distance (Km.)', 'Expense (Per Head in Rs.)', 'n_days', 'Boarding_pt',                'Place_sentiment', 'Overall_state_sentiment']]


# In[ ]:




