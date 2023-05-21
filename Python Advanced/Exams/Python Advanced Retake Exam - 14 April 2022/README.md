# Python Advanced Retake Exam - 14 April 2022
### 01.	 Ramen Shop
You will be given two sequences of integers representing bowls of ramen and customers. Your task is to find out if you can serve all the customers.  
Start by taking the last bowl of ramen and the first customer. Try to serve every customer with ramen until we have no more ramen or customers left:  
*	Each time the value of the ramen is equal to the value of the customer, remove them both and continue with the next bowl of ramen and the next customer.  
*	Each time the value of the ramen is bigger than the value of the customer, decrease the value of that ramen with the value of that customer and remove the customer. Then try to match the same bowl of ramen (which has been decreased) with the next customer.  
*	Each time the customer's value is bigger than the value of the ramen bowl, decrease the value of the customer with the value of the ramen bowl and remove the bowl. Then try to match the same customer (which has been decreased) with the next bowl of ramen.  
Look at the examples provided for a better understanding of the problem.
#### Input
*	On the first line, you will receive integers representing the bowls of ramen, separated by a single space and a comma ", ".
*	On the second line, you will receive integers representing the customers, separated by a single space and a comma ", ".
#### Output
*	If all customers are served, print: "Great job! You served all the customers."
     *	Print all of the left ramen bowls (if any) separated by comma and space in the format: "Bowls of ramen left: {bowls of ramen left}"
*	Otherwise, print: "Out of ramen! You didn't manage to serve all customers."
     *	Print all customers left separated by comma and space in the format "Customers left: {customers left}"
#### Examples

| Input | Output |
| ----- | ------ |
| Input | Output |
| ----- | ------ |