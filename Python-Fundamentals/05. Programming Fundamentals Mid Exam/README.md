# Problem 1 - Bonus Scoring System

Create a program that calculates bonus points for each student enrolled in a course. On the first line, you are going to receive the number of the students. On the second line, you will receive the total number of lectures in the course. The course has an additional bonus, which you will receive on the third line. On the following lines, you will be receiving the count of attendances for each student.
The bonus is calculated with the following formula:  
{total bonus} = {student attendances} / {course lectures} * (5 + {additional bonus})  
Find the student with the maximum bonus and print them, along with his attendances, in the following format:  
"Max Bonus: {max bonus points}."  
"The student has attended {student attendances} lectures."  
Round the bonus points at the end to the nearest larger number.

### Input / Constrains

•	On the first line, you are going to receive the number of the students – an integer in the range [0…50]  
•	On the second line, you will receive the number of the lectures – an integer number in the range [0...50].  
•	On the third line, you will receive the additional bonus – an integer number in the range [0….100].  
•	On the following lines, you will be receiving the attendance of each student.  
•	There will never be students with equal bonuses.

### Output

•	Print the maximum bonus points and the attendances of the given student, rounded to the nearest larger number, scored by a student in this course in the format described above.

### Examples  


# Problem 2. Mu Online

You have **initial health 100 and initial bitcoins 0**. You will be given a **string representing the dungeon's rooms**. Each room is separated with '|' (vertical bar): **"room1|room2|room3…"**  
Each room contains **a command and a number**, separated by space. The command can be:  
*	"potion"
    *	You are healed with the number in the second part. But your health cannot exceed your initial health (100).
    *	First print: "You healed for {amount} hp."
    *	After that, print your current health: "Current health: {health} hp."
*	"chest"
    *	You've found some bitcoins, the number in the second part.
    *	Print: "You found {amount} bitcoins."
*	In any other case, you are facing a monster, which you will fight. The second part of the room contains the attack of the monster. You should remove the monster's attack from your health. 
    *	If you are not dead (health <= 0), you've slain the monster, and you should print: "You slayed {monster}."
    *	If you've died, print "You died! Killed by {monster}." and your quest is over. Print the best room you've manage to reach: "Best room: {room}"
If you managed to go through all the rooms in the dungeon, print on the following three lines:  
**"You've made it!"**  
**"Bitcoins: {bitcoins}"**  
**"Health: {health}"**  
### Input / Constraints
You receive a string representing the dungeon's rooms, separated with '|' (vertical bar): "room1|room2|room3…".
### Output
Print the corresponding messages described above.
### Examples
