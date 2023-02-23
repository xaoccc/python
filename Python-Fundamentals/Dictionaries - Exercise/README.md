# Exercise: Dictionaries
## 1.	Count Chars in a String
Write a program that counts all characters in a string except for space (" "). 
Print all the occurrences in the following format:
"{char} -> {occurrences}"
#### Examples

| Input | Output |
| ----- | ------ |
| text | t -> 2<br />e -> 1<br />x -> 1 |
| text text text | t -> 6<br />e -> 3<br />x -> 3 |

## 2.	A Miner Task
You will be given a sequence of strings, each on a new line until you receive the "stop" command. Every odd line on the console represents a resource (e.g., Gold, Silver, Copper, and so on) and every even - quantity. Your task is to collect the resources and print them each on a new line.  
Print the resources and their quantities in the following format:  
"{resource} -> {quantity}"  
The quantities will be in the range \[1 … 2 000 000 000\].
#### Examples

| Input | Output | Input | Output |
| ----- | ------ | ----- | ------ |
| Gold<br />155<br />Silver<br />10<br />Copper<br />17<br />stop | Gold -> 155<br />Silver -> 10<br />Copper -> 17<br /> | gold<br />155<br />silver<br />10<br />copper<br />17<br />gold<br />15<br />stop | gold -> 170<br />silver -> 10<br />copper -> 17<br /> |
