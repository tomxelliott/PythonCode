def is_int(x):
    if x - int(x) == 0:
        return True
    else:
        return False

def digit_sum(n):
    placeholder = str(n)
    result = 0
    for letter in placeholder:
        result = result + int(letter)
    return result


def factorial(x):
   if x == 0:
       return 1
   else:
       return x * factorial(x - 1)

def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    for n in range(2, x):
        if x % n == 0:
            return False
    else:
        return True

def reverse(text):
      rev_text = ""
      letters = (len(text))
      while letters > 0:
          rev_text += text[letters-1]
          letters -= 1
      return rev_text


def anti_vowel(text):
    vowels = list('aeiouAEIOU')
    text = list(text)

    text = [c for c in text if c not in vowels]

    return ''.join(text)


def censor(text, word):
    return text.replace(word, "*"*len(word))


def count(sequence, item):
    count = 0
    for i in sequence:
        if i == item:
            count += 1
    return count


def purify(x):
    result = []
    for i in x:
        if i % 2 == 0:
            result.append(i)
    return result


def product(array):
    total = 1
    for i in array:
        total *= i
    return total


def remove_duplicates(array):
    result = []
    for i in array:
        if i not in result:
            result.append(i)
    return result


score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
         
def scrabble_score(word):
    total = 0
    wordUpdated = word.lower()
    for i in wordUpdated:
        total += score[i]
    return total

def median(array):
    sort = sorted(array)
    if len(sort) % 2 == 0:
        right = len(sort) / 2
        left = (len(sort) / 2) - 1
        return (sort[right] + sort[left]) / 2.0
    else:
        return sort[len(sort) / 2]
