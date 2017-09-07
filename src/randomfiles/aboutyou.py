#########################
### Input args in Py3 ###
#########################

def main():
	print("What is your name: ", end="")
	name = input()

	print("What is your age: ", end="")
	age = input()
	s = int(age)

	print("You are {} and you are {:.1f}".format(name,s))
	exit(0)


if __name__ == '__main__':
	main()
