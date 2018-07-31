def sickfunc(x='asshole'):
	print("What the hell is wrong with you", x, "?")

if __name__ == '__main__':#runs if the script running is the script that it is part of
	print("I am in the module.")#runs when we run module.py but does not run when we import module.py to another module

#if we use a print statement without using the above if statement, then the print statement will run whe the module will be imported whether we use the module in the script or not
#when a module is imported it runs once and hence the print statement gets executed
#using this if statement avoids such conditions