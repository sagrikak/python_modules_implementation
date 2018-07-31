from operator import attrgetter

#learning about "self" word
class Enemy:
	life=3#class variable
	def __init__(self, name):#like constructor
		self.name=name#instance variable #depends on instance
		print(name, "has full life!")

	def attack(self):
		print(self.name + ': Ouch!')
		self.life-=1#accessing variables of the class we are working on

	def checkLife(self):
		if self.life <= 0:
			print(self.name + ': I am dead!')
		else:
			print(self.name + ":", str(self.life), "life left")

#creating an object
enemy1 = Enemy("C")#each object is like a copy of a class
enemy2 = Enemy("S")

enemy1.attack()
enemy1.attack()
enemy1.checkLife()
enemy2.checkLife()
enemy1.attack()
enemy1.checkLife()
print("--------")

#Inheritence
class Mario():
	def move(self):
		print('I am moving!')

class Shroom():
	def eat_shroom(self):
		print('Now I am big!')

class BigMario(Mario, Shroom):#multiple inheritence
	pass#class can't be empty#this does nothing

bm=BigMario()
bm.move()
bm.eat_shroom()
print("--------")

#sorting class objects by attributes
class User:
	def __init__(self, x, y):
		self.name = x
		self.id = y

	#repr - representation
	def __repr__(self):#decides what to print if object is to be printed
		return self.name + " : " + str(self.id)

users = [
	User('Batman', 77),
	User('Catwoman', 88),
	User('Ironman', 98),
	User('Superman', 95),
	User('Aquaman', 25),	
]

for user in sorted(users, key=attrgetter('name')):
	print(user)
print("--------")
for user in sorted(users, key=attrgetter('id')):
	print(user)
print("--------")	