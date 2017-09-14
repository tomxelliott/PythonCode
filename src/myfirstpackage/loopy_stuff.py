def fizzbuzz():
  for i in range(0,101):
    if i % 15 == 0:
      print "fizzbuzz"
    elif i % 3 == 0:
      print "fizz"
    elif i % 5 == 0:
      print "buzz"
    else:
      print i
     
def square_me(n):
  if type(n) == int:
    print "Yes, this is an int"
    print n**2
  else:
    "This function only works with integer input"
    
