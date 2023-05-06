# Exercises: Multidimensional Lists
##1. Diagonals
Using a nested list comprehension, write a program that reads rows of a square matrix and its elements, separated
by a comma and a space ", ". You should find the matrix's diagonals, prints them, and their sum in the format:  
"Primary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_primary}
Secondary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_secondary}".

#### Examples

| Input | Output |
| ----- | ------ |
| 3<br />1, 2, 3<br />4, 5, 6<br />7, 8, 9 | Primary diagonal: 1, 5, 9. Sum: 15<br />Secondary diagonal: 3, 5, 7. Sum: 15 |

## 2. Diagonal Difference
Write a program that finds the difference between the sums of the square matrix diagonals (absolute value).  
On the first line, you will receive an integer N - the size of a square matrix. The following N lines hold the values for each column - N numbers separated by a single space. Print the absolute difference between the primary and the secondary diagonal sums.  

#### Examples

| Input | Output | Comments |
| ----- | ------ | -------- |
| 3<br />11 2 4<br />4 5 6<br />10 8 -12 | 15 | Primary diagonal: sum = 11 + 5 + (-12) = 4<br />Secondary diagonal: sum = 4 + 5 + 10 = 19<br />Difference: \|4 - 19\| = 15 |

## 3. 2x2 Squares in Matrix
Find the number of all 2x2 squares containing identical chars in a matrix. On the first line, you will receive the matrix's dimensions in the format "{rows} {columns}". In the following rows, you will receive characters separated by a single space. Print the number of all square matrices you have found.  
#### Examples

| Input | Output | Comments |
| ----- | ------ | -------- |
| 3 4<br />A B B D<br />E B B B<br />I J B B | 2 | Two 2x2 squares of equal cells:<br />A B B D -- A B B D<br />E B B B -- E B B B<br />I J B B ---- I J B B |
| 2 2<br />a b<br />c d | 0 | No 2x2  squares of equal cells exist.|
| 5 4<br />A A B D<br />A A B B<br />I J B B<br /><br />C C C G<br />C C K P | 3 |Three 2x2 squares of equal cells:<br /> **A A** B D <br /> **A A B B** <br />I J **B B** <br /> **C C** C G <br /> **C C** K P |

## 4. Maximal Sum
Write a program that reads a rectangular matrix's dimensions and finds the 3x3 square with a maximum sum of its elements. There will be no case with two or more 3x3 squares with equal maximal sum.
#### Input
* On the first line, you will receive the rows and columns in the format "{rows} {columns}" – integers in the range [1, 20]
* On the following lines, you will receive each row with its columns - integers, separated by a single space in the range [-20, 20]
#### Output
* On the first line, print the maximum sum of the elements in the 3x3 square in the format "Sum = {sum}"
* On the following 3 lines, print each element of the found submatrix, separated by a single space
#### Examples

| Input | Output | Comments |
| ----- | ------ | -------- |


