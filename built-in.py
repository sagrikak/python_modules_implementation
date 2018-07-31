import os
import time
import sys
import random
import urllib.request
import urllib.parse
import re

num1=-5
print(abs(num1))
#help()  #gives info about the modules#press q to quit
list=[5,2,6,7,8,0]
print(max(list))
print(min(list))
print(round(5.6))
print(round(5.4))
print(round(5.5))
print(round(6.5))

curdir=os.getcwd()#gets the location of current working directory
print(curdir)
os.mkdir('newDir')#creates a new directory
time.sleep(2)#just so that the changes can b e viewed while they are happening
os.rename('newDir', 'newDir2')#renaming a directory
time.sleep(2)
os.rmdir('newDir2')#removing directory

sys.stderr.write('test\n')#prints error like message
sys.stderr.flush()
sys.stdout.write('test\n')#prints text
print(sys.argv)#prints the arguments that we pass in command line
#eg, type python built-in.py "Running ok" in command line
#sys.argv will print ['built-in.py', 'Running ok']
if len(sys.argv) > 1:
	print(sys.argv[1])#prints "Running ok" only

def download_web_image(url):#function to download image from web using url
	name=random.randrange(1, 1000)#assigning random number as name
	fullname=str(name)+".jpg"#assigning format
	urllib.request.urlretrieve(url, fullname)#retrieving image from "url" and naming it "fullname"
download_web_image("http://cdn.collider.com/wp-content/uploads/rodrigo-santoro.jpg")
print("Image Downloaded")

#following code to download a csv file does not work because of unauthorized access.
#it would work for a file which does not have such security
'''
#link of the csv file to be downloaded
goog_url='https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1502802872&period2=1505481272&interval=1d&events=history&crumb=Ov6NHXcEhlT'

def download_csv_file(url):
	response=urllib.request.urlopen(url)#saving the response in a variable
	csv_file=response.read()
	csv_str=str(csv_file)
	lines=csv_str.split("\\n")#takes a string and breaks it up whenever it comes across '\n' character
	destination=r'google.csv'
	write_file=open('destination', 'w')
	for line in lines:
		write_file.write(line + "\n")
	write_file.close()

download_csv_file(goog_url)
print("CSV file downloaded")
'''

#the page we're looking for is https://www.pythonprogramming.net/?s=basic&submit=search
url='http://pythonprogramming.net'
values={'s': 'basic', 'submit':'search'}#stores values to be parsed

data=urllib.parse.urlencode(values)#encodes the values to be parsed in the form of a url
data=data.encode('utf-8')#type of encoding to be used
req=urllib.request.Request(url, data)#requesting data from complete url  
resp=urllib.request.urlopen(req)#storing the response, that is the source code of the webpage in variable
respdata=resp.read()

file=open('source_code.txt', 'w')
file.write(str(respdata))#reading the response and writing it to a text file
file.close()
print("Source code downloaded")
#some popular sites might not allow programs to access their data. To get around their security, watch 37th video of python tutorials by sentdex

paragraphs=re.findall(r'<p>(.*?)</p>', str(respdata))#to find everything b/w <p> and </p>

anotherfile=open('website_data.txt', 'a')

for eachP in paragraphs:
	anotherfile.write(eachP)
anotherfile.close()
print("Website Data downloaded")

