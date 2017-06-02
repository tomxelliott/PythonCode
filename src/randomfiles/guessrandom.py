from random import randint

def guessRandom():
  guesses_left = 3
  while guesses_left > 0:
    random_number = randint(1, 10)
    guess = int(raw_input("Your guess: "))
    if guess == random_number:
        print 'You win!'
        break
    guesses_left = guesses_left -1
  else:
    print 'You lose.'
