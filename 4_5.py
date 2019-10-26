
# coding: utf-8

# In[1]:


def mrg(ls1, ls2):
    ls=ls1+ls2
    sorted=[]
    def srt(ls):
        x=min(ls)
        ls.remove(x)
        sorted.append(x) 
        if not ls:
            return sorted
          
        return srt(ls)
    return srt(ls)
print(mrg ([1, 3, 5], [2, 4, 6]))

