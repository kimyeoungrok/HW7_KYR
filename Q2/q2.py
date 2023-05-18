#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np

Docs = np.array([[1,1,0,1,0,1],
         [1,1,1,0,1,0],
         [1,1,0,1,0,0]])
Query = np.array([1,1,0,0,1,0])

doc1 = np.dot(Docs[0],Query) / (np.linalg.norm(Docs[0]) * np.linalg.norm(Query))
doc2 = np.dot(Docs[1],Query) / (np.linalg.norm(Docs[1]) * np.linalg.norm(Query))
doc3 = np.dot(Docs[2],Query) / (np.linalg.norm(Docs[2]) * np.linalg.norm(Query))

print("doc1 = {:.2f}".format(doc1))
print("doc2 = {:.2f}".format(doc2))
print("doc3 = {:.2f}".format(doc3))


# In[ ]:




