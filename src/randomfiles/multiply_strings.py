def main():
	print mult_str("33", "2")
	print mult_str("11","23")



def mult_str(a,b):
	try:
		result = int(a) * int(b)
		return result
	except TypeError as e:
		print(e)


if __name__ == '__main__':
	main()
