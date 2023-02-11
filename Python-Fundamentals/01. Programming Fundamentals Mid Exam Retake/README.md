# Problem 1 - Computer Store

Write a program that prints you a receipt for your new computer. You will receive the parts' prices (without tax) until you receive what type of customer this is - special or regular. Once you receive the type of customer you should print the receipt.
The taxes are 20% of each part's price you receive.  
If the customer is special, he has a 10% discount on the total price with taxes.  
If a given price is not a positive number, you should print "Invalid price!" on the console and continue with the next price.  
If the total price is equal to zero, you should print "Invalid order!" on the console.  
### Input
*	You will receive numbers representing prices (without tax) until command "special" or "regular":
### Output
*	The receipt should be in the following format:   
"Congratulations you've just bought a new computer!  
Price without taxes: {total price without taxes}$  
Taxes: {total amount of taxes}$  
-----------  
Total price: {total price with taxes}$"  
Note: All prices should be displayed to the second digit after the decimal point! The discount is applied only on the total price. Discount is only applicable to the final price!  
### Examples

| Input | Output | Comment |
| ----- | ------ | ------- |
| 1050<br />200<br />450<br />2<br />18.50<br />16.86<br />special | Congratulations you've just bought a new computer!<br />Price without taxes: 1737.36$<br />Taxes: 347.47$<br />-----------<br />Total price: 1876.35$ | 1050 – valid price, total 1050<br />200 – valid price, total 1250<br />…<br />16.86 – valid price, total 1737.36<br />We receive special<br />Price is positive number, so it is valid order <br />Price without taxes is 1737.36<br />Taxes: 20% from 1737.36 = 347.47<br />Final price = 1737.36 + 347.47 = 2084.83<br />Additional 10% discount for special customers<br />2084.83 – 10% = 1876.35  |
| 1023 <br />15<br />-20<br />-5.50<br />450<br />20<br />17.66<br />19.30<br />regular | Invalid price!<br />Invalid price!<br />Congratulations you've just bought a new computer!<br />Price without taxes: 1544.96$<br />Taxes: 308.99$<br />-----------<br />Total price: 1853.95$ |  |
| regular | Invalid order! |  |

# Problem 2 - The Lift
Write a program that finds a place for the tourist on a lift.  
Every wagon should have a maximum of 4 people on it. If a wagon is full, you should direct the people to the next one with space available.  
### Input
*	On the first line, you will receive how many people are waiting to get on the lift
*	On the second line, you will receive the current state of the lift separated by a single space: " ".
### Output
When there is no more available space left on the lift, or there are no more people in the queue, you should print on the console the final state of the lift's wagons separated by " " and one of the following messages:  
*	If there are no more people and the lift have empty spots, you should print:
"The lift has empty spots!  
{wagons separated by ' '}"  
*	If there are still people in the queue and no more available space, you should print:  
"There isn't enough space! {people} people in a queue!  
{wagons separated by ' '}"  
*	If the lift is full and there are no more people in the queue, you should print only the wagons separated by " "
### Examples

| Input | Output | Comment |
| ----- | ------ | ------- |
| 15<br />0 0 0 0 | The lift has empty spots!<br />4 4 4 3 | First state - 4 0 0 0 -> 11 people left<br />Second state – 4 4 0 0 -> 7 people left<br />Third state – 4 4 4 0 -> 3 people left |
| 20<br />0 2 0 | There isn't enough space! 10 people in a queue!<br />4 4 4 | First state - 4 2 0  -> 16 people left<br />Second state – 4 4 0  -> 14 people left<br />Third state – 4 4 4 -> 10 people left, but there're no more wagons. |

# Problem 3 - Memory game

Write a program that recreates the Memory game.  
On the first line, you will receive a sequence of elements. Each element in the sequence will have a twin. Until the player receives "end" from the console, you will receive strings with two integers separated by a space, representing the indexes of elements in the sequence.  
If the player tries to cheat and enters two equal indexes or indexes which are out of bounds of the sequence, you should add two matching elements at the middle of the sequence in the following format:  
"-{number of moves until now}a"  
Then print this message on the console:  
"Invalid input! Adding additional elements to the board"  
### Input
*	On the first line, you will receive a sequence of elements
*	On the following lines, you will receive integers until the command "end"
### Output
*	Every time the player hit two matching elements, you should remove them from the sequence and print on the console the following message:
"Congrats! You have found matching elements - ${element}!"
*	If the player hit two different elements, you should print on the console the following message:
"Try again!"
*	If the player hit all matching elements before he receives "end" from the console, you should print on the console the following message: 
"You have won in {number of moves until now} turns!"
*	If the player receives "end" before he hits all matching elements, you should print on the console the following message:
"Sorry you lose :(
{the current sequence's state}"
### Constraints
*	All elements in the sequence will always have a matching element.
Examples

| Input | Output | Comment |
| ----- | ------ | ------- |
| 1 1 2 2 3 3 4 4 5 5 <br />0 1<br />0 -1<br />0 1<br />0 1<br />0 1<br />end | Congrats! You have found matching elements - 1!<br />Invalid input! Adding additional elements to the board<br />Congrats! You have found matching elements - 2!<br />Congrats! You have found matching elements - 3!<br />Congrats! You have found matching elements - -2a!<br />Sorry you lose :(<br />4 4 5 5 | 1)<br />1 0<br />1 1 2 2 3 3 4 4 5 5 –> 1 = 1, equal elements, so remove them. Moves: 1<br />2)<br />-1 0<br />-1 is invalid index so we add additional elements <br />2 2 3 3 -2а -2а 4 4 5 5, Moves: 2<br />3)<br />1 0<br />2 2 3 3 -2а -2а 4 4 5 5 -> 2 = 2, equal elements, so remove them. Moves: 3<br />4)<br />1 0<br />3 3 -2а -2а 4 4 5 5 -> 3 = 3, equal elements, so remove them. Moves: 4<br />5)<br />1 0<br />-2а -2а 4 4 5 5 -> -2а = -2а, equal elements, so remove them. Moves: 5<br />6)<br />You receive the end command.<br />There are still elements in the sequence, so the player loses the game.<br />Final state - 4 4 5 5 |
| a 2 4 a 2 4 <br />0 3 <br />0 2<br />0 1<br />0 1 <br />end<br /> | Congrats! You have found matching elements - a!<br />Congrats! You have found matching elements - 2!<br />Congrats! You have found matching elements - 4!<br />You have won in 3 turns!<br /> |  |
| a 2 4 a 2 4 <br />4 0 <br />0 2<br />0 1<br />0 1 <br />end | Try again!<br />Try again!<br />Try again!<br />Try again!<br />a 2 4 a 2 4 |  |
