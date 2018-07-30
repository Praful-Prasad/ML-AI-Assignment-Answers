# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 15:36:44 2018

@author: user
"""

import statistics
 
dict1={}
dict2={}
dict3={}
dict4={}
dict5={}
for i in range(5):
    str1=input('Enter name :')
    str2=int(input('Enter marks in subject 1 :'))
    
    str3=int(input('Enter marks in subject 2 :'))
    
    str4=int(input('Enter marks in subject 3 :'))
    dict1.update({str1:str2})
    dict2.update({str1:str3})
    dict3.update({str1:str4})

for k,v in dict1.items():
    print(k,end="    ")
    print(dict1[k],end="    ")
    print(dict2[k],end="    ")
    print(dict3[k],end="    ")
    print('\n')
    
sum=0
l1=[]
l2=[]
l3=[]
for k,v in dict1.items():
    l1.append(v)
    
for k,v in dict2.items():
    l2.append(v)
for k,v in dict3.items():
    l3.append(v)
    

data1 = l1
 
x = statistics.mean(data1)
 
print("Mean for subject 1 :", x)
data1 = l2
 
x = statistics.mean(data1)
 
print("Mean for subject 2 :", x)

data1 = l3
 
x = statistics.mean(data1)
 
print("Mean for subject 3 :", x)
print('Median for subject 1 = ',l1[int(len(l1)/2)])

print('Median for subject 1 = ',l2[int(len(l1)/2)])
print('Median for subject 1= ',l3[int(len(l1)/2)])

sum=[]
for i in range(5):
    sum.append(int(l1[i]+l2[i]+l3[i]))
n=0
for k,v in dict1.items():
    dict4.update({k:sum[n]})
    n=n+1
n=0
for k,v in dict1.items():
    if(sum[n]>270):
        print(k, ' A+')
    elif(sum[n]>240):
        print(k, ' A')
    elif(sum[n]>210):
        print(k, ' B+')
    elif(sum[n]>180):
        print(k, ' B')
    elif(sum[n]>150):
        print(k, ' C+')
    elif(sum[n]<=150):
        print(k, ' C')
    n=n+1
    

