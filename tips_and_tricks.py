#!/usr/bin/env python
# coding: utf-8

# # 1. if and else in a line
# 

# In[7]:


condition = False
x  = 1 if condition else 0
x


# # 2. reading number or formating

# In[34]:


num = 10000000000
print(f'{num:,}')


# # 3.Enumerate 

# In[35]:


names =['ibm','simp','manipal','yoho']
for index,name in enumerate(names): 
    print(index,name)

# index is always first one in for loop


# # 4.zip

# In[36]:


names =['ibm','simp','manipal','yoho']
packs =['2','3.4','4.5','6.7']

for name,pack in zip(names,packs):
    print(name,'->',pack)

    
years =['2','3','1','1']
for value in zip(names,packs,years):
    print(value)


#  # unpacking

# In[33]:


a , b, *c = (1,2,3,4,5)
print(c)

a , b, *c,d = (1,2,3,4,5,7,8,9)
print(c,d)

a , b, *_,d = (1,2,3,4,5,7,8,9)
print(_)

# to avoid "too many values to unpack"


# # String reversal and string reading

# In[69]:



a ="TestforString"

print('reverse is',a[::-1]) 
print(a[0:4])
print(a[0:16:4])

#strat:end(excluded): skip in evry read


# # converting list to string

# In[76]:


a = ["tips", "For", "python"] 
print(''.join(a))


# In[83]:


def xswitch(x): 
	return xswitch._system_dict.get(x, None) 

xswitch._system_dict = {'files': 10, 'folders': 5, 'devices': 2}

print(xswitch('default'))
print(xswitch('devices'))


# # list tricks

# In[100]:


# adding two lists
years =['2014','2015','2016','2017']
new_years=['2018','2019']
years.extend(new_years)
print(years)


years =['2014','2015','2016','2017']
new_years=('2018','2019')
years.extend(new_years)
print(years)

years =['2014','2015','2016','2017']
years.extend(range(3))
print(years)

# new_years can be any enumerable

