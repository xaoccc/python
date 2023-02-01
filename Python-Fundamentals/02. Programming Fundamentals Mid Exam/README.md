# Problem 1 - SoftUni Reception
Every day, thousands of students pass by the reception at SoftUni with different questions to ask. The employees have to help everyone by providing all the information and answering all of the questions.  
Three employees are working on the reception all day. Each of them can handle a different number of students per hour. Your task is to calculate how much time it will take to answer all the questions of a given number of students.  
First, you will receive 3 lines with integers, representing the number of students that each employee can help per hour. On the following line, you will receive students count as a single integer.  
Every fourth hour, all employees have a break, so they don't work for an hour. It is the only break for the employees, because they don't need rest, nor have a personal life. Calculate the time needed to answer all the student's questions and print it in the following format: "Time needed: {time}h."  
### Input / Constraints
*	On the first three lines -  each employee efficiency -  integer in the range [1 - 100]
*	On the fourth line - students count – integer in the range [0 – 10000]
*	Input will always be valid and in the range specified
### Output
*	Print a single line: "Time needed: {time}h."
*	Allowed working time / memory: 100ms / 16MB
### Examples

| Input | Output | Comment |
| ----- | ------ | ------ |
| 5<br />6<br />4<br />20 | Time needed: 2h | All employees can answer 15 students per hour. After the first hour, there are 5 students left to be answered.<br />All students will be answered in the second hour. |
| 1<br />2<br />3<br />45 | Time needed: 10h | All employees can answer 6 students per hour. In the first 3 hours, they have answered 6 * 3 = 18 students. Then they have a break for an hour.<br />After the next 3 hours, there are 18 + 6 * 3 = 36 answered students.<br />After the break for an hour, there are only 9 students to answer.<br />So in the 10th hour, all of the student's questions would be answered. |
| 3<br />2<br />5<br />40 | Time needed: 5h |  |

# Problem 2 - Array Modifier
You are given an array with integers. Write a program to modify the elements after receiving the following commands:  
*	"swap {index1} {index2}" takes two elements and swap their places.
*	"multiply {index1} {index2}" takes element at the 1st index and multiply it with the element at 2nd index. Save the product at the 1st index.
*	"decrease" decreases all elements in the array with 1.
### Input
On the first input line, you will be given the initial array values separated by a single space.  
On the next lines you will receive commands until you receive the command "end". The commands are as follow:  
*	"swap {index1} {index2}"
*	"multiply {index1} {index2}"
*	"decrease"
### Output
The output should be printed on the console and consist of elements of the modified array – separated by a comma and a single space ", ".  
### Constraints
*	Elements of the array will be integer numbers in the range [-231...231]
*	Count of the array elements will be in the range [2...100]
*	Indexes will be always in the range of the array
### Examples

| Input | Output | Comment |
| ----- | ------ | ------ |
| 23 -2 321 87 42 90 -123<br />swap 1 3<br />swap 3 6<br />swap 1 0<br />multiply 1 2<br />multiply 2 1<br />decrease<br />end | 86, 7382, 2369942, -124, 41, 89, -3 | 23 -2 321 87 42 90 -123 – initial values<br />swap 1(-2) and 3(87) ▼<br />23 87 321 -2 42 90 -123<br />swap 3(-2) and 6(-123) ▼<br />23 87 321 -123 42 90 -2<br />swap 1(87) and 0(23) ▼<br />87 23 321 -123 42 90 -2<br />multiply 1(23) 2(321) = 7383 ▼<br />87 7383 321 -123 42 290 -2<br />multiply 2(321) 1(7383) = 2369943 ▼<br />87 7383 2369943 -123 42 90 -2<br />decrease – all - 1 ▼<br />86 7382 2369942 -124 41 89 -3 |
| 1 2 3 4<br />swap 0 1<br />swap 1 2<br />swap 2 3<br />multiply 1 2<br />decrease<br />end | 1, 11, 3, 0 |  |
