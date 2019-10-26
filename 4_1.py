
# coding: utf-8

# In[1]:


def mk_wd(balance):
    
    
    
    def withdraw(M):
        nonlocal balance    
        balance-=M
        if(balance<0):
            return "insufficient funds" 
        return  balance
    return withdraw
rem=mk_wd(100)
print(rem(10))
print(rem(20))
print(rem(30))
print(rem(100))

