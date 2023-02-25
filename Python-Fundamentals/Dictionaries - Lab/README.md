# Lab: Dictionaries
## 1.	Bakery
Your first task at your new job is to create a table of the stock in a bakery, and you really don't want to fail on your first day at work.  
You will receive a single line containing some food (keys) and quantities (values). They will be separated by a single space (the first element is the key, the second – the value, and so on). Create a dictionary with all the keys and values and print it on the console.  
#### Example

| Input | Output |
| ----- | ------ |
| bread 10 butter 4 sugar 9 jam 12 | {'bread': 10, 'butter': 4, 'sugar': 9, 'jam': 12} |
| eggs 3 sugar 7 salt 1 butter 3 | {'eggs': 3, 'sugar': 7, 'salt': 1, 'butter': 3} |

## 2.	Stock
After you have completed your first task, your boss decides to give you another one right away. Now not only you have to keep track of the stock, but also you should answer customers if you have some products in stock or not.  
You will be given key-value pairs of products and quantities (on a single line separated by space). On the following line, you will be given products to search for. Check for each product. You have 2 possibilities:  
*	If you have the product, print "We have {quantity} of {product} left".  
*	Otherwise, print "Sorry, we don't have {product}".  
#### Example

| Input | Output |
| ----- | ------ |
| cheese 10 bread 5 ham 10 chocolate 3<br />jam cheese ham tomatoes | Sorry, we don't have jam<br />We have 10 of cheese left<br />We have 10 of ham left<br />Sorry, we don't have tomatoes |
| eggs 5 bread 10<br />bread eggs | We have 10 of bread left<br />We have 5 of eggs left |
 
## 3.	Statistics
You seem to be doing great at your first job, so your boss decides to give you as your next task something more challenging. You have to accept all the new products coming in the bakery and finally gather some statistics.  
You will be receiving key-value pairs on separate lines separated by ": " until you receive the command "statistics". Sometimes you may receive a product more than once. In that case, you have to add the new quantity to the existing one. When you receive the "statistics" command, print the following:  
"Products in stock:  
- {product1}: {quantity1}  
- {product2}: {quantity2}  
…  
- {productN}: {quantityN}  
Total Products: {count_all_products}  
Total Quantity: {sum_all_quantities}"  
#### Example

| Input | Output |
| ----- | ------ |
| bread: 4<br />cheese: 2<br />ham: 1<br />bread: 1<br />statistics | Products in stock:<br />- bread: 5<br />- cheese: 2<br />- ham: 1<br />Total Products: 3<br />Total Quantity: 8 |
| eggs: 10<br />bread: 6<br />cheese: 8<br />milk: 7<br />statistics | Products in stock:<br />- eggs: 10<br />- bread: 6<br />- cheese: 8<br />- milk: 7<br />Total Products: 4<br />Total Quantity: 31 |

## 4.	Students
You will be receiving names of students, their ID, and a course of programming they have taken in the format "{name}:{ID}:{course}". On the last line, you will receive a name of a course in snake case lowercase letters. You should print only the information of the students who have taken the corresponding course in the format: "{name} - {ID}" on separate lines.   
Note: each student's ID will always be unique  
#### Example

| Input | Output |
| ----- | ------ |
| Peter:123:programming basics<br />John:5622:fundamentals<br />Maya:89:fundamentals<br />Lilly:633:fundamentals<br />fundamentals | John - 5622<br />Maya - 89<br />Lilly - 633 |
| Alex:6:programming basics<br />Maria:7:programming basics<br />Kaloyan:9:advanced<br />Todor:10:fundamentals<br />programming_basics | Alex - 6<br />Maria - 7 |

## 5.	 ASCII Values
Write a program that receives a list of characters separated by ", ". It should create a dictionary with each character as a key and its ASCII value as a value. Try solving that problem using comprehension.  
#### Examples

| Input | Output |
| ----- | ------ |
| a, b, c, a | {'a': 97, 'b': 98, 'c': 99} |
| d, c, m, h | {'d': 100, 'c': 99, 'm': 109, 'h': 104} |

## 6. Odd Occurrences
Write a program that prints all elements from a given sequence of words that occur an odd number of times (case-insensitive) in it.  
*	Words are given on a single line, space-separated.
*	Print the result elements in lowercase, in their order of appearance.
#### Examples

| Input | Output |
| ----- | ------ |
| Java C# PHP PHP JAVA C java | java c# c |
| 3 5 5 hi pi HO Hi 5 ho 3 hi pi | 5 hi |
| a a A SQL xx a xx a A a XX c | a sql xx c |

## 7.	Word Synonyms
Write a program, which keeps a dictionary with synonyms. The key of the dictionary will be the word. The value will be a list of all the synonyms of that word. You will be given a number n – the count of the words. After each term, you will be given a synonym, so the count of lines you should read from the console is 2 * n. You will be receiving a word and a synonym each on a separate line like this:  
*	{word}
*	{synonym}
If you get the same word twice, just add the new synonym to the list.  
Print the words in the following format:  
{word} - {synonym1, synonym2 … synonymN}  
#### Examples

| Input | Output |
| ----- | ------ |
| 3<br />cute<br />adorable<br />cute<br />charming<br />smart<br />clever | cute - adorable, charming<br />smart - clever |
| 2<br />task<br />problem<br />task<br />assignment | task – problem, assignment |
