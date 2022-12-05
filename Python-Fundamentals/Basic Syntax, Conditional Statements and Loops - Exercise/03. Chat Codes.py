msg_num = int(input())
for i in range(msg_num):
  msg = int(input())
  if msg == 88:
    print("Hello")
  elif msg == 86:
    print("How are you?")
  elif msg > 88:
    print("Bye.")
  else:
    print("GREAT!")
