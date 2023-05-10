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

| Input | Output |
| ----- | ------ | 
| 4 5<br />1 5 5 2 4<br />2 1 4 14 3<br />3 7 11 2 8<br />4 8 12 16 4 | Sum = 75<br />1 4 14<br />7 11 2<br />8 12 16 | 
| 5 6<br />1 0 4 3 1 1<br />1 3 1 3 0 4<br />6 4 1 2 5 6<br />2 2 1 5 4 1<br />3 3 3 6 0 5 | Sum = 34<br />2 5 6<br />5 4 1<br />6 0 5 | 

## 5. Matrix of Palindromes
Write a program to generate the following matrix of palindromes of 3 letters with r rows and c columns like the one in the examples below.
* Rows define the first and the last letter: row 0 → 'a', row 1 → 'b', row 2 → 'c', …
* Columns + rows define the middle letter:
    * column 0, row 0 → 'a', column 1, row 0 → 'b', column 2, row 0 → 'c', …
    * column 0, row 1 → 'b', column 1, row 1 → 'c', column 2, row 1 → 'd', …
#### Input
* The numbers r and c stay at the first line at the input in the format "{rows} {columns}"
* r and c are integers in the range [1, 26]
#### Examples

| Input | Output |
| ----- | ------ | 
| 4 6 | aaa aba aca ada aea afa<br />bbb bcb bdb beb bfb bgb<br />ccc cdc cec cfc cgc chc<br />ddd ded dfd dgd dhd did | 
| 3 3 | aaa aba<br />bbb bcb<br />ccc cdc | 

## 6. Matrix Shuffling
Write a program that reads a matrix from the console and performs certain operations with its elements. User input is provided similarly to the problems above - first, you read the dimensions and then the data.  
Your program should receive commands in the format: "swap {row1} {col1} {row2} {col2}" where ("row1", "col1") and ("row2", "col2") are the coordinates of two points in the matrix. A valid command starts with the "swap" keyword along with four valid coordinates (no more, no less), separated by a single space.  
* If the command is valid, you should swap the values at the given indexes and print the matrix at each step (thus, you will be able to check if the operation was performed correctly).
* If the command is not valid (does not contain the keyword "swap", has fewer or more coordinates entered, or the given coordinates are not valid), print "Invalid input!" and move on to the following command.
A negative value makes the coordinates not valid.  
Your program should finish when the command "END" is entered.  
#### Examples

| Input | Output |
| ----- | ------ | 
| Input | Output |
| ----- | ------ | 
