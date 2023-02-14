# Problem 1. Date estimation
### Input / Constraints  
Today is your exam. It’s 26th of August 2018. you will be given a single date in format year-month-day. You should estimate if the date has passed regarding to the date mention above (2018-08-26), if it is not or if it is today. If it is not you should print how many days are left till that date. Note that the current day stills count!  
Date Format:   
yyyy-mm-dd   
### Output  
The output should be printed on the console.  
If the date has passed you should print the following output:  
*	"Passed"  
If the day is today:  
"Today date"  
If the date is future:  
*	"{number of days} days"  
### Examples

| Input | Output | Comment |
| ----- | ------ | -------|
| 2018-08-20 | Passed | Because 20 august is before 26 august we print that the day is Passed |
| 2021-08-26 | 1097 days left | We estimate that the 26th of august 2021 is after 1096 and beacause 26 stills count we add 1 => 1097 |

# Problem 2. Lists
### Input / Constraints
You will be given a single lines of elements(integers), separated with one or more spaces. You should check if all elements in the line are unique. If they are you should increase the value of every even element with the number of 2 and print the list on single row in ascending order separated by ",".  
If they are not unique you should increase every odd element with the number of 3 and print them on single row, separated with ":"  
On the next line you should print sum of the all elements divided by the count of the elements in the list. You should do that until you receive the command "stop playing"  
### Output
If the elements are unique  
Unique list: {elements in the list, separated by “,”}  
### Output: {sum of all elements divided by the length of the list}  
Else  
Non-unique list: {elements in the list, separated by “:”}  
Output: {sum of all elements divided by the length of the list}  
### Examples

| Input | Output | Comment |
| ----- | ------ | -------|
| 1 2  3   4 5 6<br />1 1 2   2 1 4 7 7 8 8 <br /> 5 5 5 5  <br />stop playing | Unique list: 1,3,4,5,6,8<br /> Output: 4.50<br /> Non-unique list:<br /> 2:2:4:4:4:4:8:8:10:10<br /> Output: 5.60<br /> Non-unique list: 8:8:8:8<br /> Output: 8.00 | First is unique so we add to every even elemnt 2. \the list looks like this: 1, 4, 3, 6,5,8  After that we order them by ascending and the same list looks like this: 1,3,4,5,6,8 Output = 1+3+4+5+6+8 = 27/6 = 4.50  <br /> The elements in the list are not unique, so we add to every odd element. The list looks like this: 3:3:2:2:3:1:10:10:8:8.We order them by ascending and it becomes: 2:2:4:4:4:4:8:8:10:10 Output 56/10 = 5.60  <br />  The elements are not unique so we add to every odd eleme:nt 3 and becomes like this: 8:8:8:8 Output: 32/4 = 8 |
| 1      1 1<br />stop playing | Non-unique list: 4:4:4<br />Output: 4.00 | |

