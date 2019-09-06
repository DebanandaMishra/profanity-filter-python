#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install profanityfilter


# In[3]:


from profanityfilter import ProfanityFilter


# In[4]:


pf = ProfanityFilter()


# In[5]:


pf.censor("That's bullshit!")


# In[6]:


pf.set_censor("@")


# In[7]:


pf.censor("That's bullshit!")


# In[8]:


pf.define_words(["icecream", "choco"])


# In[9]:


pf.censor("I love icecream and choco!")


# In[10]:


pf.is_clean("That's awesome!")


# In[11]:


pf.is_clean("That's bullshit!")


# In[12]:


pf_custom = ProfanityFilter(custom_censor_list=["chocolate", "orange"])
pf_custom.censor("Fuck orange chocolates")


# In[13]:


pf_extended = ProfanityFilter(extra_censor_list=["chocolate", "orange"])
pf_extended.censor("Fuck orange chocolates")

