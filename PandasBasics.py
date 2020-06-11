#!/usr/bin/env python
# coding: utf-8

# # Pandas Series

# In[1]:


import pandas as pd


# In[ ]:


# create series object using list
data = [1,2,3,4,5]
series = pd.Series(data)


# In[3]:


series


# In[4]:


data2 = [23,34,90,'sneha',2.2,'s']
series2 = pd.Series(data2)
series2


# In[5]:


type(series)


# In[7]:


type(series2)


# In[14]:


# create series object using dictionary
dataX = {'k1':10,'k2':20,'k3':30}
s = pd.Series(dataX)
s


# In[16]:


series = pd.Series([23,44,56,11,23],index=['i','ii','iii','iv','v'])
series


# # Pandas DataFrame

# In[17]:


import pandas as pd


# In[18]:


dataList = [2,3,4,51,8,9]


# In[20]:


df = pd.DataFrame(dataList) # create df object using list


# In[21]:


df


# In[22]:


dict = {'fruits':['banana','apple','mango','grapes','pineapple'],'count':[12,6,18,40,29]}


# In[23]:


df = pd.DataFrame(dict) # create df object using dictionary


# In[24]:


df


# In[37]:


series = pd.Series([11,22,33,44],index = ['l1','l2','l3','l4']) # create df object using series


# In[38]:


df = pd.DataFrame(series)


# In[39]:


df


# In[40]:


import numpy as np


# In[41]:


array = np.array([[1,2,3],[4,5,6],[7,8,9]]) # create df object using numpy array


# In[42]:


df = pd.DataFrame(array)


# In[43]:


df


# In[44]:


pd.DataFrame([1,2,3,4,5])


# In[45]:


pd.DataFrame({'k1':[11,22,33],'k2':[111,222,333],'k3':[1111,2222,3333]})


# In[46]:


pd.DataFrame({'k1':[11,22,33],'k2':[111,222,333],'k3':[1111,2222,3333]},index = ['x','y','z'])


# In[48]:


pd.DataFrame(pd.Series(['a','sneha',12,12.3],index = ['p','q','r','s']))


# In[49]:


pd.DataFrame(np.array([[12,23,45],[21,32,43]]),index = ['row1','row2'])


# In[50]:


s = pd.Series(['a','sneha',12,12.3],index = ['p','q','r','s'])


# In[52]:


pd.DataFrame({'values':s})


# In[66]:


t = np.array([[12,23,45],[21,32,43]])


# In[68]:


pd.DataFrame({'col1':t[0],'col2':t[1]},index = ['row1','row2','row3'])


# # DataFrame Merge Operation

# In[69]:


import pandas as pd


# In[70]:


# creating first df
player = ['player1','player2','player3']
point = [8,9,10]
title = ['g1','g2','g3']


# In[71]:


df1 = pd.DataFrame({'player':player,'point':point,'title':title})


# In[72]:


df1


# In[73]:


# creating second df
player = ['player1','player5','player6']
power = ['punch','kick','boxing']
title = ['g1','g5','g6']


# In[74]:


df2 = pd.DataFrame({'player':player,'power':power,'title':title})


# In[75]:


df2


# In[76]:


df1.merge(df2,on = 'player',how = 'inner') # inner merge


# In[77]:


df1.merge(df2,on = 'title',how = 'inner')


# In[78]:


df1.merge(df2,on = 'player',how = 'left') # left merge


# In[79]:


df1.merge(df2,on = 'player',how = 'right') # right merge


# In[80]:


df1.merge(df2,on = 'player',how = 'outer') #  outer merge


# In[81]:


df2.merge(df1,on='title',how = 'outer')


# # DataFrame Join Operation

# In[82]:


# creating first df
player = ['player1','player2','player3']
point = [8,9,10]
title = ['g1','g2','g3']


# In[84]:


df1 = pd.DataFrame({'player':player,'point':point,'title':title},index = ['l1','l2','l3'])
df1


# In[93]:


players = ['player1','player5','player6']
power = ['kick','punch','boxing']
titles = ['g1','g5','g6']


# In[94]:


df2 = pd.DataFrame({'players':players,'power':power,'titles':titles},index = ['l2','l3','l4'])
df2


# In[95]:


df1.join(df2,how = 'inner')


# In[96]:


df1.join(df2,how = 'left')


# In[97]:


df1.join(df2,how = 'right')


# In[98]:


df1.join(df2,how = 'outer')


# # Concatination of two dataframes

# In[102]:


pd.concat([df1,df2],sort=True)


# # Data Analysis using Pandas

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv("mtcars.csv")


# In[3]:


df


# In[4]:


df.head()


# In[5]:


df.head(3)


# In[6]:


df.tail()


# In[7]:


df.tail(3)


# In[8]:


type(df)


# In[14]:


df.shape


# In[17]:


df.info(null_counts = True)


# In[18]:


df.mean()


# In[19]:


df.median()


# In[20]:


df.std()


# In[21]:


df.min()


# In[22]:


df.max()


# In[23]:


df.count()


# In[25]:


df.describe()


# # Data Cleaning using Pandas

# In[26]:


import pandas as pd


# In[27]:


df = pd.read_csv("mtcars.csv")


# In[28]:


df


# In[29]:


df = df.rename(columns = {'unnamed:1':'model'})


# In[30]:


df


# In[31]:


df = df[{'model','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb'}].corr()


# In[32]:


df


# In[33]:


df.mpg


# In[34]:


df = pd.read_csv("mtcars.csv")


# In[35]:


df


# In[36]:


df.mpg = df.mpg.astype(int)


# In[37]:


df


# In[38]:


df.gear = df.gear.astype(float)


# In[39]:


df


# In[40]:


df = pd.read_csv("mtcars.csv")


# In[41]:


df


# In[49]:


df


# In[52]:


df = pd.read_csv("mtcars.csv")
df


# In[51]:


df.drop(columns = ['carb','gear','am'])


# In[53]:


df.vs = df.vs.fillna(df.vs.mean())


# In[54]:


df


# # Data Manipulation using Pandas

# In[55]:


import pandas as pd


# In[56]:


df = pd.read_csv("mtcars.csv")


# In[57]:


df


# In[58]:


df.iloc[:1] 


# In[59]:


df.iloc[:,1]


# In[60]:


df.iloc[0:5,4]


# In[61]:


df.iloc[25:,4:]


# In[62]:


df.iloc[1,1]


# In[63]:


df.iloc[0,:]


# In[64]:


df.iloc[:,0]


# In[65]:


df.loc[:,"mpg"]


# In[66]:


df.loc[1:5,"gear"]


# In[67]:


df['am'] = 10


# In[68]:


df


# In[69]:


df['gear'] = 0


# In[70]:


df


# In[71]:


df = pd.read_csv("mtcars.csv")
df


# In[72]:


f = lambda x:x**2


# In[73]:


df['am'] =df['am'].apply(f)


# In[74]:


df


# In[75]:


df['gear'] = df['gear'].apply(f)


# In[76]:


df


# In[3]:


import pandas as pd
df = pd.read_csv("mtcars.csv")
df


# In[16]:


df = df.sort_values(by = "gear")
df


# In[13]:


df['cyl'] >5


# In[17]:


df = df.sort_values(by = "gear",ascending = False)
df


# In[ ]:




