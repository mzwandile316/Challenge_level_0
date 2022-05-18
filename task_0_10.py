#!/usr/bin/env python
# coding: utf-8

# In[4]:


first_word = input("Enter the first word ")
second_word = input("Enter the second word ")

first_word = set(first_word)
second_word = set(second_word)

print(''.join(sorted(first_word.intersection(second_word))))


# In[ ]:




