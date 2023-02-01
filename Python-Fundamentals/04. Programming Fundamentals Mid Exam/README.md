# Problem 1 - Guinea Pig
Merry has a guinea pig named Puppy, that she loves very much. Every month she goes to the nearest pet store and buys him everything he needs – food, hay, and cover.  
On the first three lines, you will receive the quantity of food, hay, and cover, which Merry buys for a month (30 days). On the fourth line, you will receive the guinea pig's weight.  
Every day Puppy eats 300 gr of food. Every second day Merry first feeds the pet, then gives it a certain amount of hay equal to 5% of the rest of the food. On every third day, Merry puts Puppy cover with a quantity of 1/3 of its weight.  
Calculate whether the quantity of food, hay, and cover, will be enough for a month.  
If Merry runs out of food, hay, or cover, stop the program!  
### Input
*	On the first line – quantity food in kilograms - a floating-point number in the range [0.0 – 10000.0]
*	On the second line – quantity hay in kilograms - a floating-point number in the range [0.0 – 10000.0]
*	On the third line – quantity cover in kilograms - a floating-point number in the range [0.0 – 10000.0]
*	On the fourth line – guinea's weight in kilograms - a floating-point number in the range [0.0 – 10000.0]
### Output
*	If the food, the hay, and the cover are enough, print:
     *	"Everything is fine! Puppy is happy! Food: {excessFood}, Hay: {excessHay}, Cover: {excessCover}."
*	If one of the things is not enough, print:
     *	"Merry must go to the pet store!"
The output values must be formatted to the second decimal place!
### Examples:

| Input | Output | Comments |
| ----- | ------ | -------- |
| 10<br />5<br />5.2<br />1  | Everything is fine! Puppy is happy! Food: 1.00, Hay: 1.10, Cover: 1.87. | You receive food – 10000, hay – 5000, cover – 5200, weight – 1000 (in grams). <br />On the first day, Merry gives Puppy 300gr food – 9700gr food left.<br />On the second day, the food left is 9400gr, so the needed hay is 9400 * 5%  = 470, and the hay left is 4530. <br />On the third day, the cover left is 4866.67, and the food left is 9100, and so on.<br />On the last day, Merry has: food – 1.00, hay – 1.10, and cover – 1.87. |
| 1<br />1.5<br />3<br />1.5  | Merry must go to the pet store! |  |
| 9<br />5<br />5.2<br />1  | Merry must go to the pet store! |  |

# Problem 2 - Shopping List
### Input
You will receive an initial list with groceries separated by an exclamation mark "!".  
After that, you will be receiving 4 types of commands until you receive "Go Shopping!".  
*	"Urgent {item}" - add the item at the start of the list.  If the item already exists, skip this command.  
*	"Unnecessary {item}" - remove the item with the given name, only if it exists in the list. Otherwise, skip this command.
*	"Correct {oldItem} {newItem}" - if the item with the given old name exists, change its name with the new one. Otherwise, skip this command.
*	"Rearrange {item}" - if the grocery exists in the list, remove it from its current position and add it at the end of the list. Otherwise, skip this command.
### Constraints
*	There won't be any duplicate items in the initial list
### Output
*	Print the list with all the groceries, joined by ", ":
"{firstGrocery}, {secondGrocery}, … {nthGrocery}"  
### Examples

| Input | Output | 
| ----- | ------ | 
| Tomatoes!Potatoes!Bread<br />Unnecessary Milk<br />Urgent Tomatoes<br />Go Shopping! | Tomatoes, Potatoes, Bread | 
| Milk!Pepper!Salt!Water!Banana<br />Urgent Salt<br />Unnecessary Grapes <br />Correct Pepper Onion<br />Rearrange Grapes<br />Correct Tomatoes Potatoes<br />Go Shopping! | Milk, Onion, Salt, Water, Banana | 
