QUS:-3 Write a program to create "BCA.txt" file which contain information about BCA course. 
    count and print the total number of lines starting with ‘A’, ‘B’, and ‘C’ in "intro.txt" file.

#!/usr/bin/env python
# coding: utf-8

# In[11]:


i=['BCA course','Bachelor of computer Application','is an undergraduate degree program that focuses on technology and computer applications','Spanning three years, this course equips students with the knowledge and skills required to excel in the field of computer science','I also chooes BCA course becuses they are so high course on this time.']


# In[12]:
# WRITER

with open('E:\\22bca02\\python\\BCA.txt','w') as f:
    for line in i:
        f.write(line)
        f.write('\n')


# In[13]:
#READER

with open('E:\\22bca02\\python\\BCA.txt','r') as f:
    c=f.read()
    print(c)


# In[ ]:
 #OUTPUT

BCA course
Bachelor of computer Application
is an undergraduate degree program that focuses on technology and computer applications
Spanning three years, this course equips students with the knowledge and skills required to excel in the field of computer science
I also chooes BCA course becuses they are so high course on this time.




