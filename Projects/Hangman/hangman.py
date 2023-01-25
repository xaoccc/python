# import urllib.request
import random
def prRed(skk): print("\033[31m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[32m {}\033[00m" .format(skk))
def prBlue(skk): print("\033[34m {}\033[00m" .format(skk))
#word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
#response = urllib.request.urlopen(word_site)
#txt = response.read()
#words_list = txt.splitlines()
words_list = ("python", "jumble", "easy", "difficult", "answer",  "xylophone", "automobile", "microscope", "catastrophy", "telephone", "computer")
word = random.choice(words_list)

computer_input = word[0] + (len(word)-2)*"_" + word[-1]
try_count = 1
prBlue(computer_input)
user_guess = input("Guess the word :")
def strike(user_guess):
    return ''.join([u'\u0336{}'.format(c) for c in user_guess])
if user_guess == word:
    prGreen("Congratulations! You guessed it on the first try!")
else:  
    prRed(strike(user_guess))
    while user_guess != word:
        
        user_choice = input("You can try again, guess just a letter or quit[q] :")
        try_count += 1
        if len(user_choice) > 1:
            if user_choice == word:
                prGreen(f"Congratulations! You guessed the word {word} after {try_count} attempts")
                break
            else:
                prRed(strike(user_choice))
        elif  user_choice == "q":
            break
        elif  len(user_choice) == 1:
          for i in range(len(word)):
            if user_choice == word[i]:            
              computer_input = computer_input[:i] + user_choice + computer_input[i+1:]
          if computer_input != word:
            prBlue(computer_input)
          else:
            prGreen(f"Congratulations! You guessed the word {word} after {try_count} attempts")
            break
