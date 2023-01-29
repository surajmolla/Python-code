#!/usr/bin/env python
# coding: utf-8

# In[1]:


hieght = float(input("enter your hieght"))
base = float(input("enter your base:"))
area = hieght*base*0.5
print("the area of triangle is :",area)


# In[2]:


radius = float(input("enetr your radius:"))
area = 3.14*radius*radius
print("the radius of circul is :",area)


# In[17]:


arithmetic = input("enetr your symbol to calculate your values:")
a = int(input("enetr your number:"))
b = int(input("enter your second number"))
if arithmetic =="+":
    sum = a+b
    print(f"the sum of {a} + {b} =",sum)
elif arithmetic == "-":
    substract = a-b
    print(f"the substract of {a} -{b} = ",substract)
elif arithmetic == "*":
    multiply = a*b
    print(f"the multiply of {a} * {b} = ",multiply)
elif arithmetic == "/":    
    divide = a/b
    print(f"the divide of {a} /{b} = ",divide)
else :
    print("cannot calculate your number ,enter valid arithmetics operator")


# In[21]:


from math import *
user_num1 = int(input("enter numhber to find maximum values:"))
user_num2 = int(input("enter second number :"))

print("maximum number is ",max(user_num1,user_num2))


# In[25]:


print(type(100))
print(type("false"))
print(type(15.6))


# In[28]:


user = int(input("enetr your number to find it is odd or even!"))
if user % 2 == 0:
    print("it is a even number")
else:
    print("it is a odd number")


# In[34]:


user_score = int(input("enter your score to know the grade:"))

if user_score >=80:
    print("AA")
elif user_score >=70:
    print("A+")
elif user_score >=50:
    print("B+")
elif user_score >=33:
    print("pass")
else:
    print("you are fail")


# In[39]:


num1 = int(input("enter your first number:"))
num2 = int(input("enter your decond number"))
num3 = int(input("enetr your third number:"))
if num1>num2 and num1>num3:
    print(num1 ,"is big")
elif num2>num1 and num2>num3:
    print(num2 ,"is big")
else:
    print(num3,"is big")


# In[43]:


sub = ["sharukh","suraj","kutub","mehebub","sakib"]
print(sub)


# In[52]:


print(sub[1])
print(sub[:1])
print(sub[1:])
print("suraj" in sub)
print("suraj" not in sub)
print(len(sub))
sub.append("rehan")
print(sub)


# In[53]:


sub.pop()


# In[54]:


print(sub)


# In[55]:


sub.insert(2,"salam")
sub


# In[56]:


sub.append("reahn")
sub


# In[57]:


sub.insert(2,"misty")
sub


# In[62]:


sub.sort()
print(sub)


# In[63]:


print(sub)


# In[64]:


subject2 = sub.copy()
print(subject2)


# In[65]:


print(subject2)


# In[66]:


print(subject2.index("kutub"))


# In[68]:


print(subject2[0])


# In[36]:


num = [1,1,5,4,55,4,6,4,67,8,855,4,5]
sum = 0
for x in num :
    sum = sum+x
print("the sum of all number is",sum)
    


# In[94]:


for x in range(100,10,-10):
    print(x)


# In[95]:


sum = 0
for x in range(10,1000,2):
    sum = sum +x
print(sum)


# # Factorial With Range Function With For Loop

# In[98]:


n = int(input("enetr your number to find factorial"))
fact = 1
for x in range(n,0,-1):
    fact = fact*x
print(fact)


# In[2]:


num = input('Enter the number: ')
reverse = ''
for i in range(len(num), 0, -1):
   reverse = reverse + num[i-1]
print('The reverse number is =', reverse)


# In[1]:


n=int(input("Enter the integer numbers is:"))
rev=0
while(n>0):
    digit=n%10
    rev=rev*10+digit
    n=n//10
print("The reverse number is:",rev)


# In[34]:


row = 5
for x in range(1,row+1):
    print("")
    for y in range(1,x+1):
        print("*",end = "")


# In[45]:



n1 = int(input().strip())
n2 = int(input().strip())
for x in range(n1,n2+1):
    for y in range(1,11):
        print(x,"x",y,"=",x*y)


# In[13]:


num = input("Enter a number: ")
 
sum = 0
for n in num:
  sum = sum+ int(n)
print(sum)


# In[22]:


number = int(input("Enter the integer number: "))  
revs_number = 0   
while (number > 0):    
    remainder = number % 10  
    revs_number = (revs_number * 10) + remainder  
    number = number // 10  
print("The reverse number is : {}".format(revs_number))  


# In[30]:


num = int(input("enetr your digit"))
reverse = int(str(num)[::-1])
print(reverse)
if num == reverse:
  print('Palindrome')
