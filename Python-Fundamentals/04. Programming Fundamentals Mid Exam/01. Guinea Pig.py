food = float(input())
hay = float(input())
cover = float(input())
weight = float(input())
day = 0

while day < 31:
    day += 1
    if day == 31:
        break
    food -= 0.3
    if day % 2 == 0:
        hay -= (food * 0.05)
    if day % 3 == 0:
        cover -= (weight / 3)
    if food <= 0 or hay <= 0 or cover <= 0:
        print("Merry must go to the pet store!")
        break
        
if day == 31:
    print(f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")
