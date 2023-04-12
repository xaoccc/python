# Lab: Lists as Stacks and Queues

## 1.	Reverse Strings
Write program that:  
*	Reads an input string
*	Reverses it using a stack
*	Prints the result back on the console
#### Examples

| Input | Output |
| ----- | ------ |
| I Love Python | nohtyP evoL I |
| Stacks and Queues | seueuQ dna skcatS |

## 2.	Matching Parentheses
You are given an algebraic expression with parentheses. Scan through the string and extract each set of parentheses.  
Print the result back on the console.  
#### Examples

| Input | Output |
| ----- | ------ |
| 1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5 | (2 + 3)<br />(3 + 1)<br />(2 - (2 + 3) * 4 / (3 + 1)) |
| (2 + 3) - (2 + 3) | (2 + 3)<br />(2 + 3) |

#### Hints
Scan through the expression searching for parentheses:  
*	If you find an opening parenthesis, push the index into the stack.
*	If you find a closing parenthesis, pop the topmost element from the stack. This is the index of the last opening parenthesis.
*	Use the current index and the popped one to extract a set of parentheses.

## 3.	Supermarket
Tom is working at the supermarket, and he needs your help to keep track of his clients. Write a program that reads lines of input consisting of a customer's name and adds it to the end of a queue until "End" is received. If, in the meantime, you receive the command "Paid", you should print each customer in the order they are served (from the first to the last one) and empty the queue. 
When you receive "End", you should print the count of the remaining people in the queue in the format: "{count} people remaining.". 
#### Examples

| Input | Output |
| ----- | ------ |
| George<br />Peter<br />William<br /><br />Paid<br />Michael<br />Oscar<br />Olivia<br />Linda<br />End | George<br />Peter<br />William<br />4 people remaining. |
| Anna<br />Emma<br />Alexander<br />End | 3 people remaining. |
