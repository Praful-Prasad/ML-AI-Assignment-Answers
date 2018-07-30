# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 15:12:32 2018

@author: user
"""
        
import re
import collections
str=''
vowel=0
words=0
upper=0
lower=0
l=[]
n=1
print('Enter sentences : ')
while(str!='x'):
     str=input()
     if(str!='x'):
        l.append(str)
        n=n+1
     elif(str=='x' and n<=4):
        print('Enter atleast 4 sentences. ')
        str=''
print(" paragraph =")

for x in l:
    print(x)

print('-------')


l[int(len(l)/2)]='UST Global specializes in services'
print("Updated paragraph =")

for x in l:
    print(x)
for i in l:
    for x in i:
       
        if(x.isupper()):
            upper=upper+1
           
        elif(x.islower()):
            lower=lower+1
          
        elif(x in 'aeiouAEIOU'):
            vowel=vowel+1
list=collections.Counter(l)
for k,v in list.items():
    if(v>1):
        print('Repeaing word = ',k)
        
print("vowels = ",vowel)
print("upper = ",upper)
print("lower = ",lower)
p=[]

for i in range(len(l)):
    l[i]=re.sub('[^ a-zA-Z0-9.]', '', l[i])
print("\n\nAfter removing special characters paragraph =")

for x in l:
    print(x)

temp=l[0]
l[0]=l[len(l)-1]
l[len(l)-1]=temp
print("\n\nAfter swapping 1st AND last paragraph =")

for x in l:
    print(x)
    

