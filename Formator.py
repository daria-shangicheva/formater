#!/usr/bin/env python
# coding: utf-8

# In[25]:


import os
import shutil
import sys


# In[ ]:


file_resource="/Users/user/Documents/resource/"
file_final="/Users/user/Documents/final/"


# In[ ]:


file_resource=sys.argv[0]
file_final=sys.argv[1]


# In[26]:


name_dict={'1x':'drawable-mdpi','1.5x':'drawable-hdpi','2x':'drawable-xhdpi','3x':'drawable-xxhdpi',          '4x':'drawable-xxxhdpi'}


# In[51]:


for el in name_dict:
    if os.access(file_final+name_dict.get(el),os.F_OK)==False:
        os.mkdir(file_final+name_dict.get(el))  


# In[53]:


file_names=os.listdir(path=file_resource) 


# In[54]:


for el in file_names:
    new_name=el.split("@")[0]
    if el!=new_name:
        new_rep=name_dict.get(el.split("@")[1][:-4])
        shutil.copy(file_resource+el, file_final+new_rep+'/'+new_name+".png")       

