# Exercise: Dictionaries
## 1.	Count Chars in a String
Write a program that counts all characters in a string except for space (" "). 
Print all the occurrences in the following format:
"{char} -> {occurrences}"
#### Examples

| Input | Output |
| ----- | ------ |
| text | t -> 2<br />e -> 1<br />x -> 1 |
| text text text | t -> 6<br />e -> 3<br />x -> 3 |

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

## 6.	Orders
Write a program that keeps the information about products and their prices. Each product has a name, a price, and a quantity:  
*	If the product doesn't exist yet, add it with its starting quantity.
*	If you receive a product, which already exists, increases its quantity by the input quantity and if its price is different, replace the price as well.
You will receive products' names, prices, and quantities on new lines. Until you receive the command "buy", keep adding items. Finally, print all items with their names and the total price of each product. 
#### Input
*	Until you receive "buy", the products will be coming in the format: "{name} {price} {quantity}".
*	The product data is always delimited by a single space.
#### Output
*	Print information about each product in the following format: 
"{product_name} -> {total_price}"  
*	Format the total price to the 2nd digit after the decimal separator.  
#### Examples

| Input | Output |
| ----- | ------ |
| Beer 2.20 100<br />IceTea 1.50 50<br />NukaCola 3.30 80<br />Water 1.00 500<br />buy | Beer -> 220.00<br />IceTea -> 75.00<br />NukaCola -> 264.00<br />Water -> 500.00 |
| Beer 2.40 350<br />Water 1.25 200<br />IceTea 5.20 100<br />Beer 1.20 200<br />IceTea 0.50 120<br />buy | Beer -> 660.00<br />Water -> 250.00<br />IceTea -> 110.00 |
| CesarSalad 10.20 25<br />SuperEnergy 0.80 400<br />Beer 1.35 350<br />IceCream 1.50 25<br />buy | CesarSalad -> 255.00<br />SuperEnergy -> 320.00<br />Beer -> 472.50<br />IceCream -> 37.50 |

## 7.	SoftUni Parking
SoftUni just got a new fancy parking lot. It even has online parking validation, except the online service doesn't work. It can only receive users' data, but it doesn't know what to do with it. Good thing you're on the dev team and know how to fix it, right?  
Write a program, which validates a parking place - users can register to enter the park and unregister to leave.  
The program receives 2 types of commands:  
*	"register {username} {license_plate_number}":
    *	The system only supports one car per user at the moment, so if a user tries to register another license plate using the same username, the system should print:
"ERROR: already registered with plate number {license_plate_number}"  
    *	If the check above passes successfully, the user should be registered, so the system should print:
 "{username} registered {license_plate_number} successfully"
*	"unregister {username}":
    *	If the user is not present in the database, the system should print:
"ERROR: user {username} not found"
    *	If the check above passes successfully, the system should print:
"{username} unregistered successfully"
After you execute all of the commands, print all the currently registered users and their license plates in the format:  
*	"{username} => {license_plate_number}"
#### Input
*	First line: n - number of commands - integer
*	Next n lines: commands in one of the two possible formats:
    *	Register: "register {username} {license_plate_number}"
    *	Unregister: "unregister {username}"
The input will always be valid, and you do not need to check it explicitly.  
#### Examples

| Input | Output |
| ----- | ------ |
| 5<br />register John CS1234JS<br />register George JAVA123S<br />register Andy AB4142CD<br />register Jesica VR1223EE<br />unregister Andy | John registered CS1234JS successfully<br />George registered JAVA123S successfully<br />Andy registered AB4142CD successfully<br />Jesica registered VR1223EE successfully<br />Andy unregistered successfully<br />John => CS1234JS<br />George => JAVA123S<br />Jesica => VR1223EE |
| 4<br />register Jony AA4132BB<br />register Jony AA4132BB<br />register Linda AA9999BB<br />unregister Jony | Jony registered AA4132BB successfully<br />ERROR: already registered with plate number AA4132BB<br />Linda registered AA9999BB successfully<br />Jony unregistered successfully<br />Linda => AA9999BB |
| 6<br />register Jacob MM1111XX<br />register Anthony AB1111XX<br />unregister Jacob<br />register Joshua DD1111XX<br />unregister Lily<br />register Samantha AA9999BB | Jacob registered MM1111XX successfully<br />Anthony registered AB1111XX successfully<br />Jacob unregistered successfully<br />Joshua registered DD1111XX successfully<br />ERROR: user Lily not found<br />Samantha registered AA9999BB successfully<br />Anthony => AB1111XX<br />Joshua => DD1111XX<br />Samantha => AA9999BB |

## 8.	Courses
Write a program that keeps the information about courses. Each course has a name and registered students.  
You will be receiving a course name and a student name until you receive the command "end".  
You should register each user into the corresponding course. If the given course does not exist, add it.  
When you receive the command "end", print the courses with their names and total registered users. For each course, print the registered users.  
#### Input
*	Until the "end" command is received, you will be receiving input lines in the format: 
"{course_name} : {student_name}"
*	The product data is always delimited by " : "
#### Output
*	Print the information about each course in the following format: 
"{course_name}: {registered_students}"
*	Print the information about each student in the following format:
"-- {student_name}"
#### Examples

| Input | Output |
| ----- | ------ |
| Programming Fundamentals : John Smith<br />Programming Fundamentals : Linda Johnson<br />JS Core : Will Wilson<br />Java Advanced : Harrison White<br />end | Programming Fundamentals: 2<br />-- John Smith<br />-- Linda Johnson<br />JS Core: 1<br />-- Will Wilson<br />Java Advanced: 1<br />-- Harrison White |
| Algorithms : Jay Moore<br />Programming Basics : Martin Taylor<br />Python Fundamentals : John Anderson<br />Python Fundamentals : Andrew Robinson<br />Algorithms : Bob Jackson<br />Python Fundamentals : Clark Lewis<br />end | Algorithms: 2<br />-- Jay Moore<br />-- Bob Jackson<br />Programming Basics: 1<br />-- Martin Taylor<br />Python Fundamentals: 3<br />-- John Anderson<br />-- Andrew Robinson<br />-- Clark Lewis |

## 9.	 Student Academy
Write a program that keeps the information about students and their grades.  
On the first line, you will receive an integer number representing the next pair of rows. On the next lines, you will be receiving each student's name and their grade. 
Keep track of all grades for each student and keep only the students with an average grade higher than or equal to 4.50.  
Print the final dictionary with students and their average grade in the following format:  
"{name} -> {averageGrade}"  
Format the average grade to the 2nd decimal place.  
#### Examples

| Input | Output | Input | Output |
| ----- | ------ | ----- | ------ |
| 5<br />John<br />5.5<br />John<br />4.5<br />Alice<br />6<br />Alice<br />3<br />George<br />5| John -> 5.00<br />Alice -> 4.50<br />George -> 5.00 | 5<br />Amanda<br />3.5<br />Amanda<br />4<br />Rob<br />5.5<br />Christian<br />5<br />Robert<br />6 | Rob -> 5.50<br />Christian -> 5.00<br />Robert -> 6.00 |

