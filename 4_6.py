
# coding: utf-8

# In[1]:


def fltn(lst):
    
    if type(lst) != list:
        
        return [lst]
    else:
        
        
        return sum([fltn(elem) for elem in lst],[])



x =  [[1, [2, 3]], 4, [5, 6]] 
print(fltn (x))

