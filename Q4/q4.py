#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import numpy as np

df = pd.read_csv('gender2.csv',encoding='cp949', index_col=0)
#print(df)
df = df.loc[:,["2022년_계_총인구수","2022년_남_총인구수","2022년_여_총인구수"]]
#print(df)
col_list = list(df.columns)
col_list[0] = "Total"
col_list[1] = "Male"
col_list[2] = "Female"
df.columns = col_list
print(df)


# In[ ]:





# In[ ]:




