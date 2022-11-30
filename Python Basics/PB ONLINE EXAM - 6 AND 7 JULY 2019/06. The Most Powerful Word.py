from math import floor
word_power = 0
most_word_power = 0
most_pow_word = ""
word = ""
while True:  
  if word == "End of words":
    break  
  if most_word_power < word_power:
    most_word_power = word_power
    most_pow_word = word
  word_power = 0
  word = input()
  for i in range(len(word)):
    word_power += ord(word[i])
  if word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u" or word[0] == "y" or word[0] == "A" or word[0] == "E" or word[0] == "I" or word[0] == "O" or word[0] == "U" or word[0] == "Y":
    word_power *= len(word)
  else:
    word_power = floor(word_power / len(word))
print(f"The most powerful word is {most_pow_word} - {most_word_power}" )
