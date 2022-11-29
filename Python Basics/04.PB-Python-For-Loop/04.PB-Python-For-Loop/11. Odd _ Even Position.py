#input
inputs_count = int(input())
number_sum_even = 0
number_sum_odd = 0
max_num_even = -100000
max_num_odd = -100000
min_num_even = 100000
min_num_odd = 100000

#logic
for i in range (1, inputs_count + 1):
#counting all the inputs
    number = float(input())
#checking for even number
    if i % 2 == 0 :
#suming even numbers
        number_sum_even += number
#checking for max even number
        if number > max_num_even :
            max_num_even = number
#checking for min even number
        if number < min_num_even :
            min_num_even = number
#suming odd numbers
    elif i % 2 != 0 :
        number_sum_odd += number
#checking for max odd number
        if number > max_num_odd :
            max_num_odd = number
#checking for min even number
        if number < min_num_odd :
            min_num_odd = number  

number_sum_odd_print = f"OddSum={number_sum_odd:.2f},"
number_sum_even_print = f"EvenSum={number_sum_even:.2f},"
min_num_odd_print = f"OddMin={min_num_odd:.2f},"
max_num_odd_print = f"OddMax={max_num_odd:.2f},"
min_num_even_print = f"EvenMin={min_num_even:.2f},"
max_num_even_print = f"EvenMax={max_num_even:.2f}"
if inputs_count == 1 :
    min_num_even_print = "EvenMin=No,"
    max_num_even_print = "EvenMax=No"
elif inputs_count == 0 :
    min_num_even_print = "EvenMin=No,"
    max_num_even_print = "EvenMax=No"
    min_num_odd_print = "OddMin=No,"
    max_num_odd_print = "OddMax=No,"

#print output
print(number_sum_odd_print)
print(min_num_odd_print)
print(max_num_odd_print)
print(number_sum_even_print)
print(min_num_even_print)
print(max_num_even_print)
