# Problem 1. Build a building
We are going to try to build a building. For that we will receive the budget, of course we have initial capital – m  and after that we will receive n – the number of investors who are interested to take place in our project. In the next n-lines we will receive numbers (one at a row) – the money which investors want to give us. For every investor we must print information in the following format:  
‘Investor {number} gave us {money_given}.’  
Where {money_given} is formatted two digits after the decimal point.  
If at some point we have enough money to build our building we should stop taking investors money and print:  
‘We will manage to build it. Start now! Extra money - {extra_money}.”  
If we didn’t collect enough capital after all investors’ money we must print:  
‘Project can not start. We need {money} more.’  
### Input
You will recieve on the first 3 lines:
*	budget – the budget we need to build the building [floating  number]
*	m – the initial capital we have[floating number]
*	n – number of investors [integer number]
For each investor you will receive:
*	money – The money that this investor has given to us [floating  number]
### Output
If you have enough money at some point  
*	„We will manage to build it. Start now! Extra money - {extra_money}.”  
Where extra_money is the money which has left, formatted two digits after decimal point  
If you do not have enough money after all investors have invested print:  
*	„Project can not start. We need {difference} more.”  
Where {money} is the money you need to reach the planned budget, formatted two digits after decimal point.  
### Example

| Input | Output | Comments |
| ----- | ------ | -------- |
| 2250000<br />675000<br />3<br />1000000<br />750000<br />450000 | Investor 1 gave us 1000000.00.<br />Investor 2 gave us 750000.00.<br />We will manage to build it. Start now! Extra money - 175000.00.<br /> | The budget we need is 2250000. We have initial capital of 675000. We have 3 investors, so we start taking money.<br />675000 + 1000000 = 1675000<br />1675000 + 750000 = 2425000<br />This is enough money, so we print the information and stop collecting money.<br /> |
| 15000000<br />300000.99<br />2<br />2000000.37<br />8000000.25 | Investor 1 gave us 2000000.37.<br />Investor 2 gave us 8000000.25.<br />Project can not start. We need 4699998.39 more. |  |

# Problem 2. Command Center
### Input / Constraints
We are going to receive a list of integers from console. After that we will start receive some of the following commands in format:
* swap {index1} {index2}
* enumerate_list
* max
* min
* get_divisible by {number}

*If you receive command 'swap' you should check if the indexes are valid. A valid index is index which is 0 or higher and is less than list length. 
    -   If one of the indexes is not valid just print the list without changing it
    -   If both indexes are valid swap the two elements on these indexes

*If you receive ‘enumerate_list’ you should enumerate the list and print it in the following format:
	[(0, {list[0]}), (1, list[1]), (2, list[2]), (3, list[3])]
Where {list[n]} is the element corresponding to the given index (starting from zero)  

* If you receive 'max', print the max number in the list
* If you receive 'min', print the min number in the list

* If you receive ‘get_divisible by’ you must print every element in the list which residue after division with {number} is 0 in format:
[el1, el2, ….]  
It is guaranteed -  the {number} never will be 0, so you do not need to check it.  

### Output
When you recieve a command which says 'end', you should print the count of commands you have performed. Note that invalid commands may appear. In this case do not print anything and do not count these commands as performed.
