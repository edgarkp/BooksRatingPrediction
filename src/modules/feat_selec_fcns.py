#!/usr/bin/env python
# coding: utf-8

# In[3]:

def make_mi_scores(X, y):
    from sklearn.feature_selection import mutual_info_regression
    import pandas as pd

#     Mutual information (MI) between two random variables is a non-negative value
#     which measures the dependency between the variables. 
#     It is equal to zero if and only if two random variables are independent, and higher values mean higher dependency
    mi_scores = mutual_info_regression(X=X, y=y)
    mi_scores = pd.Series(mi_scores, name="MI Scores", index=X.columns)
    mi_scores = mi_scores.sort_values(ascending=False)
    return mi_scores


# In[ ]:




