a1 = int(input())
a2 = int(input())
n = int(input())
 
for fourth in range(a1, a2):
  first = chr(fourth)
  for second in range(1, n):
    for third in range(1, int(n / 2)):
      if fourth % 2 != 0 and (second + third + fourth) % 2 != 0:
        
        print(f"{first}-{second}{third}{fourth}")
