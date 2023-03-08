# Problem 1 - The Imitation Game

During World War 2, you are a mathematician who has joined the cryptography team to decipher the enemy's enigma code. Your job is to create a program to crack the codes. 
On the first line of the input, you will receive the encrypted message. After that, until the "Decode" command is given, you will be receiving strings with instructions for different operations that need to be performed upon the concealed message to interpret it and reveal its true content. There are several types of instructions, split by '|'
*	"Move {number of letters}":
    *	Moves the first n letters to the back of the string
*	"Insert {index} {value}":
    *	Inserts the given value before the given index in the string
*	"ChangeAll {substring} {replacement}":
    *	Changes all occurrences of the given substring with the replacement text
### Input / Constraints
*	On the first line, you will receive a string with a message.
*	On the following lines, you will be receiving commands, split by '\|' .
### Output
*	After the "Decode" command is received, print this message:  
"The decrypted message is: {message}"  
### Examples

| Input | Output |
| ----- | ------ |
| zzHe<br />ChangeAll\|z\|l<br />Insert\|2\|o<br />Move\|3<br />Decode | The decrypted message is: Hello |
| owyouh<br />Move\|2<br />Move\|3<br />Insert\|3\|are<br />Insert\|9\|?<br />Decode | The decrypted message is: howareyou? |

# Problem 2 - Ad Astra 

You are an astronaut who just embarked on a mission across the solar system. Since you will be in space for a long time, you have packed a lot of food with you. Create a program, which helps you identify how much food you have left and gives you information about its expiration date.  
On the first line of the input, you will be given a text string. You must extract the information about the food and calculate the total calories.  
First, you must extract the food info. It will always follow the same pattern rules:  
*	It will be surrounded by "|" or "#" (only one of the two) in the following pattern: 
#{item name}#{expiration date}#{calories}#   or   
|{item name}|{expiration date}|{calories}|  
*	The item name will contain only lowercase and uppercase letters and whitespace  
*	The expiration date will always follow the pattern: "{day}/{month}/{year}", where the day, month, and year will be exactly two digits long  
*	The calories will be an integer between 0-10000  
Calculate the total calories of all food items and then determine how many days you can last with the food you have. Keep in mind that you need 2000kcal a day.  
### Input / Constraints
*	You will receive a single string  
### Output
*	First, print the number of days you will be able to last with the food you have:  
"You have food to last you for: {days} days!"  
*	The output for each food item should look like this:
"Item: {item name}, Best before: {expiration date}, Nutrition: {calories}"
### Examples

| Input | Output | Coments |
| ----- | ------ | ------ |
| #Bread#19/03/21#4000#\|Invalid\|03/03.20\|\|Apples\|08/10/20\|200\|\|Carrots\|06/08/20\|500\|\|Not right\|6.8.20\|5\| | You have food to last you for: 2 days!<br />Item: Bread, Best before: 19/03/21, Nutrition: 4000<br />Item: Apples, Best before: 08/10/20, Nutrition: 200<br />Item: Carrots, Best before: 06/08/20, Nutrition: 500<br /> | We have a total of three matches – bread, apples, and carrots.<br />The sum of their calories is 4700. Since you need 2000kcal a day, we divide 4700/2000, which means this food will last you for 2 days.<br />We print each item | We have a total of three matches – bread, apples, and carrots. <br />The sum of their calories is 4700. Since you need 2000kcal a day, we divide 4700/2000, which means this food will last you for 2 days.<br />We print each item |
| $$#@@%^&#Fish#24/12/20#8500#\|#Incorrect#19.03.20#450\|$5*(@!#Ice Cream#03/10/21#9000#^#@aswe\|Milk\|05/09/20\|2000\| | You have food to last you for: 9 days!<br />Item: Fish, Best before: 24/12/20, Nutrition: 8500<br />Item: Ice Cream, Best before: 03/10/21, Nutrition: 9000<br />Item: Milk, Best before: 05/09/20, Nutrition: 2000 | We have three matches. The total calories are 8500 + 9000 + 2000 = 19500, which means you have food for a total of 9 days. |

