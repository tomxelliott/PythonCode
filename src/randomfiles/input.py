raw_input("Enter a word:")
original = raw_input()
if len(original) > 0 and original.isalpha(): #isalpha() checks if the string contains non-letter characters
    word = original.lower()
    first = word[0]
    print original
else:
    print "empty"

    
hobbies = []

for i in range(3):
    hobby = str(raw_input("Your hobby: "))
    hobbies.append(hobby)
