# More Exercise: Dictionaries
## 1.	Ranking
Here comes the final and the most interesting part – the Final ranking of the candidate-interns. The final ranking is determined by the points of the interview tasks and by the points from the exams in SoftUni. Here is your final task. You will receive some lines of input in the format "{contest}:{password for contest}" until you receive "end of contests". Save that data because you will need it later. After that you will receive other type of inputs in format "{contest}=>{password}=>{username}=>{points}" until you receive "end of submissions". Here is what you need to do.
•	Check if the contest is valid (It is considered valid if you received it in the first type of input)
•	Check if the password is correct for the given contest
•	If the contest and the password is valid, save the user with the contest they take part in (a user can take part in many contests) and the points the user has in the given contest. If you receive the same contest and the same user update the points only if the new ones are more than the older ones.
In the end, you should print the info for the user with the most points (total points for all contents they participated in) in the format "Best candidate is {user} with total {total_points} points.". After that print all students ordered by their names. For each user print each contest with the points in descending order. See the examples.
Input
•	Strings in format "{contest}:{password for contest}" until the "end of contests" command. There will be no case with two equal contests
•	Strings in format "{contest}=>{password}=>{username}=>{points}" until the "end of submissions" command.
•	There will be no case with 2 or more users with same total points!
Output
•	On the first line, print the best user in format "Best candidate is {user} with total {total points} points.".
•	Then print all students ordered as mentioned above in format:
"{user_name1}
\#  {contest1} -> {points}
\#  {contest2} -> {points} 
…
\#  {contestN} -> {points}"
Constraints
•	The strings may contain any ASCII character except from (:, =, >).
•	The numbers will be in range [0 - 10000].
•	Second input is always valid.
#### Examples

| Input | Output |
| ----- | ------ |
| Part One Interview:success<br />JS Fundamentals:fundExam<br />C# Fundamentals:fundPass<br />Algorithms:fun<br />end of contests<br />C# Fundamentals=>fundPass=>Tanya=>350<br />Algorithms=>fun=>Tanya=>380<br />Part One Interview=>success=>Nikola=>120<br />Java Basics Exam=>wrong_pass=>Teo=>400<br />Part One Interview=>success=>Tanya=>220<br />OOP Advanced=>password123=>Kay=>231<br />C# Fundamentals=>fundPass=>Tanya=>250<br />C# <br />undamentals=>fundPass=>Nikola=>200<br />JS Fundamentals=>fundExam=>Tanya=>400<br />end of submissions | Best candidate is Tanya with total 1350 points.<br />Ranking:<br />Nikola<br />#  C# Fundamentals -> 200<br />#  Part One Interview -> <br />120<br />Tanya<br />#  JS Fundamentals -> 400<br />#  Algorithms -> 380<br />#  C# Fundamentals -> 350<br />#  Part One Interview -> 220 |
| Java Advanced:funpass
Part Two Interview:success
Math Concept:asdasd
Java Web Basics:forrF
end of contests
Math Concept=>ispass=>Monika=>290
Java Advanced=>funpass=>Simona=>400
Part Two Interview=>success=>Drago=>120
Java Advanced=>funpass=>Petyr=>90
Java Web Basics=>forrF=>Simona=>280
Part Two Interview=>success=>Petyr=>0
Math Concept=>asdasd=>Drago=>250
Part Two Interview=>success=>Simona=>200
end of submissions
 | Best candidate is Simona with total 880 points.
Ranking:
Drago
#  Math Concept -> 250
#  Part Two Interview -> 120
Petyr
#  Java Advanced -> 90
#  Part Two Interview -> 0
Simona
#  Java Advanced -> 400
#  Java Web Basics -> 280
#  Part Two Interview -> 200
|

## 2.	A Miner Task
You will be given a sequence of strings, each on a new line until you receive the "stop" command. Every odd line on the console represents a resource (e.g., Gold, Silver, Copper, and so on) and every even - quantity. Your task is to collect the resources and print them each on a new line.  
Print the resources and their quantities in the following format:  
"{resource} -> {quantity}"  
The quantities will be in the range \[1 … 2 000 000 000\].
#### Examples

