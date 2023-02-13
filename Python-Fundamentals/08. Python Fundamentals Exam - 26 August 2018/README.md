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

