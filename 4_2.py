
# coding: utf-8

# In[1]:


def rm_all(elem, lst):
    x=[]
    for a in lst:
        if(elem!=a):
            x.append(a)
    return x
    

x = [3, 1, 2, 1, 5, 1, 1, 7]
print(rm_all (1, x))

