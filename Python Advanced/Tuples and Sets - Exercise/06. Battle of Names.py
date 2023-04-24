number_of_names = int(input())

odd_numbers = set()
even_numbers = set()

for i in range(1, number_of_names + 1):
    current_sum = 0
    for char in input():
        current_sum += ord(char)
    current_sum //= i
    if current_sum % 2 == 0:
        even_numbers.add(current_sum)
    else:
        odd_numbers.add(current_sum)
if sum(even_numbers) > sum(odd_numbers):
    print(*even_numbers ^ odd_numbers, sep=", ")
elif sum(even_numbers) == sum(odd_numbers):
    print(*odd_numbers | even_numbers, sep=", ")
else:
    print(*odd_numbers - even_numbers, sep=", ")
