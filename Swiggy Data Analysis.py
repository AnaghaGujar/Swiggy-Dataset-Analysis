#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


df = pd.read_csv(r'c:\swiggy.csv')


# In[3]:


df.head()


# In[4]:


df.info()


# In[5]:


#Checking for null values
df.isnull().sum()


# In[6]:


#Replacing space with '_' so it will be convinient to access the column in the future
df.columns=[column.replace(" ", "_") for column in df.columns.to_list()]


# In[7]:


df.head()


# # Restaurants per City

# In[8]:


rest_count = df['Restaurant'].groupby(df['City']).count()


# In[9]:


rest = rest_count.sort_values(ascending = False)
rest


# In[71]:


rest.plot(kind='bar',figsize=(10,8) )
plt.title('Restaurant count per City', weight ='bold', size=14) 
plt.ylabel('Restaurants Count')


# Kolkata city has more restaurants which work with Swiggy as per dataset.

# # Restaurants with High Average Rating as per City

# In[51]:


df['Avg_ratings'].max()


# In[52]:


# To get the maximum values of each row
df.loc[df['Avg_ratings'].idxmax()]


# In[53]:


# High Average ratings restaurant of Swiggy
high_avg_ratings=df[['City','Restaurant','Avg_ratings']][df.Avg_ratings == df.Avg_ratings.max()]
high_avg_ratings.style.hide_index()


# In[58]:


#High average ratings restaurant count as per cities
city_count = high_avg_ratings['Restaurant'].groupby(high_avg_ratings['City']).count().sort_values(ascending = False)
city_count


# In[73]:


city_count.plot(kind='barh',color='#86bf91', figsize=(9,6))
#city_count.plot(kind='bar', figsize=(8,8))
plt.title('High average ratings restaurant count as per cities', weight='bold', size = 14) 
plt.xlabel('Number of high avg rating restaurant count')


# Even though Kolkata city has more restaurants but it has only one restaurant with 5 rating. Whereas Mumbai is second to Kolkata which has more restaurants and also provide more 5 rating restaurants as well. 

# # Restaurants with Highest Total_ratings

# In[75]:


df['Total_ratings'].max()


# In[76]:


high_total_ratings=df[['City','Restaurant','Total_ratings']][df.Total_ratings == df.Total_ratings.max()]
high_total_ratings.style.hide_index()


# All the highest total ratings restaurants belong to Hyderabad.

# # Average Delivery Time per City

# In[16]:


#Overall Average Delivery time
Avg_del_time = df['Delivery_time'].mean()
Avg_del_time = int(Avg_del_time)
Avg_del_time


# In[17]:


#Average Delivery time as per Cities
Del_time = df['Delivery_time'].groupby(df['City']).mean().sort_values()
round(Del_time,2)


# In[18]:


plt.figure(figsize=(10,6))
plt.plot(Del_time, color='orange')
plt.xlabel('City')
plt.ylabel('Delivery Time')
plt.title('Average Delivery time per city')


# Ahmedabad City offers less delivery time which is really good but it is sad that Ahmedabad City doesn't have a single high rating restaurant. 
# 
# Mumbai City is performing good in delivery service as well.

# # Restaurants with Price of more than Average Price

# In[78]:


avg_price_range = df['Price'].mean()
avg_price_range


# In[82]:


#Following are the restaurant offers food whose price is more than Average Price
high_avg_price_rest=df[['Restaurant','Price']][df.Price > df['Price'].mean()]
high_avg_price_rest.style.hide_index()


# In[83]:


#Total Restaurants having price more than average price
high_avg_price_rest.count()


# In[22]:


# Top 10 restaurants offering high price


# In[85]:


high_avg_price=df[['City','Restaurant','Food_type','Price','Avg_ratings']][df.Price > df['Price'].mean()]
high_avg_price = high_avg_price.sort_values(by = 'Price',ascending = False)
high_avg_price.head(10).style.hide_index()


# # Areas with more restaurants as per City

# In[86]:


area_count=df.groupby(['City', 'Area']).size()
area_count


# In[87]:


area_count =area_count.to_frame('type_count').reset_index()
area_count


# In[88]:


area_count_per_city = area_count.groupby('City').apply(lambda x: x.loc[x['type_count'].idxmax()])
area_count_per_city


# In[94]:


plt.figure(figsize=(10,6))
plt.scatter(area_count_per_city.Area,area_count_per_city.type_count , c = '#9A32CD')
plt.xlabel('Area')
plt.title('Areas with more restaurants', weight ='bold', size = 14)


# In[95]:


plt.figure(figsize=(10,6))
ax =sns.barplot(x = area_count_per_city.Area, y= area_count_per_city.type_count, hue = area_count_per_city.City)
ax.legend(bbox_to_anchor=(1, 1.02), loc='upper left')
plt.title('Areas with more restaurants as per City', weight ='bold', size = 14)


# In[ ]:




