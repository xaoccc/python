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
