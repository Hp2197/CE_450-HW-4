
# coding: utf-8

# In[1]:


def sym(l):
    if(len(l)==0 or len(l)==1):
        return True
    if(l[0]==l[-1]):
        l.remove(l[0])
        l.remove(l[-1])
    if(len(l)==2 and l[0]!=l[1]):
        return False
   
    return sym(l)

print(sym ([1]))
print(sym ([1, 4, 5, 1]))
print(sym ([1, 4, 4, 1]))
print(sym (['l', 'o', 'l']))

