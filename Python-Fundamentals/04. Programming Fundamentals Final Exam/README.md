# Problem 1 - Password Reset

Yet again, you have forgotten your password. Naturally, it's not the first time this has happened. Actually, you got so tired of it that you decided to help yourself with an intelligent solution.  
Write a password reset program that performs a series of commands upon a predefined string. First, you will receive a string, and afterward, until the command "Done" is given, you will be receiving strings with commands split by a single space. The commands will be the following:  
*	"TakeOdd"  
    *	 Takes only the characters at odd indices and concatenates them to obtain the new raw password and then prints it.  
*	"Cut {index} {length}"  
    *	Gets the substring with the given length starting from the given index from the password and removes its first occurrence, then prints the password on the console.  
    *	The given index and the length will always be valid.  
*	"Substitute {substring} {substitute}"  
    *	If the raw password contains the given substring, replaces all of its occurrences with the substitute text given and prints the result.
    *	If it doesn't, prints "Nothing to replace!".  
### Input
*	You will be receiving strings until the "Done" command is given.
### Output
*	After the "Done" command is received, print:
    *	"Your password is: {password}"
### Constraints
*	The indexes from the "Cut {index} {length}" command will always be valid.
### Examples

| Input | Output |
| ----- | ------ |
| Siiceercaroetavm!:?:ahsott.:i:nstupmomceqr <br />TakeOdd<br />Cut 15 3<br />Substitute :: -<br />Substitute \| ^<br />Done | icecream::hot::summer<br />icecream::hot::mer<br />icecream-hot-mer<br />Nothing to replace!<br />Your password is: icecream-hot-mer |
| up8rgoyg3r1atmlmpiunagt!-irs7!1fgulnnnqy<br />TakeOdd<br />Cut 18 2<br />Substitute ! \*\*\*<br />Substitute ? .!.<br />Done | programming!is!funny<br />programming!is!fun<br />programming\*\*\*is\*\*\*fun<br />Nothing to replace!<br />Your password is: programming\*\*\*is\*\*\*fun |

№ Problem 2 - Fancy Barcodes

Your first task is to determine if the given sequence of characters is a valid barcode or not. 
Each line must not contain anything else but a valid barcode. A barcode is valid when:
*	It is surrounded by a "@" followed by one or more "#"
*	It is at least 6 characters long (without the surrounding "@" or "#")
*	It starts with a capital letter
*	It contains only letters (lower and upper case) and digits
*	It ends with a capital letter
Examples of valid barcodes: @###Che46sE@##, @#FreshFisH@#, @###Brea0D@###, @##Che46sE@##  
Examples of invalid barcodes: ##InvaliDiteM##, @InvalidIteM@, @#Invalid_IteM@#  
Next, you have to determine the product group of the item from the barcode. The product group is obtained by concatenating all the digits found in the barcode. If there are no digits present in the barcode, the default product group is "00".  
### Examples:  
@#FreshFisH@# -> product group: 00  
@###Brea0D@### -> product group: 0  
@##Che4s6E@## -> product group: 46  
### Input
On the first line, you will be given an integer n – the count of barcodes that you will be receiving next.  
On the following n lines, you will receive different strings.  
### Output
For each barcode that you process, you need to print a message.  
If the barcode is invalid:  
*	"Invalid barcode"
If the barcode is valid:  
*	"Product group: {product group}"
### Examples

| Input | Output |
| ----- | ------ |
| 3<br />@#FreshFisH@#<br />@###Brea0D@###<br />@##Che4s6E@##| Product group: 00<br />Product group: 0<br />Product group: 46 |
| 6<br />@###Val1d1teM@###<br />@#ValidIteM@#<br />##InvaliDiteM##<br />@InvalidIteM@<br />@#Invalid_IteM@#<br />@#ValiditeM@# | Product group: 11<br />Product group: 00<br />Invalid barcode<br />Invalid barcode<br />Invalid barcode<br />Product group: 00 |
