# Problem 1. Sino The Walker
Sino is one of those people that lives in SoftUni. He leaves every now and then, but when he leaves he always takes a different route, so he needs to know how much time it will take for him to go home. Your job is to help him with the calculations.  
You will receive the time that Sino leaves SoftUni, the steps taken and time for each step in seconds.  
You need to print the exact time that he will arrive at home in the format specified.  
### Input / Constrains
*	The first line will be the time Sino leaves SoftUni in the following format: HH:mm:ss  
*	The second line will contain the number of steps that he needs to walk to his home. This number will be an integer in range [0…2,147,483,647]  
*	On the final line you will receive the time in seconds for each step. This number will be an integer in range [0…2,147,483,647]  
### Output
*	Print the time of arrival at home in the following format:  
    *	Time Arrival: {hours}:{minutes}:{seconds}  
*	If hours, minutes or seconds are a single digit number, add a zero in front.  
*	If, for example, hours are equal to zero, print a 00 in their place. The same is true for minutes or seconds.  
*	Time of day starts at 00:00:00 and ends at 23:59:59 
### Examples

| Input | Output |
| ----- | ------ |
| 12:30:30<br />90<br />1 | Time Arrival: 12:32:00 |
| 23:49:13<br />5424<br />2 | Time Arrival: 02:50:01 |

# Problem 2. SoftUni Karaoke
SoftUni cultivates talent whether it's coding talent or something else and in this case, something else is singing. Since you love music you want to take part in the event but as a programmer you simply lack the "something else" so your job is to make the software to track participants' awards.  
On the first line, you will receive a list with all participants that applied for performance.  
On the second line, you will receive the list with all available songs.   
On the next lines, until the "dawn" command, you will get the names of people, the song that they are performing on stage and the award they get from the audience.
However, not every time the plan goes according to schedule. In other words, everyone (listed or not) can go on stage and perform a song that is not even available and he still gets awards from the audience. However, you should record only the awards for listed participants that perform songs available in the list. In case someone is not listed or sings a song that is not available you should not record neither the participant, nor his award.   
When the "dawn" comes, you need to print all participants, the count of the unique awards they received and all unique awards. Participants should be sorted by number of awards in descending order and then by participant name alphabetically. Awards should be sorted in alphabetical order.  
### Input
*	On the first line, you will receive list with all participants that applied for performance in the format: "{participant}, {participant} … {participant}"
*	On the second line, you will get all available songs in the in the format: "{song}, {song} … {song}"
*	On the next lines, until the "dawn" command you will receive every stage performance in the format: "{participant}, {song}, {award}" 
*	Performances and songs will be separated by a comma and a single or multiple white spaces
### Output
*	Print all participants along with the number of unique awards they won in the format: 
    *	"{participant}: {award count} awards"
    *	"--{award}"
*	Print participants sorted by unique awards count in descending order. If two participants have the same unique award count, sort them alphabetically by name
*	Print unique awards for every participant sorted alphabetically
*	If there are no awards, print "No awards"
### Constrains
•	The number of total participants will be in range [1 … 100]
•	The number of total songs will be in range [1 … 100]
•	The input will always end with the "dawn" command
 
### Examples

| Input | Output |
| ----- | ------ |
| Trifon, Vankata, Gesha<br />Dragana - Kukavice, Bon Jovi - It's my life, Lorde - Royals<br />Gesha, Bon Jovi - It's my life, Best Rock<br />Vankata, Dragana - Kukavice, Best Srabsko<br />Vankata, Dragana - Kukavice, Best Srabsko<br />Vankata, Dragana - Kukavice, Stiga Tolko Srabsko<br />Vankata, PHP Web, Educational 101<br />dawn | Vankata: 2 awards<br />--Best Srabsko<br />--Stiga Tolko Srabsko<br />Gesha: 1 awards<br />--Best Rock<br /> |
| Gesha<br />Bon Jovi - It's my life<br />Gesha, Bon Jovi - It's my life, Best Rock<br />Vankata, Dragana - Kukavice, Best Srabsko<br />Vankata, Dragana - Kukavice, Stiga Tolko Srabsko<br />Vankata, PHP Web, Educational 101<br />dawn | Gesha: 1 awards<br />--Best Rock |
| Sino<br />Vasko Naidenov - Nova Godina<br />dawn | No awards |
