coffee_needed = 0
while True:
  activity = input()
  if activity == "END":
    break
  elif activity == "coding" or activity == "cat" or activity == "dog" or activity == "movie":
    coffee_needed += 1
  elif activity == "CODING" or activity == "CAT" or activity == "DOG" or activity == "MOVIE":
    coffee_needed += 2
  else:
    continue
if coffee_needed > 5:
  print("You need extra sleep")
else:
  print(coffee_needed)
