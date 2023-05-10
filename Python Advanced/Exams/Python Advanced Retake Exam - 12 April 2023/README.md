## 1.	Rubber Duck Debuggers

*Rubber Duck Debugging is a type of debugging where you place a rubber duck on your desk and explain to it your code line by line. You gathered a few programmers and gave them a task and judging by the time it took them to write the code, you reward them with a type of rubber ducky.*  
You will be given two sequences of integers. The first one represents the time it takes a programmer to complete a single task. The second one represents the number of tasks you’ve given to your programmers.  
Your task is to count how many rubber ducks of each type you’ve given to your programmers.  
While you have values in the sequences, you need to start from the first value of the programmers time's sequence and multiply them by the last value of the tasks' sequence:  
*	If the calculated time is between any of the time ranges below, you give the corresponding ducky and remove the programmer time's value and the tasks' value.
*	If the calculated time goes above the highest range, decrease the number of the tasks' value by 2. Then, move the programmer time's value to the end of its sequence, and continue with the next operation.

| Rubber Ducky type | Time needed to earn it |
| ----- | ------ |
| Darth Vader Ducky | 0 - 60 |
| Thor Ducky | 61 - 120 |
| Big Blue Rubber Ducky | 121 - 180 |
| Small Yellow Rubber Ducky | 181 - 240 |

Your task is considered done when the sequences are empty.  
#### Input
*	The first line will represent each programmer’s time to complete a single task – integers, separated by a single space.
*	The second line will represent the number of tasks that should be completed – integers, separated by a single space.
#### Output
*	On the first line, you output:
    *	"Congratulations, all tasks have been completed! Rubber ducks rewarded:"
*	On the next 4 lines, you output the type and number of ducks given, ordered like in the table:
    *	"Darth Vader Ducky: {count}
Thor Ducky: {count}  
Big Blue Rubber Ducky: {count}  
Small Yellow Rubber Ducky: {count}"  
#### Constraints
*	All the given numbers will be valid integers in the range [1, 1000].
*	There will be no negative inputs.
*	The number of values in both sequences will always be equal.
#### Examples

| Input | Output |
| ----- | ------ |
| 10 15 12 18 22 6<br />12 16 5 6 9 1 | Congratulations, all tasks have been completed! Rubber ducks rewarded:<br />Darth Vader Ducky: 1<br />Thor Ducky: 3<br />Big Blue Rubber Ducky: 1<br />Small Yellow Rubber Ducky: 1 |
| 2 55 17 31 23<br />7 5 17 4 27 | Congratulations, all tasks have been completed! Rubber ducks rewarded: <br />Darth Vader Ducky: 1<br />Thor Ducky: 0<br />Big Blue Rubber Ducky: 2<br />Small Yellow Rubber Ducky: 2 |

## 2. The Squirrel
*An intern from a big company must solve the game - "The squirrel". He doesn’t have enough experience, so he needs your help.*  
Here are the rules of the game:  
The game starts with 0 collected hazelnuts. Your goal is to collect 3 of them.  
You get as input the size of the field, which will be always a square shape. After that, you will receive the directions in which the squirrel can move – "left", "right", "down", and "up" in a sequence, each value separated by a comma and a space (", "). On the next rows, you will receive the field.  
Possible characters in the field:  
*	s - represents the squirrel's position.
*	h – represents a hazelnut. 
*	* – the asterisk represents an empty position.
*	t – represents a trap.
The squirrel starts from the s - position.  
*	If the squirrel steps on a hazelnut, you have to increase them by 1. The position should be marked with an asterisk (\*).
*	If the squirrel collects all 3 hazelnuts, the game ends.
*	Asterisk (\*) does nothing, so nothing happens if the squirrel steps on it.
*	If it steps on a trap, the game ends.
*	If the squirrel moves out of the field, the game ends.
After all commands you will have 4 possible results:  
*	You win if the squirrel collects 3 of the hazelnuts.
*	The squirrel collects less than 3 hazelnuts.
*	The squirrel steps on a trap.
*	The squirrel moves out of the field.
#### Input
*	On the first line, you will receive the length of the field – an integer number in the range [3, 5].
*	On the second line, you will receive the commands to move the squirrel – an array of strings separated by ", ".
*	In the next N lines, you will receive the values for every row.
#### Output
*	On the first line:
    *	If the squirrel goes out of the field - "The squirrel is out of the field.".
    *	If the squirrel steps on a trap - "Unfortunately, the squirrel stepped on a trap...".
    *	If the squirrel hasn’t collected all hazelnuts - "There are more hazelnuts to collect.".
    *	If the squirrel has collected all hazelnuts - "Good job! You have collected all hazelnuts!".
*	On the second line, print the number of collected hazelnuts - "Hazelnuts collected: {hazelnutsCount}"
#### Constraints
*	The size of the field will be between [3,5].
*	There could be one or no trap on the field.
*	There will always be 3 hazelnuts on the field.
#### Examples

| Input | Output |
| ----- | ------ |
| 5<br />left, left, up, right, up, up<br />\*\*h\*\*<br />t\*\*\*\*<br />\*h\*\*\*<br />\*h\*s\*<br />\*\*\*\*\* | Good job! You have collected all hazelnuts!<br />Hazelnuts collected: 3 |
| 4<br />down, down, right, right<br />\*s\*h<br />\*\*\*h<br />\*\*\*t<br />h\*\*\* | Unfortunately, the squirrel stepped on a trap...<br />Hazelnuts collected: 0 |
| 4<br />down, down, right, right<br />h\*\*\*<br />\*\*\*h<br />\*s\*t<br />\*\*h\* | The squirrel is out of the field.<br />Hazelnuts collected: 0 |

## 3. Movie Organizer
Mary has a large collection of films, from old black-and-white classics to the newest blockbusters. But her collection is an unorganized jumble. She spends hours searching for a particular movie, only to find it in the most unexpected place. Mary needs your help to organize her movies.  
Write a function called "movie_organizer" that groups movies by genre. The function will receive a different number of arguments, passed as tuples containing two elements: the first one is the movie's name, and the second is the genre for example ("Movie Name", "Genre").  
The function should sort the movies by their genre. Arrange Mary's collection by the number of movies in each genre in descending order. If two or more genres have the same number of movies, return them in ascending order (alphabetically) by genre.  
Each genre group should be sorted in ascending order (alphabetically) by the movie's name.  
To help Mary keep track of her movies, add next to each genre the number of movies in the group.  
In the end, return the output as described below.  
Note: Submit only the function in the judge system  
#### Input
*	There will be no input from the console, just parameters passed to your function
#### Output
*	The output should look like this:
"{genre_1} - {number_of_movies_in_the_genre_group}  
\* {movie_name_1}  
\* {movie_name_2}  
\* {movie_name_3}  
…  
\* {movie_name_n}  
{genre_2} - {number_of_movies_in_the_genre_group}  
\* {movie_name_1}  
\* {movie_name_2}  
…  
\* {movie_name_n}  
{genre_n} - {number_of_movies_in_the_genre_group}  
\* {movie_name_1}  
…  
\* {movie_name_n}"  
Constraints
*	Each tuple given will always contain a movie with its genre.
*	You will never receive the same movie twice or more times.
#### Examples

| Test Code | Output |
| ----- | ------ |
| print(movie_organizer(("The Matrix", "Sci-fi"))) |	Sci-fi - 1<br />\* The Matrix |
| print(movie_organizer(("The Godfather", "Drama"), ("The Hangover", "Comedy"), ("The Shawshank Redemption", "Drama"), ("The Pursuit of Happiness", "Drama"), ("The Hangover Part II", "Comedy"))) |	Drama - 3<br />\* The Godfather<br />\* The Pursuit of Happiness<br />\* The Shawshank Redemption<br />Comedy - 2<br />\* The Hangover<br />\* The Hangover Part II |
| print(movie_organizer(("Avatar: The Way of Water", "Action"), ("House Of Gucci", "Drama"), ("Top Gun", "Action"), ("Ted", "Comedy"), ("Duck Soup", "Comedy"), ("The Dark Knight", "Action"), ("A Star Is Born", "Musicals"), ("The Warrior", "Action"), ("Like A Boss", "Comedy"), ("The Green Mile", "Drama"), ("21 Jump Street", "Comedy"))) |	Action - 4<br />\* Avatar: The Way of Water<br />\* The Dark Knight<br />\* The Warrior<br />\* Top Gun <br />Comedy - 4<br />\* 21 Jump Street<br />\* Duck Soup<br />\* Like A Boss<br />\* Ted<br />Drama - 2<br />\* House Of Gucci<br />\* The Green Mile<br />Musicals - 1<br />\* A Star Is Born |
