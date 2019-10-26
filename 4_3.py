
# coding: utf-8

# In[1]:


def add_many(x, elem, lst): 
    for x in range(0,x):
        lst.append(elem)
    return lst


lst = [1, 2, 4, 2, 1]
print(add_many (2, 5, lst) )

