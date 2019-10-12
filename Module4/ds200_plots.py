
# coding: utf-8

# In[44]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[45]:

data_all = pd.read_csv('Number_of_Schools-Secondary_School.csv')


# In[46]:

data_all


# In[47]:

sen_sec = data_all[data_all['School Type']=='Senior Secondary School'][data_all['India/ State/ UTs'] == 'India']


# In[48]:

low_sec = data_all[data_all['School Type']=='Lower Secondary School'][data_all['India/ State/ UTs'] == 'India']


# In[49]:

scatter = np.vstack((np.array(sen_sec.iloc[0,2:]),np.array(low_sec.iloc[0,2:])))


# In[50]:

scatter


# In[51]:

scatter.shape


# In[52]:

plt.plot(np.array(range(10))+2001, scatter[0], c = 'r')
plt.xlabel('Year')
plt.ylabel('No. of Senior Secondary Schools in India')
plt.title('Trend of number of Secondary Schools in India from 2001 to 2010')
plt.savefig('Senior Secondary schools trend across years.png',bbox_inches='tight')
plt.show()


# In[53]:

plt.plot(np.array(range(10))+2001, scatter[1], c = 'g')
plt.xlabel('Year')
plt.ylabel('Number of Lower Secondary Schools in India')
plt.title('Trend of number of Lower Secondary Schools in India from 2001 to 2010')
plt.savefig('Lower Secondary schools trend across years.png',bbox_inches='tight')
plt.show()


# In[54]:

sen_sec_2010 = np.array(data_all[data_all['School Type']=='Senior Secondary School']['2010'][1:])


# In[55]:

low_sec_2010 = np.array(data_all[data_all['School Type']=='Lower Secondary School']['2010'][1:])


# In[56]:

plt.scatter(sen_sec_2010,low_sec_2010)
plt.xlabel('No. of Senior Secondary Schools in 2010')
plt.ylabel('No. of Lower Secondary Schools in 2010')
plt.title('Scatter plot of no. of Lower Secondary schools v/s no. of Sr. Secondary schools in 2010')
plt.savefig('Scatter plot 2010.png',bbox_inches='tight')
plt.show()


# In[57]:

sen_sec_2001 = np.array(data_all[data_all['School Type']=='Senior Secondary School']['2001'][1:])
low_sec_2001 = np.array(data_all[data_all['School Type']=='Lower Secondary School']['2001'][1:])
plt.scatter(sen_sec_2001,low_sec_2001)
plt.xlabel('No. of Secondary Schools in 2001')
plt.ylabel('No. of Lower Secondary Schools in 2001')
plt.title('Scatter plot of no. of Lower Secondary schools v/s no. of Sr. Secondary schools in 2001')
plt.savefig('Scatter plot 2001.png',bbox_inches='tight')
plt.show()


# In[58]:

sec_all = np.array(data_all[data_all['School Type']=='Secondary School'][1:].iloc[:,2:])


# In[59]:

sec_all.shape


# In[60]:

sec_2001_val = np.tile(sec_all[:,0],(10,1)).transpose()


# In[61]:

sec_all_norm = np.float32(sec_all) / np.float32(sec_2001_val)


# In[62]:

sec_all_norm[15]
sec_all[15]


# In[63]:

plt.boxplot(sec_all_norm)
plt.xticks(np.array(range(10))+1, np.array(range(10))+2001)
plt.xlabel('Year')
plt.ylabel('Ratio of schools in given year w.r.t. 2001')
plt.title('Trend of increase in number of Secondary schools from 2001 to 2010')
plt.savefig('Box plot Secondary schools.png',bbox_inches='tight')
plt.show()


# In[64]:

plt.boxplot(sec_all_norm, showfliers=False)
plt.xticks(np.array(range(10))+1, np.array(range(10))+2001)
plt.xlabel('Year')
plt.ylabel('Ratio of schools in given year w.r.t. 2001')
plt.title('Trend of increase in number of Secondary schools from 2001 to 2010')
plt.savefig('Box plot Secondary schools no outliers.png',bbox_inches='tight')
plt.show()


# In[65]:

low_sec_all = np.array(data_all[data_all['School Type']=='Lower Secondary School'][1:].iloc[:,2:])
low_sec_2001_val = np.tile(low_sec_all[:,0],(10,1)).transpose()
low_sec_all_norm = np.float32(low_sec_all) / np.float32(low_sec_2001_val)
plt.boxplot(low_sec_all_norm)
plt.xticks(np.array(range(10))+1, np.array(range(10))+2001)
plt.xlabel('Year')
plt.ylabel('Ratio of schools in given year w.r.t. 2001')
plt.title('Trend of increase in number of Lower Secondary schools from 2001 to 2010')
plt.savefig('Box plot Lower Secondary schools.png',bbox_inches='tight')
plt.show()


# In[66]:

plt.boxplot(low_sec_all_norm, showfliers=False)
plt.xticks(np.array(range(10))+1, np.array(range(10))+2001)
plt.xlabel('Year')
plt.ylabel('Ratio of schools in given year w.r.t. 2001')
plt.title('Trend of increase in number of Lower Secondary schools from 2001 to 2010')
plt.savefig('Box plot Lower Secondary schools no outliers.png',bbox_inches='tight')
plt.show()


# In[67]:

sen_sec_all = np.array(data_all[data_all['School Type']=='Senior Secondary School'][1:].iloc[:,2:])
sen_sec_2001_val = np.tile(sen_sec_all[:,0],(10,1)).transpose()
sen_sec_all_norm = np.float32(sen_sec_all) / np.float32(sen_sec_2001_val)
plt.boxplot(sen_sec_all_norm)
plt.xticks(np.array(range(10))+1, np.array(range(10))+2001)
plt.xlabel('Year')
plt.ylabel('Ratio of schools in given year w.r.t. 2001')
plt.title('Trend of increase in number of Senior Secondary schools from 2001 to 2010')
plt.savefig('Box plot Senior Secondary schools.png',bbox_inches='tight')
plt.show()


# In[68]:

plt.boxplot(sen_sec_all_norm, showfliers=False)
plt.xticks(np.array(range(10))+1, np.array(range(10))+2001)
plt.xlabel('Year')
plt.ylabel('Ratio of schools in given year w.r.t. 2001')
plt.title('Trend of increase in number of Senior Secondary schools from 2001 to 2010')
plt.savefig('Box plot Senior Secondary schools no outliers.png',bbox_inches='tight')
plt.show()


# In[ ]:



