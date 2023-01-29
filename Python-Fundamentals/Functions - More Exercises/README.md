# More Exercises: Functions

## 1. Data Types

Write a function that, depending on the first line of the input, reads one of the following strings: "int", "real", or "string".  
If the data type is an int, multiply the number by 2.  
If the data type is real, multiply the number by 1.5 and format the result to the second decimal point.  
If the data type is a string, surround the input with "$".  
Print the result on the console.  

#### Examples

| Input  | Output |
| ------------- | ------------- |
| int<br>5 | 10 |
| real<br>2 | 3.00 |
| string<br>hello | $hello$ |

#### Hint
Try to solve the problem using only one method with different overloads.  

## 2. Center Point

You will be given the coordinates of two points on a Cartesian coordinate system - X1, Y1, X2, and Y2 on separate lines. Write a function that prints the point which is closest to the center of the coordinate system (0, 0) in the format: "({X}, {Y})"  
If the points are at the same distance from the center, print only the first one. The resulting coordinates must be formatted to the lower integer.

#### Examples

| Input  | Output |
| ------------- | ------------- |
| 2<br>4<br>-1<br>2 | (-1, 2) |
| 10<br>14.5<br>-17.2<br>16 | (10, 14) |

## 3. Longer Line

You will be given the coordinates of four points. The first and the second pair of points form two different lines.  
Create a function that prints the longer line in the format "({X1}, {Y1})({X2}, {Y2})" starting from the point which is closer to the center of the coordinate system (0, 0). You can reuse the method that you wrote for the previous problem. If the lines are of equal length, print only the first one. The resulting coordinates must be formatted to the lower integer.

#### Examples

| Input  | Output |
| ------------- | ------------- |
| 2<br>4<br>-1<br>2<br>-5<br>-5<br>4<br>3 | (4, -3)(-5, -5) |
| 1<br>2<br>3<br>4<br>9<br>7<br>5<br>6 | (5, 6)(9, 7) |

## 4. Tribonacci Sequence

In the Tribonacci sequence, every number is formed by the sum of the previous 3.  
Write a function that prints numbers from the Tribonacci sequence on one line separated by a single space, starting from 1. You will receive a positive integer number as input.  

#### Examples

| Input  | Output |
| ------------- | ------------- |
| 4 | 1 1 2 4 |
| 8 | 1 1 2 4 7 13 24 44 |

## Multiplication Sign

You will receive three integer numbers. Write a program that finds if their multiplication (the result) is negative, positive, or zero. Try to do this WITHOUT multiplying the 3 numbers.

| Input  | Output |
| ------------- | ------------- |
| 2<br>3<br>-1 | negative |
| 2<br>3<br>1  | positive |
