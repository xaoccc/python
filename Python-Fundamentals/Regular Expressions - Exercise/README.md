# Exercise: Regular Expressions
## 1.	Capture the Numbers
Write a program that receives strings on different lines and extracts only the numbers. Print all extracted numbers on a single line, separated by a single space.  
#### Examples

| Input | Output |
| ----- | ------ |
| The300<br />What is that?<br />I think it's the 3rd movie <br />Let's watch it at 22:45 | 300 3 22 45 |
| 123a456<br />789b987<br />654c321<br />0 | 123 456 789 987 654 321 0 |
| Let's go11!!!11!<br />Okey!1! | 11 11 1 |

## 2.	Find Variable Names in Sentences
Write a program that finds all variable names in each string. A variable name starts with an underscore ("_") and contains only capital and non-capital letters and digits. Extract only their names without the underscore. Try to do this only with regular expressions.
The output consists of all variable names extracted and printed on a single line, separated by a comma.  
#### Examples

| Input | Output |
| ----- | ------ |
| The _id and _age variables are both integers. | id,age |
| Calculate the _area of the _perfectRectangle object. | area,perfectRectangle |
| _\_invalidVariable \_evenMoreInvalidVariable\_ \_validVariable | validVariable |
	
## 3.	Find Occurrences of Word in Sentence
Write a program that finds how many times a word is used in a string. The output is a single number indicating the number of times the string contains the word. Note that letter case does not matter – it is case-insensitive.
#### Examples
	
| Input | Output |
| ----- | ------ |
| The waterfall was so high, that the child couldn't see its peak.<br />the | 2 |
| How do you plan on achieving that? How? How can you even think of that? <br />how | 3 |
| There was one. Therefore I bought it. I wouldn't buy it otherwise.<br />there | 1 |

## 4.	Extract Emails
Write a program that receives a single string and extracts all email addresses from it. Print the extracted email addresses on separate lines. Emails are in the format "{user}@{host}", where: 
*	{user} could consist only of letters and digits; the symbols ".", "-" and "_" can appear between them.  
    *	Examples of valid users: "stephan", "mike03", "s.johnson", "st_steward", "softuni-bulgaria", "12345"  
    *	Examples of invalid users: ''--123", ".....", "nakov_-", "_steve", ".info"  
*	{host} is a sequence of at least two words, each couple of words must be separated by a single dot ".". Each word consists of only letters and can have hyphens "-" between the letters.  
    *	Examples of valid hosts: "softuni.bg", "software-university.com", "intoprogramming.info", "mail.softuni.org"  
    *	Examples of invalid hosts: "helloworld", ".unknown.soft." , "invalid-host-", "invalid-"  
Examples of valid emails: info@softuni-bulgaria.org, kiki@hotmail.co.uk, no-reply@github.com,  s.peterson@mail.uu.net, info-bg@software-university.software.academy  
Examples of invalid emails: --123@gmail.com, …@mail.bg, .info@info.info, _steve@yahoo.cn, mike@helloworld, mike@.unknown.soft., s.johnson@invalid-  
#### Examples
	
| Input | Output |
| ----- | ------ |
| Please contact us at: support@github.com. | support@github.com |
| Just send email to s.miller@mit.edu and j.hopking@york.ac.uk for more information. | s.miller@mit.edu<br />j.hopking@york.ac.uk |
| Many users @ SoftUni confuse email addresses. We @ Softuni.BG provide high-quality training @ home or @ class. –- steve.parker@softuni.de. | steve.parker@softuni.de |

## 5. Furniture
Write a program that calculates the total cost of bought furniture. You will be given information about each purchase on separate lines until you receive the command "Purchase". Valid information should be in the format: ">>{furniture_name}<<{price}!{quantity}". The price could be a floating-point or integer number. You should store the names of the furniture and the total price.  
In the end, print the name of each bought furniture and the total cost, formatted to the second decimal point:   
"Bought furniture:  
{1st name}  
{2nd name}  
…  
{N name}  
Total money spend: {total_cost}"  
#### Examples

| Input | Output | Comment |
| ----- | ------ | ------ |
| >>Sofa<<312.23!3<br />>>TV<<300!5<br />>Invalid<<!5<br />Purchase | Bought furniture:<br />Sofa<br />TV<br />Total money spend: 2436.69 | Only the Sofa and the TV are valid, for each of them we multiply the price by the quantity and print the result |

## 6.	*Extract the Links
Write a program that extracts links from a given text. The text will come in the form of strings, each representing a sentence. You need to extract only the valid links from it. Example:  

"www.internet.com"  
Sub-Domain : www  			 
Domain name: internet
Domain extension: com  

The Sub-Domain must always be "www". The Domain name can consist of English alphabet letters (uppercase and lowercase), digits, and dashes ("–"). The Domain extension consists of one or more domain blocks, a domain block consists of a dot followed by one or more lowercase English alphabet letters, a Domain extension must have at least one domain block in order to be valid. The Sub-Domain and Domain name must be separated by a single dot. Any link that does NOT follow the specified above rules should be treated as invalid.  
Example incorrect links:    
* "ww.justASite.bg"
* "lel.awesome.com"
* "www.weird_site.hit.bg"
* "www.no-symb#^ols-allow%ed.com"
* "www.mark.12"
* "www.web-site."
* "www.example-site._*^#"
Example of correct links:  
* "Some textwww.softuni.bg"
* "Just a link in a www.sea-of-text.bg-swimming around"
* "Instruments www.Instruments.rom.com.trombone2000 Instrument here"
* "All your ice cream flavors-www.scream.for.ice.cream (We also have squirrels)"
 The output is all valid links you have found, printed – each on a new line.
#### Examples

| Input | Output | 
| ----- | ------ | 
| Join WebStars now for free, at www.web-stars.com <br />You can also support our partners:<br />Internet - www.internet.com<br />WebSpiders - www.webspiders101.com<br />Sentinel - www.sentinel.-ko | www.web-stars.com<br />www.internet.com<br />www.webspiders101.com |
| Need information about cheap hotels in London?<br />You can check us at www.london-hotels.co.uk !<br />We provide the best services in London.<br />Here are some reviews in some blogs:<br />London Hotels are awesome! - www.indigo.bloggers.com <br />I am very satisfied with their services - ww.ivan.bg<br />Best Hotel Services! - www.rebel21.sedecrem.moc | www.london-hotels.co.uk<br />www.indigo.bloggers.com<br />www.rebel21.sedecrem.moc |
