key = int(input())
char = int(input())
decrypted_message = ""

for i in range(char):
  message = ord(input())
  decrypted_message += chr(message + key)
print(decrypted_message)
