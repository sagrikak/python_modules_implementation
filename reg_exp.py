#regular expressions is a programming language itself
#can be used to filter data to find useful items
#in this case we'll be using it to separate paragraph data from rest of the html data

import re

examplestr='''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97, and his grandfather Oscar is 102.
'''

ages=re.findall(r'\d{1,3}', examplestr)#r here says that it's a reguar string #searches for numbers with 1-3 digits
names=re.findall(r'[A-Z][a-z]*', examplestr)#searches for a capital letter followed by as many small letters #asterisk is to tell that there can be multiple lowercase letters after the capital letter 

print(ages)
print(names)

agedict={}
x=0
for eachname in names:
	agedict[eachname]=ages[x]
	x+=1
print(agedict)

'''
Identifiers:

\D anything but a number
\d any number
\s space
\S anything but a space
\w any character
\W anything but a character
.  any character except for a new line
\b the white space around words
\. a period

Modifiers:

{x,y} for digits x to y in length
+     match if there is 1 or more occurence
? 	  match if there is 0 or 1 occurence
*     match if there is 0 or more occurence
$     match the end of a string
^     matching the beginning of a string
|     or
[]    range or "variance" eg. [1-5a-qA-Z] searching for numbers b/w 1-5 or letters from a-q(small case) or capital letters
{x}   expecting "x" amount

White Space Characters:

\n new line
\s space
\t tab
\e escape
\f form feed
\r return

Don't Forget!:

.+*?[]$^(){}|\ use escape character to use them

'''