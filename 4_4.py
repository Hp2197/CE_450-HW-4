
# coding: utf-8

# In[1]:


def f (suits, numbers):
    
    z=[[] for i in range(len(suits)*len(numbers))]
    count=0
    for y in range(0,len(suits)):     
        for t in range(0,len(numbers)):
            
            z[count]=suits[y],numbers[t]
            count+=1  
          
        
    return z


print(f(['S', 'C'], [1, 2, 3]))
print(f(['S', 'C'], [3, 2, 1]))

