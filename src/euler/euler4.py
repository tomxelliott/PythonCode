main():
  for i in range(100,1000):
    for j in range(100,1000):
      fig = i*j
      if str(fig) == str(fig)[::-1]:
        res_i = i
        res_j = j

  print('The greatest combination is ' + str(res_i) + ' and ' + str(res_j)) 

if __name__ == '__main__':
  main()
