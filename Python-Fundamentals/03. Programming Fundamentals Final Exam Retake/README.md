# Problem 1 - Secret Chat

You have plenty of free time, so you decide to write a program that conceals and reveals your received messages. Go ahead and type it in!  
On the first line of the input, you will receive the concealed message. After that, until the "Reveal" command is given, you will receive strings with instructions for different operations that need to be performed upon the concealed message to interpret it and reveal its actual content. There are several types of instructions, split by ":\|:"  
*	"InsertSpace:\|:{index}":
    *	Inserts a single space at the given index. The given index will always be valid.
*	"Reverse:\|:{substring}":
    *	If the message contains the given substring, cut it out, reverse it and add it at the end of the message. 
    *	If not, print "error".
    *	This operation should replace only the first occurrence of the given substring if there are two or more occurrences.
*	"ChangeAll:\|:{substring}:\|:{replacement}":
    *	Changes all occurrences of the given substring with the replacement text.
### Input / Constraints
*	On the first line, you will receive a string with a message.
*	On the following lines, you will be receiving commands, split by ":|:".
### Output
*	After each set of instructions, print the resulting string. 
*	After the "Reveal" command is received, print this message:
"You have a new text message: {message}"  
### Examples

| Input | Output |
| ----- | ------ |
| heVVodar!gniV<br />ChangeAll:\|:V:\|:l<br />Reverse:\|:!gnil<br />InsertSpace:\|:5<br />Reveal | hellodar!gnil<br />hellodarling!<br />hello darling!<br />You have a new text message: hello darling! |
| Hiware?uiy<br />ChangeAll:\|:i:\|:o<br />Reverse:\|:?uoy<br />Reverse:\|:jd<br />InsertSpace:\|:3<br />InsertSpace:\|:7<br />Reveal | Howare?uoy<br />Howareyou?<br />error<br />How areyou?<br />How are you?<br />You have a new text message: How are you? |

# Problem 2 - Mirror words

