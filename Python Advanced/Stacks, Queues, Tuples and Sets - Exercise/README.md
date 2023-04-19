# Exercise: Stacks, Queues, Tuples, and Sets
## 1.	Numbers
First, you will be given two sequences of integers values on different lines. The values of the sequences are separated by a single space between them.  
Keep in mind that each sequence should contain only unique values.  
Next, you will receive a number - N. On the next N lines, you will receive one of the following commands:  
*	"Add First {numbers, separated by a space}" - add the given numbers at the end of the first sequence of numbers.
*	"Add Second {numbers, separated by a space}" - add the given numbers at the end of the second sequence of numbers.
*	"Remove First {numbers, separated by a space}" - remove only the numbers contained in the first sequence.
*	"Remove Second {numbers, separated by a space}" - remove only the numbers contained in the second sequence.
*	"Check Subset" - check if any of the given sequences are a subset of the other. If it is, print "True". Otherwise, print "False".
In the end, print the final sequences, separated by a comma and a space ", ". The values in each sequence should be sorted in ascending order.  
#### Examples

| Input | Output |
| ----- | ------ |
| 1 2 3 4 5<br />1 2 3<br />3<br />Add First 5 6<br />Remove Second 8 9 11<br />Check Subset | True<br />1, 2, 3, 4, 5, 6<br />1, 2, 3 |
| 5 4 2 9 9 5 4<br />1 1 1 5 6 5<br />4<br />Add First 5 6 9 3<br />Add Second 1 2 3 3 3<br />Check Subset<br />Remove Second 1 2 3 4 5 | False<br />2, 3, 4, 5, 6, 9<br />6 |

## 2.	Expression Evaluator
Write a program that evaluates a string expression. You will be given that string expression on the first line in the form of numbers and operators separated with a single space from each other. Your job is to take that string expression and calculate the result after evaluating it.  
To do that, you have to follow a simple rule. If, for example, we have this string "2 4 * 1 3 -", the first time we meet an operator (\*), we should take all the numbers we have so far (2, 4), apply that operation to them, and save the result (8). The next time we meet an operator (-), we again take all the numbers we have (8, 1, 3) and apply the operator to them in that order (8 - 1 - 3 = 4). In the end, we print the result.  
All the numbers will always be integers, and the possible operators are "\*", "+", "-", "/". It is important to keep the order of the numbers (especially for "/" and "-" because the order matters). When having a division, you should round the result to the lower integer.  
#### Input
*	Single line: a string containing integers and operators
#### Output
*	Single number: the result after the evaluation
#### Constrains
*	When reaching an operator, it is sure that you will have a minimum of one number to evaluate
*	The string will always end with an operator, so you get one number as a result
*	Operators and numbers will always be valid
*	There will be no case of division by zero
*	There might be negative numbers in the string
#### Examples

| Input | Output | Comment |
| ----- | ------ | ------ |
| 6 3 - 2 1 * 5 / | 1 | 6 - 3 = 3<br />3 * 2 * 1 = 6<br />6 / 5 = 1 |
| 2 2 - 1 * | 0 | 2 - 2 = 0<br />0 * 1 = 0 |
| 10 23 * 4 2 / 30 10 + 100 50 - 2 -1 * | 164 | 10 * 23 = 230<br />230 / 4 / 2 = 28<br />28 + 30 + 10 = 68<br />68 - 100 - 50 = -82<br />-82 * 2 * -1 = 164 |

