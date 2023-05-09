# Exercise: Functions Advanced

## 1. Negative vs Positive
You will receive a sequence of numbers (integers) separated by a single space. Separate the negative numbers from  
the positive. Find the total sum of the negatives and positives, and print the following:  
* On the first line, print the sum of the negatives
* On the second line, print the sum of the positives
* On the third line:
    * If the absolute negative number is larger than the positive number:
"The negatives are stronger than the positives"  
    * If the positive number is larger than the absolute negative number:
"The positives are stronger than the negatives"  
Note: you will not receive any zeroes in the input.  
#### Example

| Input | Output |
| ----- | ------ |
| 1 2 -3 -4 65 -98 12 57 -84 | -189<br />137<br />The negatives are stronger than the positives |
| 1 2 3 | 0<br />6<br />The positives are stronger than the negatives |

## 2. Keyword Arguments Length
Create a function called kwargs_length() that can receive some keyword arguments and return their length.  
Submit only your function in the judge system.  
#### Examples

| Test Code | Output |
| ----- | ------ |
| dictionary = {'name': 'Peter', 'age': 25}<br />print(kwargs_length(**dictionary)) | 2 |
| dictionary = {}<br />print(kwargs_length(**dictionary)) | 0 |

## 3. Even or Odd
Create a function called even_odd() that can receive a different quantity of numbers and a command at the end. The command can be "even" or "odd". Filter the numbers depending on the command and return them in a list.  
Submit only your function in the judge system.  
#### Examples

| Test Code | Output |
| ----- | ------ |
| print(even_odd(1, 2, 3, 4, 5, 6, "even")) | [2, 4, 6] |
| print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd")) | [1, 3, 5, 7, 9] |

## 4. Numbers Filter
Create a function called even_odd_filter() that can receive a different number of named arguments. The keys will be "even" and/or "odd", and the values will be a list of numbers.When the key is "odd", you should extract only the odd numbers from its list. When the key is "even", you should extract only the even numbers from its list. The function should return a dictionary sorted by the length of the lists in descending order. There will be no case of lists with the same length.  
Submit only your function in the judge system.  
#### Example

| Test Code | Output |
| ----- | ------ |
| print(even_odd_filter(odd=[1, 2, 3, 4, 10, 5], even=[3, 4, 5, 7, 10, 2, 5, 5, 2],)) | {'even': [4, 10, 2, 2],'odd': [1, 3, 5]} |
| print(even_odd_filter(odd=[2, 2, 30, 44, 10, 5],)) | {'odd': [5]} |

## 5. Concatenate
Write a concatenate() function that receives some strings as arguments and some named arguments (the key will be a string, and the value will be another string). First, you should concatenate all arguments successively. Next, take each key successively, and if it is present in the resulting string, change all matching parts with the key's value. In the end, return the final string. See the examples for more clarification.  
Submit only your function in the judge system.
#### Examples

| Test Code | Output |
| ----- | ------ |
| print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))  | SoftUniIsGreat! |
| print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java')) | I Love Python |

## 6. Function Executor
Create a function called func_executor() that can receive a different number of tuples, each of which will have exactly 2 elements: the first will be a function, and the second will be a tuple of the arguments that need to be passed to that function. You should execute each function and return its result in the format:  
"{function name} - {function result}"   
For more clarification, see the examples below.  
Submit only your function in the judge system.  
#### Examples

| Test Code | Output |
| ----- | ------ |
| `def sum_numbers(num1, num2):` <br />`    return num1 + num2` <br />`def multiply_numbers(num1, num2):`<br />`    return num1 * num2`<br />`print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))`  | sum_numbers - 3<br />multiply_numbers - 8 |
| `def make_upper(*strings):` <br />`    result = tuple(s.upper() for s in strings)` <br />`    return result`<br />`def make_lower(*strings):`<br />`    result = tuple(s.lower() for s in strings)`<br />`    return result`<br />`print(func_executor((make_upper, ("Python", "softUni")), (make_lower, ("PyThOn",)),))`  | make_upper - ('PYTHON', 'SOFTUNI')<br />make_lower - ('python', ) |

## 7. Grocery
Create a function called grocery_store() that receives a different number of key-value pairs. The key will be the product's name and the value - its quantity. You should return a sorted receipt for all products. They should be sorted by their quantity in descending order. If there are two or more products with the same quantity, sort them by their name's length in descending order. If there are two or more products with the same name's length, sort them by their name in ascending order (alphabetically). In the end, return a string in the following format:  
"{product_name1}: {product_quantity1}  
{product_name2}: {product_quantity2}  
…  
{product_nameN}: {product_quantityN}"  
#### Examples

