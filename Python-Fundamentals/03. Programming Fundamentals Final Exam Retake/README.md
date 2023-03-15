# Problem 1 - Secret Chat

You have plenty of free time, so you decide to write a program that conceals and reveals your received messages. Go ahead and type it in!  
On the first line of the input, you will receive the concealed message. After that, until the "Reveal" command is given, you will receive strings with instructions for different operations that need to be performed upon the concealed message to interpret it and reveal its actual content. There are several types of instructions, split by ":\|:"  
*	"InsertSpace:\|:{index}":
    *	Inserts a single space at the given index. The given index will always be valid.
*	"Reverse:\|:{substring}":
    *	If the message contains the given substring, cut it out, reverse it and add it at the end of the message. 
    *	If not, print "error".
    *	This operation should replace only the first occurrence of the given substring if there are two or more occurrences.
*	"ChangeAll:\|:{substring}:\|:{replacement}":
    *	Changes all occurrences of the given substring with the replacement text.
### Input / Constraints
*	On the first line, you will receive a string with a message.
*	On the following lines, you will be receiving commands, split by ":|:".
### Output
*	After each set of instructions, print the resulting string. 
*	After the "Reveal" command is received, print this message:
"You have a new text message: {message}"  
### Examples

| Input | Output |
| ----- | ------ |
| heVVodar!gniV<br />ChangeAll:\|:V:\|:l<br />Reverse:\|:!gnil<br />InsertSpace:\|:5<br />Reveal | hellodar!gnil<br />hellodarling!<br />hello darling!<br />You have a new text message: hello darling! |
| Hiware?uiy<br />ChangeAll:\|:i:\|:o<br />Reverse:\|:?uoy<br />Reverse:\|:jd<br />InsertSpace:\|:3<br />InsertSpace:\|:7<br />Reveal | Howare?uoy<br />Howareyou?<br />error<br />How areyou?<br />How are you?<br />You have a new text message: How are you? |

# Problem 2 - Mirror words

The SoftUni Spelling Bee competition is here. But it`s not like any other Spelling Bee competition out there. It`s different and a lot more fun! You, of course, are a participant, and you are eager to show the competition that you are the best, so go ahead, learn the rules and win!  
On the first line of the input, you will be given a text string. To win the competition, you have to find all hidden word pairs, read them, and mark the ones that are mirror images of each other.  
First of all, you have to extract the hidden word pairs. Hidden word pairs are:  
*	Surrounded by "@" or "#" (only one of the two) in the following pattern #wordOne##wordTwo# or @wordOne@@wordTwo@
*	At least 3 characters long each (without the surrounding symbols)
*	Made up of letters only
If the second word, spelled backward, is the same as the first word and vice versa (casing matters!), they are a match, and you have to store them somewhere. Examples of mirror words:  
#Part##traP# @leveL@@Level@ #sAw##wAs#  
*	If you don\'t find any valid pairs, print: "No word pairs found!"
*	If you find valid pairs print their count: "{valid pairs count} word pairs found!"
*	If there are no mirror words, print: "No mirror words!"
*	If there are mirror words print:
"The mirror words are:  
{wordOne} <=> {wordtwo}, {wordOne} <=> {wordtwo}, … {wordOne} <=> {wordtwo}"  
### Input / Constraints
*	You will recive a string.
### Output
*	Print the proper output messages in the proper cases as described in the problem description.
*	If there are pairs of mirror words, print them in the end, each pair separated by ", ".
*	Each pair of mirror word must be printed with " <=> " between the words.
### Examples

| Input | Output | Comments |
| ----- | ------ | ------ |
| @mix#tix3dj#poOl##loOp#wl@@bong&song%4very$long@thong#Part##traP##@@leveL@@Level@##car#rac##tu@pack@@ckap@#rr#sAw##wAs#r#@w1r | 5 word pairs found!<br />The mirror words are:<br />Part <=> traP, leveL <=> Level, sAw <=> wAs | There are 5 green and yellow pairs that meet all requirements and thus are valid.<br />#poOl##loOp# is valid and looks very much like a mirror words pair, but it isn\`t because the casings don\`t match.<br />#car#rac# "rac" spelled backward is "car", but this is not a valid pair because there is only one "#" between the words.<br />@pack@@ckap@ is also valid, but "ckap" backward is "pakc" which is not the same as "pack", so they are not mirror words. |
| #po0l##l0op# @bAc##cAB@ @LM@ML@ #xxxXxx##xxxXxx# @aba@@ababa@ | 2 word pairs found!<br />No mirror words! |"xxxXxx" backward is not the same as "xxxXxx"<br />@aba@@ababa@ is a valid pair, but the word lengths are different - these are definitely not mirror words |
| #lol#lol# @#God@@doG@# #abC@@Cba# @Xyu@#uyX# | No word pairs found!<br />No mirror words! |   |
