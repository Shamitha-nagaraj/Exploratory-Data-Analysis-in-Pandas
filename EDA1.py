#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv(r"C:\Users\Shamitha\Downloads\world_population.csv")
df


# In[3]:


pd.set_option('display.float_format', lambda x: '%.2f' % x)


# In[4]:


df


# In[5]:


df.info()


# In[6]:


df.describe()


# In[7]:


df.isnull().sum()


# In[8]:


df.nunique()


# In[13]:


df.sort_values(by="2022 Population", ascending=False).head(10)


# In[14]:


df.corr()


# In[18]:


sns.heatmap(df.corr(), annot = True)
plt.rcParams['figure.figsize'] = (20,7)
plt.show()


# In[23]:


df.groupby('Continent').mean().sort_values(by =  '2022 Population', ascending=False)


# In[21]:


df[df['Continent'].str.contains('Oceania')]


# In[37]:


df2=df.groupby('Continent')[['1970 Population','1980 Population',
       '1990 Population', '2000 Population', '2010 Population',
       '2015 Population', '2020 Population', '2022 Population']].mean().sort_values(by =  '2022 Population', ascending=False)
df2


# In[35]:


df.columns


# In[38]:


df3=df2.transpose()
df3


# In[39]:


df3.plot()


# In[40]:


df.boxplot(figsize=(20,10))


# In[43]:


df.select_dtypes(include='float')


# In[ ]:




