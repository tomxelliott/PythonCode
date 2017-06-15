my_list = [i**2 for i in range(1,11)]

my_file = open("output.txt", "r+")
# passing "r+" as a second argument to the function so the file will allow you to read and write to it

# Add your code below!
for i in my_list:
    my_file.write(str(i) + "\n")

my_file.close()
