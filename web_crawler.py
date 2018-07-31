import requests
from bs4 import BeautifulSoup#beautifulsoup is a combination of urllib + regular expressions
import operator

def spider(max_pages):
	page=1
	while page<=max_pages:
		url='https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/' + str(page)
		source=requests.get(url)
		plain_text=source.text#converting response to text
		soup=BeautifulSoup(plain_text, "lxml")#specifying use of lxml parser
		for link in soup.findAll('a', {'class': 'dark'}):#find all <a> tags with class attribute equal to "dark"
			href = 'https://www.hackerearth.com' + link.get('href')#get the value of href in the <a> tag
			title = link.string#get the hypertext 
			print(title)
			get_problem_data(href)#getting info about each link by visiting that link
			print(href, "\n")
		page+=1

#gets the names of tags associated with the problem
def get_problem_data(prob_url):
	source=requests.get(prob_url)
	plain_text=source.text#converting response to text
	soup=BeautifulSoup(plain_text, "lxml")
	for tag in soup.findAll('span', {'class': 'dark small less-margin-right tags-list weight-400'}):
		print(tag.string)

spider(0)#number of pages can be specified

#word frequency counter
def count(url):
	word_list = []#list to store word on the webpage
	source = requests.get(url).text#getting source code and converting it to text
	soup = BeautifulSoup(source, "lxml")#creating BeautifulSoup object
	for link in soup.findAll('a', {'class': 'dark'}):#finding all the tags with links to videos
		content = link.string#getting the value of title from the tag as that is the name of the video
		words = content.lower().split()#converting all the letters to lowercase and separating all the words in the title so that the same words can be matched correctly
		for word in words:
			word_list.append(word)#adding each word to word_list
	clean_up_list(word_list)

#cleaning up the list by removing symbols from the words
def clean_up_list(list):
	clean_list=[]
	for word in list:
		symbols = "!@#$%^&*()-_+=~`[]\{\}|\:;"'<,>.?/'
		for i in range(0, len(symbols)):
			word = word.replace(symbols[i], "")
		if len(word) > 0:
			clean_list.append(word)
	create_dict(clean_list)

#creating a dictionary to store the frequency along with words
def create_dict(list):
	word_count = {}#creating a dictionary
	for word in list:
		if word in word_count:
			word_count[word] += 1
		else:
			word_count[word] = 1
	#sorting word_count dictionary by value #the key in second parameter of sorted does not refer to key in the dictionary #to sort by value, we use itemgetter(1), to sort by key we use itemgetter(0) 
	for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
		print(key, value)

count("https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/")