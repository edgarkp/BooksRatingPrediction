#!/usr/bin/env python
# coding: utf-8

# In[1]:

def ratings_to_appreciation(ratings):
    if ratings < 3 :
        return 'poor rating'
    elif ratings < 4 :
        return 'good rating'
    else : 
        return 'high rating'
    
# In[2]:

# Create a function to get the year of the publication date\n",
def getyear(publication_date):
    return int(publication_date.rpartition('/')[2])

# In[ ]:

