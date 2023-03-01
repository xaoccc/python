# Lab: Text Processing
## 1.	Reverse Strings
You will be given strings on separate lines until you receive an "end" command. Write a program that reverses strings and prints each pair on a separate line in the format "{word} = {reversed_word}".
#### Examples

| Input | Output |
| ----- | ------ |
| helLo<br />Softuni<br />bottle<br />end | helLo = oLleh<br />Softuni = inutfoS<br />bottle = elttob |
| Dog<br />caT<br />chAir<br />end | Dog = goD<br />caT = Tac<br />chAir = riAhc |

## 2.	Repeat Strings
Write a program that reads a sequence of strings, separated by a single space. Each string should be repeated N times, where N is the length of the string. Print the final strings concatenated into one string.
#### Examples

| Input | Output |
| ----- | ------ |
| hi abc add | hihiabcabcabcaddaddadd |
| work | workworkworkwork |
| ball | ballballballball |

## 3.	Substring
On the first line, you will receive a string. On the second line, you will receive a second string. Write a program that removes all the occurrences of the first string in the second until there is no match. At the end, print the remaining string.
#### Examples

| Input | Output |
| ----- | ------ |
| ice<br />kicegiciceeb | kgb |

## 4.	Text Filter
Write a program that receives a text and a string of banned words, separated by a comma and space ", ". All banned words in the text should be replaced with the number of asterisks "*", equal to the word's length.  
The ban list will be entered on the first input line and the text - on the second input line. 
#### Examples

| Input | Output |
| ----- | ------ |
| Linux, Windows<br />It is not Linux, it is GNU/Linux. Linux is merely the kernel, while GNU adds the functionality. Therefore we owe it to them by calling the OS GNU/Linux! Sincerely, a Windows client | It is not \*\*\*\*\*, it is GNU/\*\*\*\*\*. \*\*\*\*\* is merely the kernel, while GNU adds the functionality. Therefore we owe it to them by calling the OS GNU/\*\*\*\*\*! Sincerely, a \*\*\*\*\*\*\* client |

## 5.	Digits, Letters, and Other
Write a program that receives a single string. On the first line, print all the digits found in the string, on the second – all the letters, and on the third – all the other characters. There will always be at least one digit, one letter, and one other character.
#### Examples

| Input | Output |
| ----- | ------ |
| Agd#53Dfg^&4F53 | 53453<br />AgdDfgF<br />#^& |
