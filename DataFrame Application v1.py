#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd
import numpy as np
# Question Number	Company background	Details	Points (Total 23)

filepath = "C:\\Users\\jyoth\\Documents\\prashant\\Python Scripts\\DataFrame Application\\ZS.csv"
zs = pd.read_csv(filepath)
#zs.head()
# SQL Query Select Question Number, Company background,Details,Points (Total 23) from zs LIMIT 5; 
#zs[['Question Number','Company background','Details','Points (Total 23)']].head(5)
#zs.assign(Points = zs['Points (Total 23)'].notna()).head(5)
#Filter the rows with blank in Points(total 23) column
#zs[zs['Points (Total 23)'].notna()]
#Unfortunately there are some rows with zero in them
#Filter the rows with value 1 in Points(total 23) column
zs[(zs['Points (Total 23)']==1) | (zs['Points (Total 23)']==0.5) | (zs['Points (Total 23)']==2) ]


# In[ ]:




