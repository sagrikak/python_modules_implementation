#!/usr/bin/python #sometimes used in linux to notify linux the path of python so that the script can be executed as executible

import csv
import statistics as s #renaming module for easier use
from statistics import mean, variance as v #importing single function from module
#importing single function from module and renaming it
from struct import *
import heapq
from collections import Counter
from operator import itemgetter

class Calculator:#ususally class named are started with capital
	def addition(x, y):
		added=x+y
		print(added)

	def subtraction(x, y):
		sub=y-x
		print(sub)

	def multiplication(x, y):
		mult=x*y
		print(mult)

	def division(x, y):
		div=y/x
		print(div)

	def double(x):
		return x*2

Calculator.multiplication(3, 33)
Calculator.addition(3, 33)
Calculator.subtraction(3, 33)
Calculator.division(3, 33)
print("--------")

exlist=[4,3,5,8,9,12,33]
x=mean(exlist)#no need to use "s." as the function is imported separately
print(x)
x=s.median(exlist)
print(x)
x=s.stdev(exlist)
print(x)
x=v(exlist)# no need to use complete name as the function is renamed
print(x)

#map#used when we want to perform an operation on all the elements of the list
doubled_list = list(map(Calculator.double, exlist))#list function gathers the results into a list#first argument of map is the function that is to be applied. second is the list
print(doubled_list)
print("--------")

#reading data from csv file
with open('example.csv') as file:
	readcsv=csv.reader(file, delimiter=',')#reads data from csv file

	dates=[]
	colors=[]

	for row in readcsv:#for every row in csv file#each row is treated as an element
		color=row[3]
		date=row[0]

		dates.append(date)
		colors.append(color)

	print(dates)
	print(colors)

	while True:
		try:#if exception occurs, passes it to exception and continues with the program
			whatcolor=input("What color do you want to know the date of?\n")#if user enters a color that does not exist in list, then it is treated as exception
			thedate=dates[colors.index(whatcolor.lower())]#the lower function makes all the letters lowercase so that search for any color does not result negative because of uppercase and lowercase
			print("The date of", whatcolor, "is", thedate)
			break
		except Exception as e:#Exception holds the error statement
			print(e)#prints the error statement
print("--------")

print('''
Multi Line print
Easy, Right?
============
|          |
|    BOX   |
|          |
============
''')

first = ['eight', 'ten', 'zero']
second = ['8', '10', '0']
final = zip(first, second)#zips two lists together
for a, b in final:
	print(a, b)
print("--------")

answer = lambda x, y: x*y#lambda are small functions that do not have any name#are used only once
#x here acts like parameter
print(answer(3, 15))
print("--------")

#finding min, max in a dictionary#sorting a dictionary
stocks = {
	'GOOG' : 520.24,
	'FB' : 76.45,
	'YHOO' : 39.28,
	'AMZN' : 306.21,
	'AAPL' : 99.76
}
#sorting a zipped list is easier than sorting a dictionary so we zip the keys and values of the dictionary together
#while zipping, the first parameter is used to find min, max or sort the zipped list
#so if we want to sort by value, we will use the values as the first parameter while zipping
print(min(zip(stocks.values(), stocks.keys())))
print(max(zip(stocks.values(), stocks.keys())))
print(sorted(zip(stocks.values(), stocks.keys())))

print(min(zip(stocks.keys(), stocks.values())))
print(max(zip(stocks.keys(), stocks.values())))
print(sorted(zip(stocks.keys(), stocks.values())))
print("--------")

#struct can be used to convert data to bytes
packed_data = pack('ifi', 5, 0.195, 17)#stores data as bytes #first parameter takes type of data, i for integer, f for float#remember order
print(packed_data)

print(calcsize('i'))#tells the bytes required to store integer
print(calcsize('f'))#tells the bytes required to store float
print(calcsize('ifi'))#tells the bytes required to store 1 float and 2 ints

#to convert byte data to normal data
original_data = unpack('ifi', packed_data)
print(original_data)
print("--------")

#bitwise operators
a=50     #110010
b=25	 #011001
c=a&b    #010000
print(c)

x=240    #11110000
y=x>>3   #00011110
print(y)
print("--------")

#finding min and max 
newstocks = [#a list of dictionaries
	{'ticker': 'AAPL', 'price': 201},
	{'ticker': 'GOOG', 'price': 800},
	{'ticker': 'F', 'price': 54},
	{'ticker': 'MSFT', 'price': 313},
	{'ticker': 'LVG', 'price': 313}
]

#sorts the list by prices but MSFT apears before LVG(alphabetically LVG should come before)
for x in sorted(newstocks, key=itemgetter('price')):
	print(x)
print("--------")
#sort first by price then by ticker
for x in sorted(newstocks, key=itemgetter('price', 'ticker')):
	print(x)
print("--------")
#heapq function takes first argument as the number of results required #second is the list #third is optional and is used to define key for sorting
print(heapq.nsmallest(2, newstocks, key = lambda newstocks: newstocks['price']))
print(heapq.nlargest(2, newstocks, key = lambda newstocks: newstocks['price']))
print("--------")

#frequency counter#Counter class
sample_text = ""\
  "We are conducting a marathon competitive programming challenge" \
  "September Circuits starting from 15th September 2017."\
  "The objective of September Circuits is to challenge the"\
  "talented and creative minds in competitive programming with"\
  "some interesting algorithmic problems."

words = sample_text.split()#returns a list containing all the words in sample_text
count = Counter(words)
print(count.most_common(3))#prints 3 most common words in text


