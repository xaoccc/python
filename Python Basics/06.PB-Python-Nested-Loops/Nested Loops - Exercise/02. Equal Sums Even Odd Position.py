num1 = int(input())
num2 = int(input())

for n in range (num1, num2 + 1):
    sum_even_pos, sum_odd_pos = 0, 0
#enumerate намира index и неговата стойност - digit(string) в променливата n
    for index, digit in enumerate(str(n)):
        if index % 2 == 0:
            #превръщаме n в число, за да можем да смятаме
            sum_odd_pos += int(digit)
        else:
            sum_even_pos += int(digit)
    if sum_odd_pos == sum_even_pos:
        print(n, end=' ')
