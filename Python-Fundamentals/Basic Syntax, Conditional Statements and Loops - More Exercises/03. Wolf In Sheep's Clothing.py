sheeps_str = input()
sheeps = sheeps_str.split(", ")
if sheeps[-1] == "wolf" :
  print("Please go away and stop eating my sheep")
else:
  print(f"Oi! Sheep number {len(sheeps) -sheeps.index('wolf') - 1}! You are about to be eaten by a wolf!" )
