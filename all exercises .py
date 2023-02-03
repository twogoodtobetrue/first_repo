#1
i = 1 
while i <4 :
    x = '*'
    y = i * x
    i = i + 1
print(y)
   
    
    
    
#2    
    
x = '*'
for i in range(1,6):
    if i % 2 == 0 :
        pass 
    else :
        print(i * x)

        
        
        
 ##3      
        
        
todo = ["exercise1", "exercise2", "exercise3","coffee break" ,"exercise4","exercise5","exercise6"]
for x in todo:
    if x.upper() == "COFFEE BREAK":
        print(x)
        break


#4
list1 = ["lion", "monkey", "dog","fish"]
tuple1 = ("lion", "monkey", "dog","fish")
set1 = {"lion", "monkey", "dog","fish"}
dict1 = {"lion":"land", "monkey":"land", "dog":"land","fish":"water"}
for i in list1 :
    print(i)
for i in tuple1 :
    print(i)
for i in set1 :
    print(i)

#5
list1 = ["lion", "monkey", "dog","fish"]
tuple1 = ("lion", "monkey", "dog","fish")
set1 = {"lion", "monkey", "dog","fish"}
dict1 = {"lion":4, "monkey":2, "dog":4,"fish":2}
print(len(list1))
print(len(tuple1))
print(len(set1))
print(len(dict1))
print(list1[0])
print(tuple1[0])
print(dict1['lion'])
list1[1]= 'rabbit'
#tuple1[1] = 'rabbit' 'tuple' object does not support item assignment
list1.append('monkey')
list1.remove('rabbit')
dict1['fish'] =1



#6
def goodbye():
    print('goodbye')
    
    
#7
def goodbye(name):
    print(f'goodbye {name}')
name = 'adam'
print(goodbye(name))

#8

import os

user = os.getlogin()
print(user)


#5 function 

import random
random_list_summer = []
for i in range(15) :
    random_list_summer.append(random.randint(-100,100))
print(random_list_summer)
print('the sum is ' ,sum(random_list_summer))
    

#6 function 

def fibonacci_of(n):
    if n in {0, 1}:  
        return n
    else :
        return fibonacci_of(n - 1) + fibonacci_of(n - 2)  
for i in range(5) :
    print(fibonacci_of(i))

#7

x = int(input('please insert the number :'))
F = lambda x : x**2
print(F(x))





    
    
   