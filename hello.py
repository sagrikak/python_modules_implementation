#! python3
'''
multiple 
line 
comment
'''

import sys
import time
import random
import urllib.request
import module#importing module 

print(18/4)#prints4.5
print(18//4)#drops the decimal value

var2=88#not a global variable
var3=68#not a global variable

def func(x):#creating a function#don't use function name similar to basic functions
	print('I am a function')
	print("still a function")
	print(x)
	print("var2="+str(var2))#can access variable but cannot modify it because var2 is not global
	global var3#converting local variable to global#use of global variables is not appreciated 
	var3+=2#can be modified because it's global
	return var3#returning value

def func2(x="Default function parameter"):#setting default function parameter
	print(x)

print(5.0/2)
print(r'\n\n\n')#adding r prints the string as it is
print(4**4)#pow(4,4)
print('Hello '+'World!')#print is in-built function #no import needed
print('Hello','World!')#prints Hello World! with space in between
print('Hi '+str(5))
print(int('1')+1)
print(sys.version)#printf version of python being used
time.sleep(1)#pauses for 1 sec
print("We're going")#using ' between " works
print('He said,"Hi"')#using " between ' works
print('We\'re going')#using escape character \ to print ' between '

var=32+44
print(var)
x, *y, z=[3, 5, 9, 8, 7]#x is assigned to first element #z is assigned to last and y is assigned to rest
print(x)
print(y)
print(z)

condition=1
while condition<5:
	print(condition)#only the indented part will belong to the loop
	condition+=1#use ctrl+[ to shift text to left 

list=[5,25,12,33,44]

list.append(25)#adds 25 at the end of list
list.insert(2, 999) #inserts 999 at index 2
list.remove(25)#removes the first occurence of 25
print("33 is at", list.index(33))
print("33 comes", list.count(33), "times")

print('List:')
for x in list:
	print(x)

list.sort()

print('List:')
for x in list:
	print(x)

for x in range(1, 10, 2):#goes upto 10, that is, 1-9#range is a built in function#third parameter is for increment(optional, deafault=1)
	print(x)

x=5
y=5
z=3

if x<y>z:
	print('y is the greatest.')
if x>y:
	print("x is greater than y.")
elif x<y:
	print('y is greater than x.')
elif y is x:#is can be used instead of ==
	print('y is equal to x.')

temp=func("function parameter")
func2()#no need of parameter as default parameter is already set
print("temp="+str(temp))

def add(*nums):#*allows flexible number of arguments for a function
	sum=0
	for x in nums:
		sum+=x
	return sum

addsum=add(100, 1000, 2000)
print("addsum =", addsum)
addsum=add(100, 1000)
print("addsum =", addsum)
addsum=add(2000)
print("addsum =", addsum)
addsum=add(*list)#unpacking values from a list
print("addsum =", addsum)

groceries={'cereal', 'maggi', 'beer', 'beer'}#a set#different from lists as sets can't have duplicate values
print(groceries)#beer gets printed only once

if 'beer' in groceries:
	print('Yum!')

dictionary={'Me': [50,'Stupid as hell'], 'Others': [100,'Stupider than me'], 'God': ['-','Who?']}#a dictionary consists of a key and a value as every element
print(dictionary)
print(dictionary['Me'][1])
dictionary['Cats']=[20,'Wisest of all'] #adding ndew elements to the dictionary#if this element is already present, it's value changes
print(dictionary)
del dictionary['God']
print(dictionary)

for i, j in dictionary.items():#accessing items of dictionary
	print(i, ":", j)

name=input("What is your name?\n")#to take input from user#the text in the braces appears before the user to tell them the kind of input that is expected%can be left empty

module.sickfunc(name)#calling function of module named 'module'

x=random.randrange(33, 1000)
print(x)

text='Sample text to save.\nNew Line!'
saveFile=open('example.txt', 'w')#the file is opened for writing#all the previous data gets cleared# if the file doesn't exist, it'll be created
saveFile.write(text)#writes in file
saveFile.close()#always close the file

append='\nNew Info!\n'#adds info to the file
appendFile=open('example.txt', 'a')
appendFile.write(append)
appendFile.close()

readMe=open('example.txt', 'r').read()#reads from a file
print(readMe)

readLines=open('example.txt', 'r').readlines()#reads from the file line by line and stores each line as a list
print(readLines)

egtuple = 5, 3, 7, 8 # defining a tuple #iterates faster then list#cannot change value of tuple therefore different thean list
egtuple2 = (3, 7, 8, 6)#another way of defining tuple
print(egtuple)
print(egtuple2[2])

twodlist=[[2, 7], [3, 8], [5, 11]]
print(twodlist)
print(twodlist[2][0])
