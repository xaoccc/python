# Lab: Classes and Objects

## 1.	Comment
Create a class with the name "Comment". The __init__ method should accept 3 parameters:
*	username
*	content
*	likes (optional, 0 by default)
Use the exact names for your variables  
Note: there is no input/output for this problem. Test the class yourself and submit only the class  
#### Example

| Test Code | Output |
| --------- | ------ |
| comment = Comment("user1", "I like this book")<br />print(comment.username)<br />print(comment.content)<br />print(comment.likes) | user1<br />I like this book<br />0 |

## 2.	Party
Create a class Party that only has an attribute people – empty list. The __init__ method should not accept any parameters. You will be given names of people (on separate lines) until you receive the command "End". Use the created class to solve this problem. After you receive the "End" command, print 2 lines:  
*	"Going: {people}" - the people should be separated by comma and space ", ".
*	"Total: {total_people_going}"
Note: submit all of your code, including the class
#### Example

| Input | Output |
| --------- | ------ |
| Peter<br />John<br />Katy<br />End | Going: Peter, John, Katy<br />Total: 3 |
| Sam<br />Eddy<br />Edd<br />Kris<br />End | Going: Sam, Eddy, Edd, Kris<br />Total: 4 |

## 3.	Email
Create class Email. The __init__ method should receive sender, receiver and a content. It should also have a default set to False attribute called is_sent. The class should have two additional methods:    
*	send() - sets the is_sent attribute to True
*	get_info() - returns the following string: "{sender} says to {receiver}: {content}. Sent: {is_sent}"  
You will receive some information (separated by a single space) until you receive the command "Stop". The first element will be the sender, the second one – the receiver, and the third one – the content. On the final line, you will be given the indices of the sent emails separated by comma and space ", ".     
Call the send() method for the given indices of emails. For each email, call the get_info() method.  
Note: submit all of your code, including the class  
#### Example

| Input | Output |
| --------- | ------ |
| Peter John Hi,John<br />John Peter Hi,Peter!<br />Katy Lilly Hello,Lilly<br />Stop<br />0, 2 | Peter says to John: Hi,John. Sent: True<br />John says to Peter: Hi,Peter!. Sent: False<br />Katy says to Lilly: Hello,Lilly. Sent: True |
| Anna, Bella, Hi<br />Sam, Dany, Okey<br />Felix, Mery, Bye<br />Stop<br />0 | Anna, says to Bella,: Hi. Sent: True<br />Sam, says to Dany,: Okey. Sent: False<br />Felix, says to Mery,: Bye. Sent: False |

## 4.	Zoo
Create a class Zoo. It should have a class attribute called __animals that stores the total count of the animals in the zoo. The __init__ method should only receive the name of the zoo. There you should also create 3 empty lists (mammals, fishes, birds). The class should also have 2 more methods:  
*	add_animal(species, name) - based on the species, adds the name to the corresponding list  
*	get_info(species) - based on the species returns a string in the following format:  
"{Species} in {zoo_name}: {names}  
Total animals: {total_animals}"   
On the first line, you will receive the name of the zoo. On the second line, you will receive number n. On the following n lines you will receive animal info in the format: "{species} {name}". Add the animal to the zoo to the corresponding list. The species could be "mammal", "fish", or "bird".  
On the final line, you will receive a species.   
At the end, print the info for that species and the total count of animals in the zoo. 

#### Example
| Input | Output |
| --------- | ------ |
| Great Zoo<br />5<br />mammal lion<br />mammal bear<br />fish salmon<br />bird owl<br />mammal tiger<br />mammal | Mammals in Great Zoo: lion, bear, tiger<br />Total animals: 5 |
| Blah<br />1<br />mammal bear<br />mammal | Mammals in Blah: bear<br />Total animals: 1 |

## 5.	Circle
Create a class Circle. In the __init__ method, the circle should only receive one parameter - its diameter. Create a class attribute called __pi that is equal to 3.14. The class should also have the following methods:  
*	calculate_circumference() - returns the circumference of the circle  
*	calculate_area() - returns the area of the circle  
*	calculate_area_of_sector(angle) - gives the central angle in degrees, returns the area that fills the sector  
Notes: Search the formulas on the internet. Name your methods and variables exactly as in the description! Submit only the class. Test your class before submitting it!  
#### Example 

| Test code | Output |
| --------- | ------ |
| circle = Circle(10)<br />angle = 5<br />print(f"{circle.calculate_circumference():.2f}")<br />print(f"{circle.calculate_area():.2f}")<br />print(f"{circle.calculate_area_of_sector(angle):.2f}") | 31.40<br />78.50<br />1.09 |


![image](https://user-images.githubusercontent.com/114498517/217537840-e3a87856-969b-438e-98de-6ab37396dea7.png)