else:
  print("Not Palindrome")


# # number and digit and word count

# In[37]:



number_of_word = 0
number_digit  = 0
number_of_letter = 0
string = input("enter your string")
for x in string:
    if x >= "a" and x<= "z":
        number_of_letter = number_of_letter +1
    elif x>="1" and x<="9":
        number_digit = number_digit+1
    elif x == " ":
        number_of_word = number_of_word+1
print(number_of_word+1)
print(number_digit)
print(number_of_letter)


# # Matrix 

# In[39]:


matrix = [
    [1,4,5],
    [6,5,4]
]
for row in matrix:
    for col in row:
        print(col)


# # Dictonary

# In[49]:


user = input("enter your key to find value:")
find = dict.get(user,"not valid key")
dict = {
    "101":"suraj",
    "102":"misty",
    "103":"kutub",
    "104":"rehan",
    "105":"mehebub"
}
print(find)


# # Function

# In[3]:


def add(x,y):
    sum = x+y
    print(sum)
num1 = int(input("enetr first number:") )
num2 = int(input("enter second number:"))
add(num1,num2)


# # Xarg

# In[6]:


def addition(*number):
    sum = 0
    for x in number:
        sum = sum+x
    print(sum)
addition(10,20,30)
addition(10,20,30,40)


# # XXArg

# In[9]:


def student(**details):
    print(details)
student(id= 101,name = "suraj-molla",perofession = "data scientist")


# # Lamda Function 

# ##### lamda argument :exprssion

# In[11]:


a = (lambda x : x*x*x)(2)
print(a)


# In[12]:


result = lambda x,y : x*x + 2*x*y + y*y 
print(result(2,3))


# In[13]:


def arg1(x):
    return lambda y : x*y
mydoubler = arg1(2)
print(mydoubler(3))


# In[14]:


def arg1(x):
    return lambda y :x*y
doubler = arg1(2)
tripler = arg1(3)

print(doubler(11))
print(tripler(5))


# # Map And Filtter Function 

# ### With Name Function

# In[15]:


def squre(x):
    return x*x
List = [2,3,4,5,6,7,8,9]
result = list(map(squre,List))
print(result)


# ### With Lambda Function

# In[23]:


function = lambda x : x*x
List = [2,3,4,5,6,7,8,9]
result = (map(function,List))
print(list(result))


# ## Filter Function

# ### Using NameFunction

# In[ ]:


List = [4,5,6,7,8,9,10]
def even(x):
        return x % 2 == 0 
result = filter(even,List)
print(list(result))


# ### Using Lambda Function

# In[30]:


List = [4,5,6,7,8,9,10]
function = lambda x : x % 2 ==0
result = filter(function,List)
print(list(result))


# ### Name Function With Control Statement

# In[31]:


List = [4,5,6,7,8,9,10]
def even(x):
        if x % 2 == 0 :
            return x
result = filter(even,List)
print(list(result))


# # List Comprehension

# #### [expression for item in iterable if condition == True]

# In[32]:


List = [4,5,6,7,8,9,10] 
result = [x for x in List if x % 2 == 0]
print(list(result))


# In[33]:


List = [4,5,6,7,8,9,10]
result = [x*x for x in List]
print(list(result))


# In[37]:


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
result = [x.upper() for x in fruits]
print(list(result))


# In[38]:


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1+list2
print(list(list3))


# # Zip Function 

# In[41]:


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = zip(list1,list2)
print(list(list3))


# # Recurssion

# ##### Python also accepts function recursion, which means a defined function can call itself.
# 
# Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result

# In[42]:


def my_func(n):
    if n ==1:
        return 1
    else :
        return n*(n-1)
print(my_func(3))


# In[10]:


def nothing():
    print("hello")
    nothing()


# # hackerank soltuion day 5 - 30 day lets review

# In[9]:


n = int(input())
for x in range(n):
    strlst = input()
    for i in range(len(strlst)):
        if i % 2 ==0:
            print(strlst[i],end  = " ")
    print(" " , end = "")
    for j in range(len(strlst)):
        if j % 2 != 0:
            print(strlst[j], end = " ")
    print()


# # Pattern Printing

# In[14]:


n = int(input("enter yor range:"))
for x in range(n):
    for y in range(x):
        print("# ", end= "")
    print()


# In[18]:


n = int(input("enter yor range:"))
for x in range(n):
    for y in range(n-x):
        print("# ", end= "")
    print()


# In[19]:


n = int(input("enter yor range:"))
for x in range(n):
    for y in range(x):
        print("# ", end= "")
    print()
for x in range(n):
    for y in range(n-x):
        print("# ", end= "")
    print()


# In[ ]:




