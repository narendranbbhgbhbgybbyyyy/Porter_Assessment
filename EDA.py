#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import csv


# In[98]:


# While importing the csv, enable date parsing in the date specific columns
df = pd.read_csv(r"C:\Users\naren\OneDrive\Documents\olacabs.csv", parse_dates=[4,5], dayfirst=True)


# In[8]:


df.head()


# In[9]:


#filtering cancelled rides by drivers for drop location 'airport'
driver_count = df[(df['cancelled_by'] == 'driver') & (df['drop_loc'] == 'Airport') & (df['driver_id'])]


# In[10]:


driver_count


# In[11]:


# Extract hour from the Request timestamp
 df["RequestHour"] = df["pickup_time"].dt.hour


# In[12]:


df.head()


# In[13]:


df[(df['cancelled_by'] == 'driver') & (df['drop_loc'] == 'Airport') & (df['driver_id'])]


# In[14]:



# Separate 5 different timeslots from the Hour - Dawn, Early Morning, Noon, Late Evening, Night
df["TimeSlot"] = df["RequestHour"].apply(lambda x: "Dawn" if x<=4 else ("Early Morning" if x<=9 else ("Noon" if x<=16 else ("Late Evening" if x<=21 else "Night"))))


# In[15]:


df.head()


# In[16]:


#filtering cancelled rides by drivers for drop location 'airport'
Driver_cancelling = df[(df['cancelled_by'] == 'driver') & (df['drop_loc'] == 'Airport') & (df['driver_id'])]


# In[17]:


Driver_cancelling


# In[18]:


#filtering completed rides by drivers for drop location other tahn 'airport'
data = df[(df['status'] == 4 ) & (df['drop_loc'] != 'Airport') & (df['driver_id'])]


# In[19]:


data


# In[20]:


#combining driver_cancelling and data dataframe
get =  pd.merge(Driver_cancelling, data, on='driver_id', how='right')


# In[21]:


get


# In[22]:


get.describe()


# In[24]:


Driver_cancelling.describe()


# In[25]:


Driver_cancelling = df[(df['cancelled_by'] == 'driver') & (df['drop_loc'] == 'Airport') & (df['driver_id']) & (df['status'] == 5)]


# In[26]:


Driver_cancelling


# In[27]:


Driver_cancelling.describe()


# In[28]:


data = df[(df['status'] == 4 ) & (df['drop_loc'] != 'Airport') & (df['driver_id'])]


# In[29]:


data


# In[30]:


data.describe()


# In[31]:


get =  pd.merge(Driver_cancelling, data, on='driver_id', how='right')


# In[32]:


get


# In[33]:


get.describe()


# In[34]:


Driver_cancelling.groupby(['TimeSlot','status']).size().unstack().plot(kind='bar', stacked=True,figsize=(20, 10))
plt.title('Frequency of Requests by Hour')


# In[35]:


Driver_cancelling.count()


# In[36]:


data.count()


# In[37]:


data.groupby(['TimeSlot','status']).size().unstack().plot(kind='bar', stacked=True,figsize=(20, 10))
plt.title('Frequency of Requests by Hour')


# 
