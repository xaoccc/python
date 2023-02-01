# Lab: Lists Basics

## 1. Strange Zoo
You are at the zoo, and the meerkats look strange. 
You will receive 3 strings on separate lines, representing the tail, the body, and the head of an animal in that order. Your task is to re-arrange the elements in a list so that the animal looks normal again:
*	On the first position is the head;
*	On the second position is the body;
*	On the last one is the tail.
#### Example

| Input | Output |
| ----- | ------ |
| my tail<br />my body seems on place<br />my head is on the wrong end! | ['my head is on the wrong end!', 'my body seems on place', 'my tail'] |
| tail<br />body<br />head | ['head', 'body', 'tail'] |
| T<br />B<br />H | ['H', 'B', 'T'] |

## 2. Courses
On the first line, you will receive a single number n. On the following n lines, you will receive names of courses. You should create a list of courses and print it.  
#### Example

| Input | Output |
| ----- | ------ |
| 2<br />PB Python<br />PF Python | ['PB Python', 'PF Python'] |
| 4<br />Front-End<br />C# Web<br />JS Core<br />Programming Fundamentals | ['Front-End', 'C# Web', 'JS Core', 'Programming Fundamentals'] |

## 3.	List Statistics
On the first line, you will receive a number n. On the following n lines, you will receive integers. You should create and print two lists:  
*	One with all the positives (including 0) numbers
*	One with all the negatives numbers
Finally, print the following message:  
"Count of positives: {count_positives}  
Sum of negatives: {sum_of_negatives}"  
#### Example

| Input | Output |
| ----- | ------ |
| 5<br />10<br />3<br />2<br />-15<br />-4 | [10, 3, 2]<br />[-15, -4]<br />Count of positives: 3<br />Sum of negatives: -19 |
| 6<br />11<br />2<br />35<br />599<br />31<br />20 | [11, 2, 35, 599, 31, 20]<br />[]<br />Count of positives: 6<br />Sum of negatives: 0 |

## 4.	Search
On the first line, you will receive a number n. On the second line, you will receive a word. On the following n lines, you will be given some strings. You should add them to a list and print them. After that, you should filter out only the strings that include the given word and print that list too.
#### Example

| Input | Output |
| ----- | ------ |
| 3<br />SoftUni<br />I study at SoftUni<br />I walk to work<br />I learn Python at SoftUni | ["I study at SoftUni", "I walk to work", "I learn Python at SoftUni"]<br />["I study at SoftUni", "I learn Python at SoftUni"] |
| 4<br />tomatoes<br />I love tomatoes<br />I can eat tomatoes forever<br />I don't like apples<br />Yesterday I ate two tomatoes | ["I love tomatoes", "I can eat tomatoes forever", "I don't like apples", "Yesterday I ate two tomatoes"]<br />["I love tomatoes", "I can eat tomatoes forever", "Yesterday I ate two tomatoes"] |

## 5.	Numbers Filter
On the first line, you will receive a single number n. On the following n lines, you will receive integers. After that, you will be given one of the following commands:
*	even
*	odd
*	negative
*	positive
Filter all the numbers that fit in the category (0 counts as a positive and even). Finally, print the result.  
#### Example

| Input | Output |
| ----- | ------ |
| 5<br />33<br />19<br />-2<br />18<br />998<br />even | [-2, 18, 998] |
| 3<br />111<br />-4<br />0<br />negative | [-4] |
