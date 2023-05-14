# Apocalypse Preparation

You are in the middle of a zombie apocalypse and you want to go out for exploration. But before you do that, you need to prepare some healing items.  
On the first line, you will be given a sequence representing textiles. On the second line, you will be given another sequence, which represents medicaments.  
While both collections contain any elements, you will have to combine elements from the collections in order to create healing items. You should start by getting the first value of textile and the last value of medicaments:  
*	If their sum is equal to any of the items in the table below create that item and remove both values. 
*	Otherwise, check if the sum is bigger than the value of the MedKit, create the MedKit, remove both values, and add the remaining resources(of the sum) to the next value in the medicament collection (Take the element from the collection, add the remaining sum to it, and put the element back to its place).
*	If you can’t create anything, remove the textile value, add 10 to the medicament value, and return the medicament back to its place, into its collection. 
You need to stop creating healing items when either the textile or the medicaments are exhausted.  

| Healing item | Resources needed |
| ------------ | ---------------- |
| Patch | 30 |
| Bandage | 40 |
| MedKit | 100 |

In the end, you should print on the console message for the sequence that has ended, then the created items, and in the end the remaining items (if any).
### Input
*	On the first line, you will receive a sequence of integers representing the textiles, separated by a single space (" ").
*	On the second line, you will receive a sequence of integers representing the medicaments, separated by a single space (" ").
### Output
*	On the first line print which one of the collections is over:
    *	If the textile is over print: "Textiles are empty."
    *	If the medicaments are over print: "Medicaments are empty."
    *	If both are empty print: "Textiles and medicaments are both empty."
*	On the next n lines print only the created items (if any) ordered by the amount created descending, then by name alphabetically:
"{item name} - {amount created}  
  {item name} - {amount created}  
…  
"  
Hint: Do not print items, which are not created.  
*	On the last line print the remaining items(if any):
    *	If there are any medicaments left: 
 "Medicaments left: …{medicament2}, {medicament1}"  
    *	If there are any textiles left:  
"Textiles left: {textile1}, {textile2}…"  
### Constraints
*	All the numbers will be in the range [0…1000].
*	All the inputs will be valid.
### Examples

| Input | Output |
| ----- | ------ |
| 20 10 40 70 20<br />10 50 10 30 20 80 | Textiles are empty.<br />MedKit - 2<br />Bandage - 1<br />Patch - 1<br />Medicaments left: 50, 10 |
| 30 30 10 80 60<br />40 20 30 10 70 | Textiles and medicaments are both empty.<br />MedKit - 3<br />Bandage - 2 |
| 30 30 10 80 60 20<br />40 20 30 10 70 | Medicaments are empty.<br />MedKit - 3<br />Bandage - 2<br />Textiles left: 20 |
| 60 15 20 30 20<br />20 15 40 | Medicaments are empty.<br />Bandage - 1<br />MedKit - 1<br />Patch - 1<br />Textiles left: 30, 20 |

# 02. Blind Man’s Buff
Blind man's buff is played in a spacious area, such as outdoors or in a large room, in which one player, is blindfolded and gropes around attempting to touch the other players without being able to see them…  
You will be given N and M – integers, indicating the playground’s dimensions. On the next N lines, you will receive the rows of the playground, with M columns. You will be marked with the letter 'B', and placed in a random position. In random positions, furniture or other obstacles will be marked with the letter 'O'. The other players (opponents) will be marked with the letter 'P'. There will always be three other players participating in the game. All of the empty positions will be marked with '-'.  
Your goal is to touch as many players as possible during the game, without leaving the playground or stepping on an obstacle.
On the next few lines, until you receive the command "Finish", you will receive a few lines with commands representing which direction you need to move. The possible directions are "up", " down", "right", and "left". If the direction leads you out of the field, you need to stay in position inside the field(do NOT make the move). If you have an obstacle, towards the direction, do NOT make the move and wait for the next command.  
You need to keep track of the count of touched opponents and the moves you’ve made.  
In case you step on a position marked with '-', increase the count of the moves made.  
When you receive a command with direction, you check the position you need to step on for an obstacle or opponent. If there is an opponent, you touch him and the position is marked with '-'(increase the count of the touched opponents and moves made), and this is your new position.   
The game is over when you manage to touch all other opponents or the given command is "Finish". A game report is printed on the Console:  
"Game over!"  
"Touched opponents: {count} Moves made: {count}"  

### Input
*	On the first line, you'll receive the dimensions of the playground in the format: "N M", where N is the number of rows, and M is the number of columns. They'll be separated by a single space (" ").
*	On the next N lines, you will receive a string representing the respective row of the playground. The positions in every string will be separated by a single space (" ").  
*	On the next few lines, until you receive the command "Finish", you will be given directions (up, down, right, left).   
### Output
*	When the game is over, the following output should be printed on the Console:
"Game over!"
"Touched opponents: {count} Moves made: {count}"
### Constraints
*	The playground size will be a 32-bit integer in the range [2 … 2 147 483 647].
*	The playground will always have three opponents in it - 'P'.
*	The obstacles on the playground will always be random count, and there will be cases without any obstacles.
### Examples
