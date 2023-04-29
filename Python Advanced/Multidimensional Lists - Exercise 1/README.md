# Exercises: Multidimensional Lists
##1. Diagonals
Using a nested list comprehension, write a program that reads rows of a square matrix and its elements, separated
by a comma and a space ", ". You should find the matrix's diagonals, prints them, and their sum in the format:  
"Primary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_primary}
Secondary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_secondary}".

#### Examples

| Input | Output |
| ----- | ------ |
| 3<br />1, 2, 33<br />4, 5, 63<br />7, 8, 9 | Primary diagonal: 1, 5, 9. Sum: 15<br />Secondary diagonal: 3, 5, 7. Sum: 15 |

### 2. Diagonal Difference
Write a program that finds the difference between the sums of the square matrix diagonals (absolute value).  