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
| 2250000<br />675000<br />3<br />1000000<br />750000<br />450000 | Investor 1 gave us 1000000.00.
Investor 2 gave us 750000.00.
We will manage to build it. Start now! Extra money - 175000.00.
 | Comments |
| ----- | ------ | -------- |
