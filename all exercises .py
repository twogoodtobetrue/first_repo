#!/usr/bin/env python
# coding: utf-8

# #variables

# #1
# 

# In[1]:


firstName = 'Mario'


# #2

# In[2]:


age = 25


# #3

# In[12]:


sentence = '''hello , I'm mario!'''


# #4

# In[6]:


amount = 4.3


# #5

# In[8]:


a = [True , True , True]
bool(a)


# #6

# In[13]:


my_first2_Name : 'Mario'


# #7

# In[ ]:





# #8

# In[14]:


a = 1
b = 2 
c = 3
print(a,b,c)


# #9

# In[15]:


a = 4
b = 6


# In[16]:


c = 4
a = b
b = c
print(a , b)


# #10

# In[17]:


hello = 'Hello!'
name = 'Jhon Doe'
age = '40'


# In[23]:


len(hello)


# In[21]:


len(name)


# In[22]:


len(age)


# #11

# a = 'hello' #capitalize
# b = 'tom' #uppercase
# c = 'LAURA' #lowercase
# question = 'How are you' #change o in e
# age_question = 'How old are you?' #use the correct method to create a string for each word
# print(a, b, c, question, age_question

# In[35]:


a = 'hello' 
a.capitalize()


# In[36]:


b = 'tom'
b.upper()


# In[37]:


c = 'LAURA'
c.lower()


# In[39]:


question = 'How are you'
question.replace('o' , 'e')


# In[45]:


age_question = 'How old are you?'
age_question.split( )


# #12

# In[46]:



age = 30
name = 'Mike'
print(f'Hello, {name}. You are {age}')


# #Operators

# #1

# In[49]:


bool(True*False)


# #2

# In[50]:


bool(True+False)


# #3

# In[51]:


5%2


# #4

# In[53]:


bool(True + False)


# #5

# In[55]:


firstName = "Mario"
lastName = "Rossi"

sentence = firstName + ' ' + lastName
print(sentence) # Should print "Mario Rossi"


# #6

# In[60]:


brands = ["Adidas", "Nike"]
if "Nike" in brands :
    print(True)
else :
    print(False)


# #7

# In[61]:


brands = ["Adidas", "Nike"]
if "Reebok" in brands :
    print(True)
else :
    print(False)


# #Methods

# #1

# In[68]:


print(type("Hello World"))
print(type(True))
print(type(False))
print(type(33))
print(type(24.5))
print(type(4+1j))
print(type(4j))
print(type(["lion", "monkey", "dog","fish"]))
print(type(("lion", "monkey", "dog","fish")))
print(type({"name" : "John", "surname" : "Doe", "age":22}))
print(type({"lion", "monkey", "dog","fish"}))


# #2
# num1 = 1.3
# num2 = 2.3
# num3 = 1j 
# num4 = 1.4 
# num5 = 1.5

# In[81]:


num1 = float(num1)
num2 = int(num2)
num3 = complex(num3)
num4 = round(num4)
num5 = round(num5)
print(num1 , num2 , num3 , num4 , num5)
type(num1)
#....


# #3

# In[90]:


num1 = 1122334455666
num1_str = str(num1)
print(num1_str)
len(num1_str)
print(num1_str[3])
print(num1_str[3:5])
##no more data was on dowloanded file !


# #Conditions

# #1

# In[91]:


num1 = 335 
num2 = 66
if num1 > num2 :
    print ('num1 is greater')
else :
    print('num2 is greater')


# #2

# In[94]:


num1 = 335 
num2 = 66
if num1 > num2 :
    print ('num1 is greater')
elif num2 > num1 :
    print('num2 is greater')
else :
    print('number2 equals to number1')


# #3

# In[8]:


import random
number1 = random.randint(1,100)
number2 = random.randint(1,100)
if number1 > number2 :
    print ('number1 is greater')
    print(f'number1 is {number1}')
    print(f'number1 is{number2}')
elif number2 > number1 :
    print('number2 is greater')
    print(number1)
    print(number2)
else :
    print('number2 equals to number1')
    print(number1)
    print(number2)


# #4

# In[9]:


import random

number1 = random.randint(-100,100)
number2 = random.randint(-100,100)

if abs(number1) > abs(number2):
    print('number1 absolute value greater than number2 absolute value')
elif abs(number1) < abs(number2):
    print('number2 absolute value greater than number1 absolute value')


# In[ ]:




