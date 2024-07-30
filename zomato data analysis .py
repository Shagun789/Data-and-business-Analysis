#!/usr/bin/env python
# coding: utf-8

# ![Screenshot%202024-07-23%20142526.png](attachment:Screenshot%202024-07-23%20142526.png)

# ![Screenshot%202024-07-23%20142727.png](attachment:Screenshot%202024-07-23%20142727.png)

# ## Importing libraries

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ## create the dataframe

# In[2]:


df = pd.read_csv("Zomato")


# ## calling the dataset

# In[3]:


df.head(5)


# ### convert the data types  of column-rate

# In[4]:


def handlerate(value):
    value = str(value).split("/")
    value = value[0];
    return float(value)
df["rate"] = df["rate"].apply(handlerate)
print(df.head())


# In[5]:


df.info()


# ## Type of restraunt

# In[6]:


df.head()


# In[7]:


plt.figure(figsize=(12, 6)) 

sns.countplot(x=df["listed_in(type)"], palette="viridis")

plt.title("Distribution of Restaurant Types", fontsize=20, fontweight='bold', color='navy')
plt.xlabel("Type of Restaurant", fontsize=15, fontweight='bold', color='darkred')
plt.ylabel("Count", fontsize=15, fontweight='bold', color='darkred')

plt.xticks(rotation=45, fontsize=12, color='darkgreen')
plt.yticks(fontsize=12, color='darkgreen')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

plt.show()


# # Majourity of restraunt falls under dining category

# In[8]:


df.head()


# In[9]:


grouped_data = df.groupby("listed_in(type)")["votes"].sum()
result = pd.DataFrame({"votes": grouped_data})

plt.plot(result.index, result["votes"], c="pink", marker="o")
plt.xlabel("Type of restaurant", color="red", fontsize=20)
plt.ylabel("Votes", color="red", fontsize=20)
plt.title("Votes by Type of Restaurant", fontsize=24)
plt.xticks(rotation=45) 
plt.grid(True)  
plt.tight_layout()  
plt.show()


# ## dining restraunt has recieved the highest votes

# In[19]:


plt.figure(figsize=(10, 6)) 

plt.hist(df["rate"], bins=5, color='skyblue', edgecolor='black', alpha=0.7)
plt.title("Ratings Distribution", fontsize=20, fontweight='bold', color='navy')
plt.xlabel("Ratings", fontsize=15, fontweight='bold', color='darkred')
plt.ylabel("Frequency", fontsize=15, fontweight='bold', color='darkred')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(fontsize=12, color='darkgreen')
plt.yticks(fontsize=12, color='darkgreen')

plt.tight_layout()

plt.show()


# # Average order spending by couples

# In[12]:


plt.figure(figsize=(14, 7))
couple_data = df["approx_cost(for two people)"].astype(str)  # Convert to string for better plotting
sns.countplot(x=couple_data, palette="coolwarm", order=couple_data.value_counts().index)
plt.title("Approximate Cost Distribution for Two People", fontsize=20, fontweight='bold', color='navy')
plt.xlabel("Approximate Cost (for two people)", fontsize=15, fontweight='bold', color='darkred')
plt.ylabel("Count", fontsize=15, fontweight='bold', color='darkred')
plt.xticks(rotation=45, fontsize=12, color='darkgreen')
plt.yticks(fontsize=12, color='darkgreen')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

plt.show()


# ## Maximum couples spend 300 rupees for each order

# In[13]:


# which mode recieves maximum rating online or offline?


# In[14]:


df.head(2)


# In[19]:


plt.figure(figsize=(10, 6))  
sns.boxplot(x="online_order", y="rate", data=df, palette="Pastel1")

plt.title("Ratings Distribution by Online Order Availability", fontsize=20, fontweight='bold', color='navy')
plt.xlabel("Online Order Available", fontsize=15, fontweight='bold', color='darkred')
plt.ylabel("Rating", fontsize=15, fontweight='bold', color='darkred')
plt.xticks(fontsize=12, color='darkgreen')
plt.yticks(fontsize=12, color='darkgreen')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


# In[20]:


# conclusion - offline order lower ratings in comparison to online order


# In[21]:


df.head()


# In[24]:


pivot_table = df.pivot_table(index="listed_in(type)", columns="online_order", aggfunc="size", fill_value=0)

plt.figure(figsize=(12, 8))  
sns.heatmap(pivot_table, annot=True, cmap="YlGnBu", fmt="d", linewidths=.5, linecolor='black', cbar_kws={'label': 'Count'})
plt.title("Heatmap of Online Order Availability by Restaurant Type", fontsize=20, fontweight='bold', color='navy')
plt.xlabel("Online Order", fontsize=15, fontweight='bold', color='darkred')
plt.ylabel("Listed In (Type)", fontsize=15, fontweight='bold', color='darkred')
plt.xticks(fontsize=12, color='darkgreen')
plt.yticks(fontsize=12, color='darkgreen')
plt.tight_layout()

plt.show()


# ## Business insights from the Data analysis

# ### Dining Preference: The data shows that the majority of restaurants fall under the "Dining" category, indicating that customers prefer sit-down meals over other types of dining options. This suggests an opportunity to focus on enhancing the dining experience by improving ambiance, service quality, and menu variety to attract more customers.
# 
# ### High Votes for Dining Restaurants: The data reveals that dining restaurants have received the highest number of votes, indicating a strong customer preference and satisfaction with sit-down meal experiences. This suggests a focus on further enhancing the dining environment, service quality, and menu offerings to capitalize on this preference and maintain high customer engagement.
# 
# ### Rating Range: Most restaurant ratings fall between 3.75 and 4.25. This indicates a general satisfaction among customers, with room for improvement to achieve higher ratings. Focusing on customer feedback and enhancing service quality could help in moving more ratings towards the higher end of the scale.
# 
# 
# ### Spending Behavior: The data indicates that most couples spend around 300 rupees on their orders. This suggests that mid-range pricing is popular among customers, and maintaining or offering more options within this price range could attract more business.
# 
# 
# ### Order Type and Ratings: Restaurants offering offline orders tend to receive lower ratings compared to those with online ordering options. This highlights the importance of a seamless online ordering experience and suggests that improving offline service could boost overall customer satisfaction and ratings.
# 
# 
# ### Order Preferences: Dining restaurants primarily accept offline orders, while cafes mainly receive online orders. This suggests that customers prefer to order in person at dining establishments but choose online ordering for cafes. Tailoring order options to match these preferences could enhance customer satisfaction and streamline service.
# 
# 
# 
# 
# 
# 

# In[ ]:




