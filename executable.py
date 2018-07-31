#!/usr/bin/python #sometimes used in linux to notify linux the path of python so that the script can be executed as executible

import statistics as s #renaming module for easier use
from statistics import mean, variance as v #importing single function from module
 #importing single function from module and renaming it

class calculator:
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

calculator.multiplication(3, 33)
calculator.addition(3, 33)
calculator.subtraction(3, 33)
calculator.division(3, 33)

exlist=[4,3,5,8,9,12,33]
x=mean(exlist)#no need to use "s." as the function is imported separately
print(x)
x=s.median(exlist)
print(x)
x=s.stdev(exlist)
print(x)
x=v(exlist)# no need to use complete name as the function is renamed
print(x)

print('''
Multi Line print
Easy, Right?
============
|          |
|    BOX   |
|          |
============
''')