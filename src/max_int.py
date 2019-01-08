def main():
	max_int_val('01230')
	max_int_val('891')

def max_int_val(input):
	x = [int(i) for i in input]
	result = x[0]
	index = 0
	while index < len(x) - 1:
		if result + x[index+1] > result * x[index+1]:
			result = result + x[index+1]
		else:
			result = result * x[index+1]
		index += 1

	print result


if __name__=='__main__':
	main()
	# Expected results:
	# 9
	# 73