| Input | Output | Input | Output |
| ----- | ------ | ----- | ------ |
| Gold<br />155<br />Silver<br />10<br />Copper<br />17<br />stop | Gold -> 155<br />Silver -> 10<br />Copper -> 17<br /> | gold<br />155<br />silver<br />10<br />copper<br />17<br />gold<br />15<br />stop | gold -> 170<br />silver -> 10<br />copper -> 17<br /> |

## 3.	Capitals
Using a dictionary comprehension, write a program that receives country names on the first line, separated by comma and space ", ", and their corresponding capital cities on the second line (again separated by comma and space ", "). Print each country with their capital on a separate line in the following format: "{country} -> {capital}".
#### Hints
*	You could use the zip() method.  
#### Examples

| Input | Output |
| ----- | ------ |
| Bulgaria, Romania, Germany, England<br />Sofia, Bucharest, Berlin, London | Bulgaria -> Sofia<br />Romania -> Bucharest<br />Germany -> Berlin<br />England -> London |
| Bulgaria, Germany, France<br />Varna, Frankfurt, Paris | Bulgaria -> Varna<br />Germany -> Frankfurt<br />France -> Paris |

## 4.	Phonebook
Write a program that receives info from the console about people and their phone numbers.  
Each entry should have a name and a number (both strings) separated by a "-". If you receive a name that already exists in the phonebook, update its number.  
After filling the phonebook, you will receive a number – N. Your program should be able to perform a search of contact by name and print its details in the format: "{name} -> {number}". In case the contact isn't found, print: "Contact {name} does not exist."  
#### Examples

| Input | Output |
| ----- | ------ |
| Adam-0888080808<br />2<br />Mery<br />Adam | Contact Mery does not exist.<br />Adam -> 0888080808 |
| Adam-+359888001122<br />Ralf-666<br />George-5559393<br />Silvester-02/987665544<br />4<br />Silvester<br />silvester<br />Rolf<br />Ralf | Silvester -> 02/987665544<br />Contact silvester does not exist.<br />Contact Rolf does not exist.<br />Ralf -> 666 |

## 5.	Legendary Farming
You are playing a game, and your goal is to win a legendary item - any legendary item will be good enough. However, it's a tedious process, and it requires quite a bit of farming. The possible items are:  
*	"Shadowmourne" - requires 250 Shards  
*	"Valanyr" - requires 250 Fragments  
*	"Dragonwrath" - requires 250 Motes  
"Shards", "Fragments", and "Motes" are the key materials 	(case-insensitive), and everything else is junk.  
You will be given lines of input in the format:  
"{quantity1} {material1} {quantity2} {material2} … {quantityN} {materialN}"  
Keep track of the key materials - the first one that reaches 250, wins the race. At that point, you have to print that the corresponding legendary item is obtained.  
In the end, print the remaining shards, fragments, motes in the format:  
"shards: {number_of_shards}  
fragments: {number_of_fragments}  
motes: {number_of_motes}"  
Finally, print the collected junk items in the order of appearance.  
#### Input
*	Each line comes in the following format: "{quantity1} {material1} {quantity2} {material2} … {quantityN} {materialN}"
#### Output
*	On the first line, print the obtained item in the format: "{Legendary item} obtained!"  
*	On the next three lines, print the remaining key materials  
*	On the several final lines, print the junk items  
*	All materials should be printed in the format: "{material}: {quantity}"  
*	The output should be lowercase, except for the first letter of the legendary  
#### Examples

| Input | Output |
| ----- | ------ |
| 3 Motes 5 stones 5 Shards<br />6 leathers 255 fragments 7 Shards | Valanyr obtained!<br />shards: 5<br />fragments: 5<br />motes: 3<br />stones: 5<br />leathers: 6 |
| 123 silver 6 shards 8 shards 5 motes<br />9 fangs 75 motes 103 MOTES 8 Shards<br />86 Motes 7 stones 19 silver | Dragonwrath obtained!<br />shards: 22<br />fragments: 0<br />motes: 19<br />silver: 123<br />fangs: 9 |

