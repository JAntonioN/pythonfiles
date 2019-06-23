#one py all the code in the indentation 0 is going to be run in the cmd

# __name__ = '__main__'  #this happens internally when you run the python code in cmd
# you define first the functions and then you run the code with the if __name__=='__main__'

#if __name__ == '__main__': #we are going to run these directly
#	myfunc()

def func():
	print('Func() in one.py')

print('Top level in one.py')

if __name__ == '__main__':
	print('One.py is being run directly!')
else:
	print('One.py is being imported!')

#Usually what is made is;
#if __name__ == '__main__':
	#run the code that was defined in the top level of the code
