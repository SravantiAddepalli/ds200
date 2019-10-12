
# coding: utf-8

# In[146]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[147]:

data_all = pd.read_csv('Number_of_Schools-Secondary_School.csv')


# In[148]:

data_all


# In[149]:

sec = data_all[data_all['School Type']=='Secondary School'][data_all['India/ State/ UTs'] == 'India']


# In[150]:

low_sec = data_all[data_all['School Type']=='Lower Secondary School'][data_all['India/ State/ UTs'] == 'India']


# In[151]:

scatter = np.vstack((np.array(sec.iloc[0,2:]),np.array(low_sec.iloc[0,2:])))


# In[152]:

scatter


# In[153]:

scatter.shape


# In[249]:

plt.plot(np.array(range(10))+2001, scatter[0], c = 'r')
plt.xlabel('Year')
plt.ylabel('Number of Secondary Schools in India')
plt.title('Trend of number of Secondary Schools in India from 2001 to 2010')
plt.show()
#plt.savefig('plt1.png')


# In[242]:

plt.plot(np.array(range(10))+2001, scatter[1], c = 'g')
plt.xlabel('Year')
plt.ylabel('Number of Lower Secondary Schools in India')
plt.title('Trend of number of Lower Secondary Schools in India from 2001 to 2010')
plt.show()


# In[156]:

sec_2010 = np.array(data_all[data_all['School Type']=='Secondary School']['2010'][1:])


# In[157]:

low_sec_2010 = np.array(data_all[data_all['School Type']=='Lower Secondary School']['2010'][1:])


# In[250]:

plt.scatter(sec_2010,low_sec_2010)
plt.xlabel('No. of Secondary Schools in 2010')
plt.ylabel('No. of Lower Secondary Schools in 2010')
plt.title('Scatter plot of number of Lower Secondary schools v/s number of Secondary schools in 2010')
plt.show()


# In[251]:

sec_2001 = np.array(data_all[data_all['School Type']=='Secondary School']['2001'][1:])
low_sec_2001 = np.array(data_all[data_all['School Type']=='Lower Secondary School']['2001'][1:])
plt.scatter(sec_2001,low_sec_2001)
plt.xlabel('No. of Secondary Schools in 2001')
plt.ylabel('No. of Lower Secondary Schools in 2001')
plt.title('Scatter plot of number of Lower Secondary schools v/s number of Secondary schools in 2001')
plt.show()


# In[184]:

sec_all = np.array(data_all[data_all['School Type']=='Secondary School'][1:].iloc[:,2:])


# In[186]:

sec_all.shape


# In[219]:

sec_2001_val = np.tile(sec_all[:,0],(10,1)).transpose()


# In[220]:

sec_all_norm = np.float32(sec_all) / np.float32(sec_2001_val)


# In[228]:

sec_all_norm[15]
sec_all[15]


# In[233]:

plt.boxplot(sec_all_norm)
plt.xticks(np.array(range(10))+1, np.array(range(10))+2001)
plt.xlabel('Year')
plt.ylabel('Ratio of schools in given year w.r.t. 2001')
plt.title('Trend of increase in number of Secondary schools from 2001 to 2010')
plt.show()


# In[235]:

plt.boxplot(sec_all_norm, showfliers=False)
plt.xticks(np.array(range(10))+1, np.array(range(10))+2001)
plt.xlabel('Year')
plt.ylabel('Ratio of schools in given year w.r.t. 2001')
plt.title('Trend of increase in number of Secondary schools from 2001 to 2010')
plt.show()


# In[236]:

low_sec_all = np.array(data_all[data_all['School Type']=='Lower Secondary School'][1:].iloc[:,2:])
low_sec_2001_val = np.tile(low_sec_all[:,0],(10,1)).transpose()
low_sec_all_norm = np.float32(low_sec_all) / np.float32(low_sec_2001_val)
plt.boxplot(low_sec_all_norm)
plt.xticks(np.array(range(10))+1, np.array(range(10))+2001)
plt.xlabel('Year')
plt.ylabel('Ratio of schools in given year w.r.t. 2001')
plt.title('Trend of increase in number of Lower Secondary schools from 2001 to 2010')
plt.show()


# In[237]:

plt.boxplot(low_sec_all_norm, showfliers=False)
plt.xticks(np.array(range(10))+1, np.array(range(10))+2001)
plt.xlabel('Year')
plt.ylabel('Ratio of schools in given year w.r.t. 2001')
plt.title('Trend of increase in number of Lower Secondary schools from 2001 to 2010')
plt.show()

