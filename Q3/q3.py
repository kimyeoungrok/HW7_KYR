#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np

df = pd.DataFrame(np.array([[1000,25],[280,120],[900,30]]), index=['store1','store2','store3'], columns=['unit price', 'number'])
print(df)
df['total price'] = df['unit price'] * df['number']
print(df)
df2 = df.sort_values(by="total price", ascending=False)
print(df2.head(2))


# In[ ]:




