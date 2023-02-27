# More Exercise: Dictionaries
## 1.	Ranking  
Here comes the final and the most interesting part – the Final ranking of the candidate-interns. The final ranking is determined by the points of the interview tasks and by the points from the exams in SoftUni. Here is your final task. You will receive some lines of input in the format "{contest}:{password for contest}" until you receive "end of contests". Save that data because you will need it later. After that you will receive other type of inputs in format "{contest}=>{password}=>{username}=>{points}" until you receive "end of submissions". Here is what you need to do.  
*	Check if the contest is valid (It is considered valid if you received it in the first type of input)  
*	Check if the password is correct for the given contest  
*	If the contest and the password is valid, save the user with the contest they take part in (a user can take part in many contests) and the points the user has in the given contest. If you receive the same contest and the same user update the points only if the new ones are more than the older ones.  
In the end, you should print the info for the user with the most points (total points for all contents they participated in) in the format "Best candidate is {user} with total {total_points} points.". After that print all students ordered by their names. For each user print each contest with the points in descending order. See the examples.  
#### Input
*	Strings in format "{contest}:{password for contest}" until the "end of contests" command. There will be no case with two equal contests  
*	Strings in format "{contest}=>{password}=>{username}=>{points}" until the "end of submissions" command.  
*	There will be no case with 2 or more users with same total points!  
Output
*	On the first line, print the best user in format "Best candidate is {user} with total {total points} points.".
*	Then print all students ordered as mentioned above in format:  
"{user_name1}  
\#  {contest1} -> {points}  
\#  {contest2} -> {points}  
…  
\#  {contestN} -> {points}"  
#### Constraints
*	The strings may contain any ASCII character except from (:, =, >).
*	The numbers will be in range [0 - 10000].
*	Second input is always valid.
#### Examples

| Input | Output |
| ----- | ------ |
| Part One Interview:success<br />JS Fundamentals:fundExam<br />C# Fundamentals:fundPass<br />Algorithms:fun<br />end of contests<br />C# Fundamentals=>fundPass=>Tanya=>350<br />Algorithms=>fun=>Tanya=>380<br />Part One Interview=>success=>Nikola=>120<br />Java Basics Exam=>wrong_pass=>Teo=>400<br />Part One Interview=>success=>Tanya=>220<br />OOP Advanced=>password123=>Kay=>231<br />C# Fundamentals=>fundPass=>Tanya=>250<br />C# <br />undamentals=>fundPass=>Nikola=>200<br />JS Fundamentals=>fundExam=>Tanya=>400<br />end of submissions | Best candidate is Tanya with total 1350 points.<br />Ranking:<br />Nikola<br />#  C# Fundamentals -> 200<br />#  Part One Interview -> <br />120<br />Tanya<br />#  JS Fundamentals -> 400<br />#  Algorithms -> 380<br />#  C# Fundamentals -> 350<br />#  Part One Interview -> 220 |
| Java Advanced:funpass<br />Part Two Interview:success<br />Math Concept:asdasd<br />Java Web Basics:forrF<br />end of contests<br />Math Concept=>ispass=>Monika=>290<br />Java Advanced=>funpass=>Simona=>400<br />Part Two Interview=>success=>Drago=>120<br />Java Advanced=>funpass=>Petyr=>90<br />Java Web Basics=>forrF=>Simona=>280<br />Part Two Interview=>success=>Petyr=>0<br />Math Concept=>asdasd=>Drago=>250<br />Part Two Interview=>success=>Simona=>200<br />end of submissions | Best candidate is Simona with total 880 points.<br />Ranking:<br />Drago<br />\#  Math Concept -> 250<br />\#  Part Two Interview -> 120<br />Petyr<br />\#  Java Advanced -> 90<br />\#  Part Two Interview -> 0<br />Simona<br />\#  Java Advanced -> 400<br />\#  Java Web Basics -> 280<br />\#  Part Two Interview -> 200 |

## 2.	