# Problem 3. Descriptions
### Input / Constraints
You will receive descriptions of people. For each in a single row. Your role will be to decide if the description contains valid information or not, If contains you should store the data in the database.  
When you receive the command "make migrations" you should print all info you have stored.  
A valid person's information in a description will contain the following:  
* a string "name is" after which a single space and a name (first name and last name), separated by single space. Both names should start with capital letter.
* single space before and after that two digits representing the person's age after which we have single space and the word "years". A valid age is between >9 and age<100
* birthday date - before the date we should have the word "on" after that single space and then date in exact format dd-mm-yyyy (months will be digits and the date should be separated with "-" {dd-mm-yyyy})  
* Every description should end with '.'(dot) after the date of birth.  
If one of this requirements is not valid DO NOT include any of the information for the person in the database.
### Output
After the command "make migrations" you should print the info in the following format:  
“Name of the person: {person's name}.”  
“Age of the person: {age of the person}.”  
“Birthdate of the person: {Birthdate of the person}.”  
If date base is empty print:  
"DB is empty"  
Hello,everyone my name is Maria Mariova. I am 22 years old. was born on 22-06-1994.  
### Examples

| Input | Output | Comment |
| ----- | ------ | -------|
| Hello,everyone my name is Maria Mariova. I am 22 years old. was born on 22-06-1994.<br />Hello,everyone my name is Yan Familiov. I am 10 years old. was born on 22-06-2008.<br />make migrations | Name of the person: Maria Mariova.<br />Age of the person: 22.<br />Birthdate of the person: 22-06-1994.<br />Name of the person: Yan Familiov.<br />Age of the person: 10.<br />Birthdate of the person: 22-06-2008. | Because the first example is valid we add the person information to our data base.<br />The second example is also valid so we add the info to the data base |
| Hello,everyone my name is Py Thon. I am 18 years old. was born on 16-10-2000.<br />Hello,everyone my name is Ja Va. I am 20 years old. was born on kogato si iskam.<br />make migrations  | Name of the person: Py Thon.<br />Age of the person: 18.<br />Birthdate of the person: 16-10-2000. | First row is valid so we add it to the datebase<br />Second example is not valid, because the birthday is not in the requested format. |

# Problem 4. Books
### Input / Constraints
You are asked to write a program for a bookstore. Your task is to create a software, which tells the sellers if there is a requested book in stock or not. If there is you should sell it and at the end of the workday the software should list all sold books and the sum of their prices.  
A valid book has:  
* Title -> string
* Author -> string
* Chapters -> list of strings
* Price -> with positive floating point number or integer
First you start receiving strings of books – the bookstore's stock, which you should store the book if it's valid until you receive the command 'on work'.  
Then you will start receiving requests for books. If the bookstore has that book in stock, you should list it as a sold book, if there is no such book you should print -> "No such book here"  
When you receive the command 'end work' you should print all sold books and after that the amount of money.  
A valid book will always be in format: 
"{title} {author} {price} -> {chapter1}, {chapter2}, {chapter3} ..."
A requests for a book always will be in format: "{title}"
### Output  
The output should be printed on the console.  
For every sold book you should print the information in the following format:  
* "SOLD: {title of the sold book} with author {author of the sold book}. Chapters in the book {the sum of the chapters of the sold book}"  
At the end of the program you should print the sum formatted to second digit after decimal:  
* "Money: {sum of all sold books prices}"  
If there aren't any sold books print 
* "Bad day :("
### Constraints:
No books with same name and different authors will come as input  
### Examples

| Input | Output | Comment |
| ----- | ------ | ------- |
| richDadPoorDad RobertKiyosaki 7.00 -> beRich, thinkDifferent, eDucateYourself, startThinking<br />richWoman kimKiyosaki 12.00 -> launchWithMyGirls, myStory, goAndDoon work<br />richDadPoor<br />richDadPoorDad<br />richWomen<br />richWoman<br />end work | No such book here<br />No such book here<br />SOLD: richDadPoorDad with author RobertKiyosaki. Chapters in the book 4<br />SOLD: richWoman with author kimKiyosaki. Chapters in the book 3<br />Money: 19.00 | First book is valid, so we add it to the store.<br />Second book is also valid, so we add it to the store<br /> richDadPoor is not  in the store, so  we print “no such book here”<br />richDadPoorDad (7.00) is in the store and we sell it<br />richWomen is not  in the store, so  we print “no such book here”<br />richWoman (12.00) is in the store and we sell it<br />The amount is 12+7 = 19|
| killAmockingBird  20.50 -> chapter1<br />on work<br />richDadPoor<br />killAmockingBird<br />killAmockingBird<br />richWomen<br />end work | No such book here<br />No such book here<br />No such book here<br />No such book here<br />Bad day :( |  |
| littlePrinceDataResume AntoineDeSaintExupery 7.20 -> Plot, ToneAndWritingStyle, Background, HonoursAndLegacy<br />EatThatFrog BrianTracy 15.05 -> ApplyThePowerOfClearlyWrittenGoals, PlanEveryDayInAdvance<br />on work<br />littlePrinceDataResume<br />littlePrinceDataResume<br />littlePrinceDataResume<br />EatThatFrog<br />Top10Pockemons<br />end work | No such book here<br />SOLD: littlePrinceDataResume with author AntoineDeSaintExupery. Chapters in the book 4<br />SOLD: littlePrinceDataResume with author AntoineDeSaintExupery. Chapters in the book 4<br />SOLD: littlePrinceDataResume with author AntoineDeSaintExupery. Chapters in the book 4<br />SOLD: EatThatFrog with author BrianTracy. Chapters in the book 2<br />Money: 36.65 |  |
