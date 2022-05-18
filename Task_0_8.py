#!/usr/bin/env python
# coding: utf-8

# In[1]:


def convert_number(minutes):
    minutes = minutes % (24 * 60)
    hour = minutes // 60
    minutes %= 60
    return "%d Hour:%02d minutes" % (hour, minutes)

number = int(input("Enter number "))
print(convert_number(number))


# In[ ]:




