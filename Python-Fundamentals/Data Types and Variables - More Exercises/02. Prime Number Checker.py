num = int(input())
is_prime = 0

for i in range(1, num + 1):
  if num % i == 0:
    is_prime += 1
    if is_prime > 2:
      break
print(is_prime <= 2)
