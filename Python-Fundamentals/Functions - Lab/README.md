# Lab: Functions
## 1. Absolute Values
Write a program that receives a sequence of numbers, separated by a single space, and prints their absolute value as a list. Use abs().
#### Example

| Input | Output |
| ----- | ------ |
| 1 2.5 -3 -4.5 | [1.0, 2.5, 3.0, 4.5] |
| -0 1 10 -6.66 | [0.0, 1.0, 10.0, 6.66] |

## 2. Grades
Write a function that receives a grade between 2.00 and 6.00 and prints the corresponding grade in words.  
2.00 – 2.99 - "Fail"  
3.00 – 3.49 - "Poor"  
3.50 – 4.49 - "Good"  
4.50 – 5.49 - "Very Good"  
5.50 – 6.00 - "Excellent"  
#### Example

| Input | Output |
| ----- | ------ |
| 3.33 | Poor |
| 4.50 | Very Good |
| 2.99 | Fail |

## Calculations
Create a function that receives three parameters, calculates a result depending on the given operator, and returns it. Print the result of the function.  
The input comes as three parameters – an operator as a string and two integer numbers. The operator can be one of the following:  "multiply", "divide", "add", "subtract".  
#### Example

| Input | Output |
| ----- | ------ |
| subtract<br />5<br />4 | 1 |
| divide<br />8<br />4 | 2 |

Print the result by calling the function and passing the given parameters.
## 3. Repeat String
Write a function that receives a string and a counter n. The function should return a new string – the result of repeating the old string n times. Print the result of the function. Try using lambda.  
#### Example

| Input | Output |
| ----- | ------ |
| abc<br />3 | abcabcabc |
| String<br />2 | StringString |

## 4. Orders
Write a function that calculates the total price of an order and returns it. The function should receive one of the following products: "coffee", "coke", "water", or "snacks", and a quantity of the product. The prices for a single piece of each product are:  
coffee - 1.50  
water - 1.00  
coke - 1.40  
snacks - 2.00  
Print the result formatted to the second decimal place.  
#### Example

| Input | Output |
| ----- | ------ |
| water<br />5 | 5.00 |
| coffee<br />2 | 3.00 |

## 5. Calculate Rectangle Area
Create a function that calculates and returns the area of a rectangle by given width and height. Print the result on the console.  
#### Example

| Input | Output |
| ----- | ------ |
| 3<br />4 | 12 |
| 6<br />2 | 12 |

## 6. Rounding
Write a program that rounds all the given numbers, separated by a single space, and prints the result as a list. Use round().
#### Example

| Input | Output |
| ----- | ------ |
| 1.0 2.5 3.0 4.5 | [1, 2, 3, 4] |
| 2.56 1.9 -3.4 8.1 | [3, 2, -3, 8] |
