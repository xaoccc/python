#If we have a long list with numbers and we want to find out which are prime
input_list = [int(i) for i in input().split()]
new_list = []

def is_prime(n) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = int(n**0.5)
    for i in range(5, limit+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True

#Here we filter and get just the prime numbers
result = filter(is_prime, input_list)

for n in result:
     new_list.append(n)
     #We can print each prime number
     print(n)
#Or we can store them in a list
print(new_list)
