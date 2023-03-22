#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# # Load dataset

# In[7]:


epl_df = pd.read_csv('D:\Python\Projects\Python Projects\Football Data Analysis\\Football.csv')
epl_df.head()


# In[9]:


epl_df.info()


# In[11]:


epl_df.describe()


# In[13]:


epl_df.isna().sum()


# In[15]:


# Creating 2 new columns

epl_df['MinsPerMatch'] = (epl_df['Mins'] / epl_df['Matches']).astype(int)
epl_df['GoalsPerMatch'] = (epl_df['Goals'] / epl_df['Matches']).astype(float)
epl_df.head()


# In[17]:


# Total Goals

Total_Goals = epl_df['Goals'].sum()
print(Total_Goals) 


# In[19]:


# Penalty Goals

Total_PenaltyGoals = epl_df['Penalty_Goals'].sum()
print(Total_PenaltyGoals)


# In[21]:


# Penalty Attempts

Total_PenaltyAttempts = epl_df['Penalty_Attempted'].sum()
print(Total_PenaltyAttempts)


# In[23]:


# Pie chart for penaties missed vs scored

plt.figure(figsize = (13, 6))
pl_not_scored = epl_df['Penalty_Attempted'].sum() - Total_PenaltyGoals
data = [pl_not_scored, Total_PenaltyGoals]
labels = ['Penalties_missed', 'penalties_scored']
color = sns.color_palette('Set2')
plt.pie(data, labels = labels, colors = color, autopct = '%.0f%%')
plt.show()


# In[25]:


# Unique Positions

epl_df['Position'].unique()


# In[27]:


# Total FW players

epl_df[epl_df["Position"] == 'FW']


# In[29]:


# Players from different nations

np.size((epl_df['Nationality'].unique()))


# In[31]:


# Most players from which countries

nationality = epl_df.groupby('Nationality').size().sort_values(ascending = False)
nationality.head(10).plot(kind='bar', figsize=(12, 6), color=sns.color_palette('magma'))


# In[33]:


# Clubs with maximum players in their squad

epl_df['Club'].value_counts().nlargest(5).plot(kind = 'bar', color=sns.color_palette('viridis'))


# In[35]:


# Clubs with least players in their squad

epl_df['Club'].value_counts().nsmallest(5).plot(kind = 'bar', color=sns.color_palette('viridis'))


# In[37]:


# Players based on their age group

Under20 = epl_df[epl_df['Age'] <= 20]
age20_25 = epl_df[(epl_df['Age'] > 20) & (epl_df['Age'] <= 25)]
age25_30 = epl_df[(epl_df['Age'] > 25) & (epl_df['Age'] <= 30)]
Above30 = epl_df[epl_df['Age'] > 30]  


# In[39]:


x = np.array([Under20['Name'].count(), age20_25['Name'].count(),age25_30['Name'].count(),Above30['Name'].count()])
mylabels = ['<=20', '>20 & <=25', '>25 & <=30', ">30"]
plt.title('Total Players with age groups', fontsize = 20)
plt.pie(x, labels = mylabels, autopct='%.1f%%')
plt.show()


# In[41]:


# Total under 20 players in each club

players_under_20 = epl_df[epl_df['Age'] < 20]
players_under_20['Club'].value_counts().plot(kind = 'bar', color = sns.color_palette('cubehelix'))


# In[43]:


# Under 20 players in Manchester United

players_under_20[players_under_20["Club"]=='Manchester United']


# In[44]:


# Under 20 players in Chelsea

players_under_20[players_under_20["Club"]=='Chelsea']


# In[45]:


# Aversge age of players in each club

plt.figure(figsize=(12, 6))
sns.boxplot(x = 'Club', y = 'Age', data = epl_df)
plt.xticks(rotation = 90)


# In[47]:


num_player = epl_df.groupby('Club').size()
data = epl_df.groupby('Club')['Age']


# In[48]:


# Top 10 assists

top_10_assists = epl_df[['Name', 'Club', 'Assists', 'Matches']].nlargest(n=10, columns = 'Assists')
top_10_assists


# In[49]:


# Most goals by players

top_10_goals = epl_df[['Name', 'Club', 'Goals', 'Matches']].nlargest(n = 10, columns = 'Goals')
top_10_goals


# In[50]:


# Goals per match

top_10_goalspermatch = epl_df[['Name', 'GoalsPerMatch', 'Club', 'Matches', 'Goals']].nlargest(n = 10, columns = 'GoalsPerMatch')
top_10_goalspermatch


# In[52]:


# Pie chart - Goals with assists and without assists

plt.figure(figsize=(14, 7))
assists = epl_df['Assists'].sum()
data = [Total_Goals - assists, assists]
labels = ['Goals without assists', 'Goals with assists']
color = sns.color_palette('Set1')
plt.pie(data, labels = labels, colors = color, autopct = '%.0f%%')
plt.show


# In[ ]:




