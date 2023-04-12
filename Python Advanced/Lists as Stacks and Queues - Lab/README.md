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

## 4.	Water Dispenser
Write a program that keeps track of people getting water from a dispenser and the amount of water left at the end.  
On the first line, you will receive the starting quantity of water (integer) in a dispenser. Then, on the following lines, you will be given the names of some people who want to get water (each on a separate line) until you receive the command "Start". Add those people in a queue. Finally, you will receive some commands until the command "End":  
-	"{liters}" - litters (integer) that the current person in the queue wants to get. Check if there is enough water in the dispenser for that person.  
*	If there is enough water, print "{person_name} got water" and remove him/her from the queue.
*	Otherwise, print "{person_name} must wait" and remove the person from the queue without reducing the water in the dispenser.
-	"refill {liters}" - add the given litters in the dispenser.  
In the end, print how many liters of water have left in the format: "{left_liters} liters left".  
#### Examples

| Input | Output |
| ----- | ------ |
| 2<br />Peter<br />Amy<br />Start<br />2<br />refill 1<br />1<br />End | Peter got water<br />Amy got water<br />0 liters left |
| 10<br />Peter<br />George<br />Amy<br />Alice<br />Start<br />2<br />3<br />3<br />3<br />End | Peter got water<br />George got water<br />Amy got water<br />Alice must wait<br />2 liters left |

## 5.	Hot Potato
Hot Potato is a game in which children form a circle and toss a hot potato. The counting starts with the first kid. Every nth toss, the child holding the potato leaves the game. When a kid leaves the game, it passes the potato to the next kid. It continues until there is only one kid left.  
Create a program that simulates the game of Hot Potato. On the first line, you will receive kids' names, separated by a single space. On the second line, you will receive the nth toss (integer) in which a child leaves the game.  
Print every kid who is removed from the circle in the format "Removed {kid}". In the end, print the only kid left in the format "Last is {kid}".  
#### Examples

| Input | Output |
| ----- | ------ |
| Tracy Emily Daniel<br />2 | Removed Emily<br />Removed Tracy<br />Last is Daniel |
| George Peter Michael William Thomas<br />10 | Removed Thomas<br />Removed Peter<br />Removed Michael<br />Removed George<br />Last is William<br /> |
| George Peter Michael William Thomas<br />1 | Removed George<br />Removed Peter<br />Removed Michael<br />Removed William<br />Last is Thomas |
