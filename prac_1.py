# a = str() # string
# b = int() , float(), complex() # numeric
# c=  list(), tuple(), range() # seq. type (array)
# d = dict() # mapping # key value pairs
# e = bool,True,False #Boolean type
# f = bytes(), bytearray, memoryview() # Binary
# g = set(), frozenset() #

#######################################################################################################################
''' TYPE CASTING '''
# a = 100
# print(a)
# print(type(a))
# b = "Hello"
# a = str(a)
# print(a)
# print(type(a))
#
# a = list(a)
# print(a)
# print(type(a))
#
# a = tuple(a)
# print(a)
# print(type(a))
#
# a = list(a)
# print(a)
# print(type(a))
#
# a = str(a)
# print(a)
# print(type(a))
''' End '''

#######################################################################################################################
''' STRING USEFUL FUNCTIONS'''

var1 = 'Hi this is prac_1 Module '
# print(var1[5])                            # Index find
# print(var1[::-1])                           # Slicing
# print(var1.count('is'))                    # Count the related word
# print(var1.index('z'))                   # Find the index of given string (handle error for not found)
# print(var1.replace("is", "issss", 2))     # Replace string with the given string by given times
# print(var1.upper())                       # Convert string into Upper case
# print(var1.lower())                       # Convert string into Upper case
# print(var1.split("this"))                    # Split string into list based on the given text

'''concat two strings'''
var2 = 'Thanks for loading this module'
# print(var1 + var2)

''' string formatting '''
var3 = 'Hi {}, this is prac_1 Module '
name = 'Suraj'
# var4 = f'Hi {name}, this is prac_1 Module '
# print(var4)
# print(var3.format(name))

''' Use of if statement '''
# word = 'Shubham'
# if word in var1:
#     print("Yes '{}' word found !".format(word))
# else:
#     print("No '{}' word Not found !".format(word))

''' String looping '''
# loop_word = 'Hello World !'
# for i in loop_word:
#     print(i)

''' End '''
#####################################################################################################################

''' LIST USEFUL FUNCTIONS '''
list1 = [1,2,3,4,'a']
# print(list1[0])                                   # Index find
# print(list1[-2])                                  # Index find (Negative)
# print(list1[::-1])                                 # Index find (Negative)
''' add items to the list '''
# list1.append(5)                                   # add items to the end
# list1.insert(1,5)                                   # add items at the given index
# print(list1)

''' adding two lists '''
# list2 = [5,6,7,8,9]
# # print(list1+list2)
#
# list1.extend(list2)
# print(list1)

''' remove items from list two lists '''
# list1.remove(2)                           #remove by specifying the item
# list1.pop(0)                              #remove by index
# print(list1)
# list1.pop()
# print(list1)
##########################################27/01/2021###################################################################
'''List Comprehension'''

# src_list= [1,2,3,4,5,6,7,8,9,10]
#
# tgt_list=[]
# for i in src_list:
#     if i%2==0:
#         tgt_list.append(i)
# print(tgt_list)
#
# tgt_list=[i for i in src_list if i%2==0]                      # [expression for item in iterable if condition == True]
# print(tgt_list)

''' Sort Lists '''
# list3= ['b','c','a','d','z','w','x']
# print(list3)
# list3.sort(reverse=True)
# print(list3)

''' Copy Lists'''

list4 = [1,2,3,4]
# list5 = list4
# list4.append(5)
# print(id(list4))
# print(id(list5))
# print(list4)
# print(list5)

# list5 = list4[:]
# list4.append(5)
# print(id(list4))
# print(id(list5))
# print(list4)
# print(list5)

''' End '''
''' TUPLE USEFUL FUNCTIONS '''

# t1 = (1,1,2)                                              # # ordered, Unchangeable, Duplicates Allowed
# print(type(t1))


''' Update Tuple'''
# x = ("a", "b", "c")
# print(x)
# y = list(x)
# y[1] = "z"
# x = tuple(y)
# print(x)

''' Add items to tuple'''

# tup1 = ("a", "b", "c")
# print(tup1)
# y = list(tup1)
# y.append("d")
# tup1 = tuple(y)
# print(tup1)

''' Looping in tuple'''

# tup2 = (1,2,3,4)
# for i in tup2:
#     print(i)


''' END'''

''' Useful modules '''

''' SET USEFUL FUNCTIONS '''

# set1 = {1,1,2,3,4,3,1,2,3,1,2,3,1,2,3,4,2,1,2,3,2,3,5,6,1,2,3,4,5,67,5,4,3,2,3,3,2,3,4,5,6,8}              # Unordered, Duplicates Not Allowed
# # print(type(set1))
# print(set1)
# ''' Type casting into list/tuple'''
# print(list(set1))
# print(tuple(set1))

''' Looping '''
# s1 = {1,2,3,4}
# for x in s1:
#   print(x)

''' Add items '''
# s2 = {1,2,3,4}
# print(s2)
# s2.add(5)
# print(s2)

''' Remove  items '''
# s3 = {1,2,3,4,5}
# print(s3)
# x = s3.pop()
# print(f"Removed Item was : {x}")
# print(s3)

# s3 = {1,2,3,4,5}
# print(s3)
# x = s3.remove(4)
# print(f"Removed Item was : {x}")
# print(s3)

''' End '''

''' Dictionaries USEFUL FUNCTIONS'''

d1 = {                                                              # Unordered,Changeable, Duplicates Not Allowed
  "FirstName" : "Rohit",
  "LastName" : "Tiwari",
  "DOB" : 1995
}

# print(type(d1))

''' access by Key '''
# if 'FirstNames' in d1 :
#   print("Found {FirstNames}")
# if 'FirstName' in d1 :
#   print("Found {FirstName}")
# # print(d1["FirstNames"])
# x = d1.get("FirstName")
# print(x)

''' dups '''
# print(d1)
# d1["FirstName"] = "Abhinandan"
# print(d1)
# #
# d1["City"] = "Mysore"
# print(d1)

''' Get all the keys/values/items'''

# k = d1.keys()
# print(k)
# v = d1.values()
# print(v)

# i = d1.items()
# print(i)

''' Looping '''

# for k,v in d1.items():
#     print(str(k) + " : " + str(v))

''' End '''


# ''' Datetime'''
# import datetime
# print(datetime.datetime.now())
# print(type(datetime.datetime.now()))
# print(datetime.datetime.utcnow())
#
# ''' Time'''
# import time
# print(time.localtime())
# print(type(time.localtime()))
# print(time.asctime())
# print(type(time.asctime()))
#
# for i in range(4):
#     print(i)
#     time.sleep(60)
#
# ''' OS '''
# import os
# print(os.path.exists(r'D:\\Python_Project\Infy_Training'))

''' Random'''
import random
# print(random.randint(1,100000))
# r1= ["a",1,"b","c",2,4,6,7]
# print(random.choice(r1))

''' UUID'''                     #Universally Unique IDentifier
import uuid
# print(uuid.uuid1())
# print(uuid.uuid1())

# print(uuid.uuid4())
# print(uuid.uuid4())
# print(uuid.uuid4().bytes)

''' JSON'''

import json

json1 =  '{ "Name":"Rahul", "age":30, "city":"New York"}'
print(type(json1))
parsed_dict = json.loads(json1)
print(type(parsed_dict))
#
parsed_jon = json.dumps(parsed_dict)
print(type(parsed_jon))



