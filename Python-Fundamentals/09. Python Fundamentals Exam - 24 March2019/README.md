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

# Problem 3. Apartments
### Input / Constraints
We have the task to create database for a businessman, who buys apartments in different neighborhoods here in Sofia.  
At the first stage he does a research for available apartments. He will give you a neighborhood name and a list of block numbers in format:

{neighborhood} -> {block_num,block_num,block_num}

When you receive the command ‘collectApartments’ you should stop adding research results and start assigning them with the real data. Note that the businessman can give you a neighborhood or a block number which haven’t been researched. In this case just do nothing, but if he gives you a researched neighborhood and a researched block number in this neighborhood assign the values for it. The data will come in the following format:

{ neighborhood}&{block_number} -> {count_of_available_apartments}|{price_for_one_apartment}

It’s  possible to receive existing neighborhood and block_number and already assigned count_of_available_apartments with given price. In this case REPLACE  the old info with the new one.  
### Output
When you recieve a command which says 'report', you should print all apartments data ordered by name of the neighborhood ascending after that by block_number ascending in the following format:

Neighborhood: {neighborhood}  
*Block number: {block_number} -> { count_of_available_apartments } apartments for sale. Price for one: {price_for_one_apartment }

* If  there is no available apartments in this block in this neighborhood just print 0 for the available apartments count.
* If there is no price, just print for price_for_one_apartment ‘None’.

### Examples

| Input | Output | Comments |
| ----- | ------ | ----- |
| Lozenec -> 11,2<br />Durvenica -> 4,3<br />Mladost1 -> 5,2<br />Mladost2 -> 7,8<br />collectApartments<br />Lozenec&11 -> 2\|100000<br />Lozenec&2 -> 1\|100000<br />Durvenica&3 -> 5\|80000<br />Durvenica&5 -> 15\|80000<br />Mladost2&13 -> 6\|80000<br />Mladost1&13 -> 7\|79000<br />report | Neighborhood: Durvenica<br /> \* Block number: 3 -> 5 apartments for sale. Price for one: 80000 <br />\* Block number: 4 -> 0 apartments for sale. Price for one: None <br />Neighborhood: Lozenec<br />\* Block number: 2 -> 1 apartments for sale. Price for one: 100000<br />\* Block number: 11 -> 2 apartments for sale. Price for one: 100000<br />Neighborhood: Mladost1<br />\* Block number: 2 -> 0 apartments for sale. Price for one: None<br />\* Block number: 5 -> 0 apartments for sale. Price for one: None<br />Neighborhood: Mladost2<br />\* Block number: 7 -> 0 apartments for sale. Price for one: None<br />\* Block number: 8 -> 0 apartments for sale. Price for one: None | Here we are just collecting data for researched apartments.<br /><br /> We receive the first data we should assign.We check that we have Lozenec in researched apartments and check that we have this block number. We have it so we store the info.We repeat the same for the next line.<br /><br />After that we receive another Neighborhood and again we check if we have the information for this block number in this neighborhood.We have it so we add it.<br /><br />On the next line we see we have the neighborhood, but we do not have this block number there, so we skip this info.We order everything and print it. Note that we have researched block numbers but there weren’t any apartments so the data for them is 0 and None! |
| StudentskiGrad -> 11,2<br />KrasnaPolyana -> 5,2<br />Borovo -> 4,3<br />KrasnaPolyana -> 5,8<br />collectApartmentsv<br />StudentskiGrad&2 -> 3|100000<br />Lozenec&2 -> 1\|100000<br />Durvenica&3 -> 5\|80000<br />Durvenica&5 -> 15\|80000<br />Mladost2&13 -> 6\|80000<br />Mladost1&13 -> 7\|79000<br />report | Neighborhood: Borovo<br />\* Block number: 3 -> 0 apartments for sale. Price for one: None<br />\* Block number: 4 -> 0 apartments for sale. Price for one: None<br />Neighborhood: KrasnaPolyana<br />\* Block number: 2 -> 0 apartments for sale. Price for one: None<br />\* Block number: 5 -> 0 apartments for sale. Price for one: None<br />\* Block number: 8 -> 0 apartments for sale. Price for one: None<br />Neighborhood: StudentskiGrad<br />\* Block number: 2 -> 3 apartments for sale. Price for one: 100000<br />\* Block number: 11 -> 0 apartments for sale. Price for one: None |  |
