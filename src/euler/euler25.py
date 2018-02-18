# Not strictly complete implementation since am using 1000 to power of 300 to generate target number.
def main():
  index = 0
  x = 0
  y = 1
  found = ''
  while not found:
    if x > 1000**300:
      found = True
      print('The index is: ' +  str(index) +  ' and Fib number is: ' +  str(x))
    x,y = y, x+y
    index +=1
    
if __name__ == '__main__':
  main()
