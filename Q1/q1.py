#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np

arr = np.array([[1,2],
               [3,4]])
eig_val, eig_vec = np.linalg.eig(arr)
determinant = np.linalg.det(arr)
print("Eigenvalues : {}".format(eig_val))
print("Eigenvectors : {}".format(eig_vec))
print("Determinant : {}".format(int(determinant)))

vec1 = np.array([1,2,3])
vec2 = np.array([4,5,6])
cross_product = np.cross(vec1, vec2)
print("Cross product : {}".format(cross_product))
A = np.array([[1,2,-2],
             [2,1,-5],
             [1,-4,1]])
B = np.array([-15,-21,18])

x = np.linalg.solve(A,B)
print("Solution : {}".format(x))


# In[ ]:




