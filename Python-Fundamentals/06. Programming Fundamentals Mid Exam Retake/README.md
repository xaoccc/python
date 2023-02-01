# Problem 1 - Black Flag 

Pirates are invading the sea, and you're tasked to help them plunder  
Create a program that checks if target plunder is reached. First, you will receive how many days the pirating lasts. Then you will receive how much the pirates plunder for a day. Last you will receive the expected plunder at the end.  
Calculate how much plunder the pirates manage to gather. Each day they gather the plunder. Keep in mind that they attack more ships every third day and add additional plunder to their total gain, which is 50% of the daily plunder. Every fifth day the pirates encounter a warship, and after the battle, they lose 30% of their total plunder.  
If the gained plunder is more or equal to the target, print the following:  
**"Ahoy! {totalPlunder} plunder gained."**  
If the gained plunder is less than the target. Calculate the percentage left and print the following:   
**"Collected only {percentage}% of the plunder."**  
Both numbers should be formatted to the 2nd decimal place.
### Input
*	On the 1st line, you will receive the days of the plunder – an integer number in the range [0…100000]
*	On the 2nd line, you will receive the daily plunder – an integer number in the range [0…50]
*	On the 3rd line, you will receive the expected plunder – a real number in the range [0.0…10000.0]
### Output
*	 In the end, print whether the plunder was successful or not, following the format described above.
### Examples

| Input | Output | Comments |
| ----- | ------ | -------- |
| 5<br />40<br />100 | Ahoy! 154.00 plunder gained. | The days are 5, and the daily plunder is 40. On the third day, the total plunder is 120, and since it is a third day, they gain an additional 50% from the daily plunder, which adds up to 140. On the fifth day, the plunder is 220, but they battle with a warship and lose 30% of the collected cargo, and the total becomes 154. That is more than expected. |
| 10<br />20<br />380 | Collected only 36.29% of the plunder. | |

# Problem 2 - Treasure Hunt

The pirates need to carry a treasure chest safely back to the ship, looting along the way.
Create a program that manages the state of the treasure chest along the way. On the first line, you will receive the initial loot of the treasure chest, which is a string of items separated by a "|".  
"{loot1}|{loot2}|{loot3} … {lootn}"  
The following lines represent commands until "Yohoho!" which ends the treasure hunt:  
*	"Loot {item1} {item2}…{itemn}":
    *	Pick up treasure loot along the way. Insert the items at the beginning of the chest. 
    *	If an item is already contained, don't insert it.
*	"Drop {index}":
    *	Remove the loot at the given position and add it at the end of the treasure chest. 
    *	If the index is invalid, skip the command.
*	"Steal {count}":
    *	Someone steals the last count loot items. If there are fewer items than the given count, remove as much as there are. 
    *	Print the stolen items separated by ", ":  
"{item1}, {item2}, {item3} … {itemn}"  
In the end, output the average treasure gain, which is the sum of all treasure items length divided by the count of all items inside the chest formatted to the second decimal point:
"Average treasure gain: {averageGain} pirate credits."
If the chest is empty, print the following message:
"Failed treasure hunt."
### Input
*	On the 1st line, you are going to receive the initial treasure chest (loot separated by "|")
*	On the following lines, until "Yohoho!", you will be receiving commands.
### Output
*	Print the output in the format described above.
### Constraints
*	The loot items will be strings containing any ASCII code.
*	The indexes will be integers in the range [-200…200]
•	The count will be an integer in the range [1….100]
### Examples

| Input | Output | Comments |
| ----- | ------ | -------- |
| Gold\|Silver\|Bronze\|Medallion\|Cup<br />Loot Wood Gold Coins<br />Loot Silver Pistol<br />Drop 3<br />Steal 3<br />Yohoho! | Medallion, Cup, Gold<br />Average treasure gain: 5.40 pirate credits. | The first command "Loot Wood Gold Coins" adds Wood and Coins to the chest but omits Gold since it is already contained. The chest now has the following items:<br />Coins Wood Gold Silver Bronze Medallion Cup<br />The second command adds only Pistol to the chest<br />The third command "Drop 3" removes the Gold from the chest, but immediately adds it at the end:<br />Pistol Coins Wood Silver Bronze Medallion Cup Gold<br />The fourth command "Steal 3" removes the last 3 items Medallion, Cup, Gold from the chest and prints them. <br />In the end calculate the average treasure gain which is the sum of all items length Pistol(6) + Coins(5) + Wood(4)  + Silver(6) + Bronze(6) = 27 and divide it by the count 27 / 5 = 5.4 and format it to the second decimal point. |
| Diamonds\|Silver\|Shotgun\|Gold<br />Loot Silver Medals Coal<br />Drop -1<br />Drop 1<br />Steal 6<br />Yohoho! | Coal, Diamonds, Silver, Shotgun, Gold, Medals<br />Failed treasure hunt. |   |
