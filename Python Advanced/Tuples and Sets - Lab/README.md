# Lab: Tuples and Sets
## 1.	Count Same Values
You will be given numbers separated by a space. Write a program that prints the number of occurrences of each number in the format "{number} - {count} times". The number must be formatted to the first decimal point.  
#### Examples

| Input | Output |
| ----- | ------ |
| -2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3 | -2.5 - 3 times<br />4.0 - 2 times<br />3.0 - 4 times<br />-5.5 - 1 times |
| 2 4 4 5 5 2 3 3 4 4 3 3 4 3 5 3 2 5 4 3 | 2.0 - 3 times<br />4.0 - 6 times<br />5.0 - 4 times<br />3.0 - 7 times |

## 2.	Students' Grades
Write a program that reads students' names and their grades and adds them to the student record.  
On the first line, you will receive the number of students – N. On the following N lines, you will be receiving a student's name and grade.  
For each student print all his/her grades and finally his/her average grade, formatted to the second decimal point in the format: "{student's name} -> {grade1} {grade2} ... {gradeN} (avg: {average_grade})".  
The order in which we print the result does not matter.  
#### Examples

| Input | Output |
| ----- | ------ |
| 7<br />Peter 5.20<br />Mark 5.50<br />Peter 3.20<br />Mark 2.50<br />Alex 2.00<br />Mark 3.46<br />Alex 3.00 | Mark -> 5.50 2.50 3.46 (avg: 3.82)<br />Peter -> 5.20 3.20 (avg: 4.20)<br />Alex -> 2.00 3.00 (avg: 2.50) |
| 4<br />Scott 4.50<br />Ted 3.00<br />Scott 5.00<br />Ted 3.66 | Ted -> 3.00 3.66 (avg: 3.33)<br />Scott -> 4.50 5.00 (avg: 4.75) |
| 5<br />Lee 6.00<br />Lee 5.50<br />Lee 6.00<br />Peter 4.40<br />Kenny 3.30 | Peter -> 4.40 (avg: 4.40)<br />Lee -> 6.00 5.50 6.00 (avg: 5.83)<br />Kenny -> 3.30 (avg: 3.30) |

## 3.	Record Unique Names
Write a program, which will take a list of names and print only the unique names in the list.  
The order in which we print the result does not matter.  
#### Examples

| Input | Output |
| ----- | ------ |
| 8<br />Lee<br />Joey<br />Lee<br />Joe<br />Alan<br />Alan<br />Peter<br />Joey | Alan<br />Joey<br />Lee<br />Joe<br />Peter |

## 4.	Parking Lot
Write a program that:  
* Records a car number for every car that enters the parking lot
*	Removes a car number when the car leaves the parking lot
On the first line, you will receive the number of commands - N. On the following N lines, you will receive the direction and car's number in the format: "{direction}, {car_number}". The direction could only be "IN" or "OUT". Print the car numbers which are still in the parking lot. Keep in mind that all car numbers must be unique.   If the parking lot is empty, print "Parking Lot is Empty".  
Note: The order in which we print the result does not matter.  
#### Examples

| Input | Output |
| ----- | ------ |
| 10<br />IN, CA2844AA<br />IN, CA1234TA<br />OUT, CA2844AA<br />IN, CA9999TT<br />IN, CA2866HI<br />OUT, CA1234TA<br />IN, CA2844AA<br />OUT, CA2866HI<br />IN, CA9876HH<br />IN, CA2822UU | CA2844AA<br />CA9999TT<br />CA2822UU<br />CA9876HH |
| 4<br />IN, CA2844AA<br />IN, CA1234TA<br />OUT, CA2844AA<br />OUT, CA1234TA | Parking Lot is Empty |

## 5.	SoftUni Party
There is a party at SoftUni. Many guests are invited, and there are two types of them: Regular and VIP. When a guest comes, check if they exist on any of the two reservation lists.  
On the first line, you will receive the number of guests – N. On the following N lines, you will be receiving their reservation codes. All reservation codes are 8 characters long, and all VIP numbers will start with a digit. Keep in mind that all reservation numbers must be unique.  
After that, you will be receiving guests who came to the party until you read the "END" command.  
In the end, print the number of guests who did not come to the party and their reservation numbers:  
*	The VIP guests must be first.
*	Both the VIP and the Regular guests must be sorted in ascending order.
#### Examples  

| Input | Output | Input | Output |
| ----- | ------ | ----- | ------ |
| 5<br />7IK9Yo0h<br />9NoBUajQ<br />Ce8vwPmE<br />SVQXQCbc<br />tSzE5t0p<br />9NoBUajQ<br />Ce8vwPmE<br />SVQXQCbc<br />END | 2<br />7IK9Yo0h<br />tSzE5t0p | 6<br /> m8rfQBvl<br />fc1oZCE0<br />UgffRkOn<br />7ugX7bm0<br />9CQBGUeJ<br />2FQZT3uC<br />2FQZT3uC<br />9CQBGUeJ<br />fc1oZCE0<br />END | 3<br />7ugX7bm0<br />UgffRkOn<br />m8rfQBvl |
