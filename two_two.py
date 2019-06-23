print('Top Level at two')
from MyMainPackage import one_two

if __name__ == '__main__':
	print('TWO IS BEING USED DIRECTLY')
	one_two.func(5)
else:
	print('Two is being imported')