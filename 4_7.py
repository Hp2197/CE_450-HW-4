
# coding: utf-8

# In[1]:


def tem(lst):
    if type(lst) != list:
            
        return [lst]
    else:
        return sum([tem(elem) for elem in lst],[])
def chk_elm(lst,n):
    lst=tem(lst)
    for i in lst:
        if(i==n):
            return True
    return False    



x =  [[1, [2, 3]], 4, [5, 6]] 
print(chk_elm (x,4))

