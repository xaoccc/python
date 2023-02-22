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

