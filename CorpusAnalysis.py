#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install indic-nlp-library


# In[1]:


INDIC_NLP_LIB_HOME=r"C:\Users\Nachiket\Documents\src\indic_nlp_library"

INDIC_NLP_RESOURCES=r"C:\Users\Nachiket\Documents\src\indic_nlp_resources"


# In[2]:


import re


# In[3]:


import sys
sys.path.append(r'{}'.format(INDIC_NLP_LIB_HOME))


# In[4]:


from indicnlp import common
common.set_resources_path(INDIC_NLP_RESOURCES)


# In[5]:


from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate


# In[7]:


f2=open(r"C:\Users\Nachiket\Downloads\corpus_final_2.txt","r+",encoding='UTF-8')


# In[8]:


text= f2.read()


# In[9]:


print(text)


# ### CORPUS CLEANING

# REMOVING NUMBERS FROM CORPUS

# In[10]:


text_no_num=re.sub(r'\d+','',text)


# In[11]:


print(text_no_num)


# REMOVING CAPITAL ENGLISH LETTERS FROM CORPUS:

# In[12]:


pattern="[A-Z]"
caps_gone__corp=re.sub(pattern,'',text_no_num)


# In[12]:


print(caps_gone__corp)


# REMOVING SMALL ENGLISH ALPHABETS FROM THE CORPUS:

# In[13]:


pattern2="[a-z]"
clean_corp=re.sub(pattern2,'',caps_gone__corp)


# In[14]:


print(clean_corp)


# REMOVING SPECIAL CHARACTERS FROM CORPUS:

# In[15]:


clean_corp2=re.sub(r"[.,:/()@< =_>-]",'',clean_corp)


# In[16]:


print(clean_corp2)


# ### CORPUS ANALYSIS

# NORMALIZATION:

# In[17]:


from indicnlp.normalize.indic_normalize import IndicNormalizerFactory
remove_nuktas=False
factory=IndicNormalizerFactory()
normalizer=factory.get_normalizer('sa',remove_nuktas=False)
print(normalizer.normalize(clean_corp2))


# TOKENIZATION:

# In[18]:


from indicnlp.tokenize import indic_tokenize  

indic_tokenize.trivial_tokenize(clean_corp2)


# SENTENCE CREATION:

# In[19]:


from indicnlp.tokenize import sentence_tokenize
sentences=sentence_tokenize.sentence_split(clean_corp2, lang='sa')

for t in sentences:
    print(t)


# TRANSLITERATION:

# In[22]:


from indicnlp.transliterate.unicode_transliterate import UnicodeIndicTransliterator

print(UnicodeIndicTransliterator.transliterate(clean_corp2,"sa","ta"))


# In[ ]:





# In[21]:


f2.close()