The SoftUni Spelling Bee competition is here. But it\`s not like any other Spelling Bee competition out there. It\`s different and a lot more fun! You, of course, are a participant, and you are eager to show the competition that you are the best, so go ahead, learn the rules and win!  
On the first line of the input, you will be given a text string. To win the competition, you have to find all hidden word pairs, read them, and mark the ones that are mirror images of each other.  
First of all, you have to extract the hidden word pairs. Hidden word pairs are:  
*	Surrounded by "@" or "#" (only one of the two) in the following pattern #wordOne##wordTwo# or @wordOne@@wordTwo@
*	At least 3 characters long each (without the surrounding symbols)
*	Made up of letters only
If the second word, spelled backward, is the same as the first word and vice versa (casing matters!), they are a match, and you have to store them somewhere. Examples of mirror words:  
#Part##traP# @leveL@@Level@ #sAw##wAs#  
*	If you don\'t find any valid pairs, print: "No word pairs found!"
*	If you find valid pairs print their count: "{valid pairs count} word pairs found!"
*	If there are no mirror words, print: "No mirror words!"
*	If there are mirror words print:
"The mirror words are:  
{wordOne} <=> {wordtwo}, {wordOne} <=> {wordtwo}, … {wordOne} <=> {wordtwo}"  
### Input / Constraints
*	You will recive a string.
### Output
*	Print the proper output messages in the proper cases as described in the problem description.
*	If there are pairs of mirror words, print them in the end, each pair separated by ", ".
*	Each pair of mirror word must be printed with " <=> " between the words.
### Examples

| Input | Output | Comments |
| ----- | ------ | ------ |
| @mix#tix3dj#poOl##loOp#wl@@bong&song%4very$long@thong#Part##traP##<br />@@leveL@@Level@##car#rac##tu@pack@@ckap@#rr#sAw##wAs#r#@w1r | 5 word pairs found!<br />The mirror words are:<br />Part <=> traP, leveL <=> Level, sAw <=> wAs | There are 5 green and yellow pairs that meet all requirements and thus are valid.<br />#poOl##loOp# is valid and looks very much like a mirror words pair, but it isn\`t because the casings don\`t match.<br />#car#rac# "rac" spelled backward is "car", but this is not a valid pair because there is only one "#" between the words.<br />@pack@@ckap@ is also valid, but "ckap" backward is "pakc" which is not the same as "pack", so they are not mirror words. |
| #po0l##l0op# @bAc##cAB@ @LM@ML@ #xxxXxx##xxxXxx# @aba@@ababa@ | 2 word pairs found!<br />No mirror words! |"xxxXxx" backward is not the same as "xxxXxx"<br />@aba@@ababa@ is a valid pair, but the word lengths are different - these are definitely not mirror words |
| #lol#lol# @#God@@doG@# #abC@@Cba# @Xyu@#uyX# | No word pairs found!<br />No mirror words! |   |

# Problem 3 - Need for Speed III

You have just bought the latest and greatest computer game – Need for Seed III. Pick your favorite cars and drive them all you want! We know that you can't wait to start playing.  
On the first line of the standard input, you will receive an integer n – the number of cars that you can obtain. On the next n lines, the cars themselves will follow with their mileage and fuel available, separated by "|" in the following format:  
"{car}\|{mileage}\|{fuel}"  
Then, you will be receiving different commands, each on a new line, separated by " : ", until the "Stop" command is given:  
*	"Drive : {car} : {distance} : {fuel}":
    *	You need to drive the given distance, and you will need the given fuel to do that. If the car doesn't have enough fuel, print: "Not enough fuel to make that ride"
    *	If the car has the required fuel available in the tank, increase its mileage with the given distance, decrease its fuel with the given fuel, and print: 
"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed."
    *	You like driving new cars only, so if a car's mileage reaches 100 000 km, remove it from the collection(s) and print: "Time to sell the {car}!"
*	"Refuel : {car} : {fuel}":
    *	Refill the tank of your car. 
    *	Each tank can hold a maximum of 75 liters of fuel, so if the given amount of fuel is more than you can fit in the tank, take only what is required to fill it up. 
    *	Print a message in the following format: "{car} refueled with {fuel} liters"
*	"Revert : {car} : {kilometers}":
    *	Decrease the mileage of the given car with the given kilometers and print the kilometers you have decreased it with in the following format:
"{car} mileage decreased by {amount reverted} kilometers"
    *	If the mileage becomes less than 10 000km after it is decreased, just set it to 10 000km and 
DO NOT print anything.  
Upon receiving the "Stop" command, you need to print all cars in your possession in the following format:  
"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt."  
### Input/Constraints
*	The mileage and fuel of the cars will be valid, 32-bit integers, and will never be negative.
*	The fuel and distance amounts in the commands will never be negative.
*	The car names in the commands will always be valid cars in your possession.
### Output
*	All the output messages with the appropriate formats are described in the problem description.
### Examples

| Input | Output | 
| ----- | ------ |
| 3<br />Audi A6\|38000\|62<br />Mercedes CLS\|11000\|35<br />Volkswagen Passat CC\|45678\|5<br />Drive : Audi A6 : 543 : 47<br />Drive : Mercedes CLS : 94 : 11<br />Drive : Volkswagen Passat CC : 69 : 8<br />Refuel : Audi A6 : 50<br />Revert : Mercedes CLS : 500<br />Revert : Audi A6 : 30000<br />Stop | Audi A6 driven for 543 kilometers. 47 liters of fuel consumed.<br />Mercedes CLS driven for 94 kilometers. 11 liters of fuel consumed.<br />Not enough fuel to make that ride<br />Audi A6 refueled with 50 liters<br />Mercedes CLS mileage decreased by 500 kilometers<br />Audi A6 -> Mileage: 10000 kms, Fuel in the tank: 65 lt.<br />Mercedes CLS -> Mileage: 10594 kms, Fuel in the tank: 24 lt.<br />Volkswagen Passat CC -> Mileage: 45678 kms, Fuel in the tank: 5 lt. | 

| Comments | 
| -------- | 
| After we receive the cars with their mileage and fuel, we start driving them. When we get to "Drive : Volkswagen Passat CC : 69 : 8" command, our program calculates that there is not enough fuel, and we print the appropriate message. Then we refuel the Audi A6 with 50 l of fuel and Revert the Mercedes with 500 kilometers.<br />When we receive the "Revert : Audi A6 : 30000", we set its mileage to 10000 km, because if the current mileage of the Audi is 38543 kms and if we subtract 30000 from it, we receive 8543 kms, which is less than 10000 kms.<br />After all the commands, we print our current collection of cars with their current mileage and current fuel. | 

| Input | Output | 
| ----- | ------ |
|  4<br />Lamborghini Veneno\|11111\|74<br />Bugatti Veyron\|12345\|67<br />Koenigsegg CCXR\|67890\|12<br />Aston Martin Valkryie\|99900\|50<br />Drive : Koenigsegg CCXR : 382 : 82<br />Drive : Aston Martin Valkryie : 99 : 23<br />Drive : Aston Martin Valkryie : 2 : 1<br />Refuel : Lamborghini Veneno : 40<br />Revert : Bugatti Veyron : 2000<br />Stop | Not enough fuel to make that ride<br />Aston Martin Valkryie driven for 99 kilometers. 23 liters of fuel consumed.<br />Aston Martin Valkryie driven for 2 kilometers. 1 liters of fuel consumed.<br />Time to sell the Aston Martin Valkryie!<br />Lamborghini Veneno refueled with 1 liters<br />Bugatti Veyron mileage decreased by 2000 kilometers<br />Lamborghini Veneno -> Mileage: 11111 kms, Fuel in the tank: 75 lt.<br />Bugatti Veyron -> Mileage: 10345 kms, Fuel in the tank: 67 lt.<br />Koenigsegg CCXR -> Mileage: 67890 kms, Fuel in the tank: 12 lt. | 
