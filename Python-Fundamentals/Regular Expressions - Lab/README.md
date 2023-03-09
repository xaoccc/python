# Lab: Regular Expressions

## 1.	Match Full Name  
Write a program to match full names from a sequence of characters and print them on the console.  
Writing the Regular Expression  
First, write a regular expression to match a valid full name, according to these conditions:  
*	A valid full name has the following characteristics:  
    *	It consists of two words.  
    *	Each word starts with a capital letter.  
    *	After the first letter, it only contains lowercase letters.  
    *	Each of the two words should be at least two letters long.  
    *	A single space separates the two words.  
To help you out, we have outlined several steps:  
1.	Use the online regex tester like https://pythex.org/ 
2.	Check out how to use character sets (denoted with square brackets - "[]")
3.	Specify that you want two words with a space between them (the space character ' ', and not any whitespace symbol)
4.	For each word, specify that it should begin with an uppercase letter using a character set. The desired characters are in a range – from 'A' to 'Z'.
5.	For each word, specify that what follows the first letter are only lowercase letters, one or more – use another character set and the correct quantifier.
6.	To prevent capturing of letters across new lines, put "\b" at the beginning and at the end of your regex. This will ensure that what precedes and what follows the match is a word boundary (like a new line).
To check your RegEx, use these values for reference (paste all of them in the Test String field):  

| Match ALL of these | Match NONE of these |
| ----- | ----- |
| Peter Smith | peter smith Peter smith peter Smith PEter Smi7h Peter SmIth |

#### Examples

| Input | 
| ----- | 
| Peter Smith, peter smith, Peter smith, peter Smith, PEter Smith, Peter SmIth, Lily Everett |
| Output |
| Peter Smith Lily Everett |

## 2.	Match Phone Number
Write a regular expression to match a valid phone number from Sofia. After you find all valid phones, print them on the console, separated by a comma and a space ", ".
Compose the Regular Expression    
A valid number has the following characteristics:  
*	It starts with "+359"
*	Then, it is followed by the area code (always 2)
*	After that, it is followed by a number:
    *	The number consists of 7 digits (separated into two groups of 3 and 4 digits, respectively). 
*	The different parts are separated by either a space or a hyphen ('-').
You can use the following RegEx properties to help with the matching: 
*	Use quantifiers to match a specific number of digits  
*	Use a capturing group to make sure the delimiter is only one of the allowed characters (space or hyphen) and not a combination of both (e.g., +359 2-111 111 has mixed delimiters, it is invalid). Use a group backreference to achieve this.  
*	Add a word boundary at the end of the match to avoid partial matches.
*	Ensure that there is a space before the '+' sign, or it is positioned at the beginning of the string.
You can use the following table of values to test your RegEx:  

| Input | 
| ----- | 
| +359 2 222 2222,359-2-222-2222, +359/2/222/2222, +359-2 222 2222 +359 2-222-2222, +359-2-222-222, +359-2-222-22222 +359-2-222-2222 |
| Output |
| +359 2 222 2222, +359-2-222-2222 |
