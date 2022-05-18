#!/usr/bin/env python
# coding: utf-8

# In[3]:


word = input("Enter word ")
blank_word = ""
vowels = ["a", "e", "i", "o", "u"]

for letter in word:
    if letter in vowels:
        blank_word += letter
print(blank_word)


# In[ ]:




