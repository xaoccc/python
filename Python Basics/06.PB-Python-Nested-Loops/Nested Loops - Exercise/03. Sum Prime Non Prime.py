sum_non_prime = 0
input_sum = 0

while True:
  input_text = input()
  if input_text == "stop":
    break
  input_text = int(input_text)
  if input_text < 0:
    print("Number is negative.")
    continue
  else:
    input_sum += input_text
    for i in range(2, input_text):
      if input_text % i == 0:
        sum_non_prime += input_text
        break
sum_prime = input_sum - sum_non_prime    

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")