
# coding: utf-8

# In[2]:


def add(i,lst):
    return i+lst
def sub(i,lst):
    return i-lst
def mul(i,lst):
    return i*lst
def fld (lst, g, i):
    i=g(i,lst[0])
    lst.remove(lst[0])
    if len(lst)==1:
        return g(i,lst[0])
    
    return fld(lst,g,i)


s=[3,2,1]
print(fld (s, mul, 1))

