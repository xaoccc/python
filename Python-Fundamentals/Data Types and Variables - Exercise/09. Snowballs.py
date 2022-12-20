snowballs = int(input())
highest_value = 0

for i in range(snowballs):
  snowball_weight = int(input())
  snowball_time = int(input())
  snowball_quality = int(input())
  value = (snowball_weight / snowball_time) ** snowball_quality
  if value > highest_value:
    highest_value = value
    weight = snowball_weight
    time = snowball_time
    quality = snowball_quality
print(f"{weight} : {time} = {int(highest_value)} ({quality})")
