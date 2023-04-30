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

### 2. Diagonal Difference
Write a program that finds the difference between the sums of the square matrix diagonals (absolute value).  
On the first line, you will receive an integer N - the size of a square matrix. The following N lines hold the values for each column - N numbers separated by a single space. Print the absolute difference between the primary and the secondary diagonal sums.  

#### Examples

| Input | Output | Comments |
| ----- | ------ | -------- |
| 3<br />11 2 4<br />4 5 6<br />10 8 -12 | 15 | Primary diagonal: sum = 11 + 5 + (-12) = 4<br />Secondary diagonal: sum = 4 + 5 + 10 = 19<br />Difference: \|4 - 19\| = 15 |

### 3. 2x2 Squares in Matrix
