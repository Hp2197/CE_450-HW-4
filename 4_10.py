
# coding: utf-8

# In[1]:


def create_2d_arr(rows, columns):
    i=[]
    b=[]
    for column in range(0,columns):
        i.append('-')
    for row in range(0,rows):
        b.append(i)
    return b
    



print(create_2d_arr (3, 5))

