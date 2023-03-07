import string
morse_input = input().split(" | ")
alphabet = list(string.ascii_uppercase)
morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
result = ""

for word in morse_input:
    word = word.split(" ")
    for letter in word:
        for i in range(len(morse)):
            if morse[i] == letter:
                result += alphabet[i]
    result += " "
            
print(result)
