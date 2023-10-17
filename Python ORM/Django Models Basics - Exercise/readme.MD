Exercises: Django Models Basics
This document defines the exercise assignments for the Python ORM course @ Software University.
Submit your solutions in the SoftUni Judge system.

1.	Person
Write a Django model called "Person" which stores information about their name and age:
-	"name": Character field.	Every "name" has a length with a maximum of 30 characters.
-	"age":	Positive integer field.
2.	Blog
Write a Django model called "Blog" which stores information about the blog’s "post" and "author":
-	"post":	Text field.
-	"author": 	Character field.	Every "author" has a length with a maximum of 35 characters.
Apply all the migrations to the database.

3.	Weather Forecast
Write a Django model called "WeatherForecast" with the following parameters:
-	"date":	Date field.
-	"temperature": 
 Float field.
-	"humidity": 
 Float field.
-	"precipitation":
 Float field.
Apply all the migrations to the database.

4.	Recipe
Write a Django model called "Recipe" with the provided information:
-	"name": 
 Character field.
 Every "name" has a length with a maximum of 100 characters.
 Also, each "name" must be unique.
-	"description":
 Text field.
-	"ingredients": 
 Text field.
-	"cook_time": 
 Positive integer field.
-	"created_at": 
 Date time field.
 Every time a new record is created the current time of the creation of the record should be saved.
Apply all the migrations to the database.

5.	Product
Write a Django model called "Product" with the following parameters:
-	"name":
 Character field.
 Every "name" has a length with a maximum of 70 characters.
-	"description": 
 Text field.
-	"price": 
 Decimal field.
 Every "price" has a maximum of 10 digits and 2 decimal places.
-	"created_at": 
 Date time field.
 Every time a new record is created the current time of the creation of the record should be saved.
Apply all the migrations to the database.

6.	User Profile
Write a Django model called "UserProfile" with the following parameters:
-	"username": 
 Character field.
 Each "username" has a length with a maximum of 65 characters.
 Also, make the "username" unique.
-	"first_name": 
 Character field.
 Each "first_name" has a length with a maximum of 40 characters.
 Make the "first_name" unique.
-	"last_name": 
 Character field.
 Each "last_name" has a length with a maximum of 40 characters.
 Make the "last_name" unique.
-	"email": 
 Email field.
 Each "email" is unique,
 Set a default value – "students@softuni.bg".
-	"bio":
 Text field.
  Each "bio" has a length with a maximum of 120 characters.
-	"profile_image_url": 
 URL field.
-	"created_at": 
 Date time field.
 Every time a new record is created the current time of the creation of the record should be saved.
Apply all the migrations to the database.

7.	Exercise
Write a Django model called "Exercise" with the following parameters:
-	"name": 
 Character field.
 Each "name" has a length with a maximum of 100 characters.
-	"description": 
 Text field.
-	"difficulty_level": 
 Character field.
 Each "difficulty_level" has a length with a maximum of 20 characters.
-	"duration_minutes":
 Positive integer field.
-	"equipment": 
 Character field.
 Each "equipment" has a length with a maximum of 90 characters.
-	"video_url": 
 URL field. 
 This field is not required.
-	"calories_burned": 
 Positive integer field.
  The field has a default value of 0 (zero).
-	"is_favorite": 
 Boolean field.
 The field has a default value of "False".
Apply all the migrations to the database.

8.	*Book
Write a Django model called "Book" with the following parameters and register the model in the Django admin site.
-	"title": 
 Character field. 
 Each "title" has a length with a maximum of 30 characters.
-	"author" – 
 Character field. 
 Each "author" has a length with a maximum of 100 characters.
-	"genre": 
 Character field.
 Each "genre" has a length with a maximum of 20 characters.
 The choices are – "Fiction", "Non-Fiction", "Science Fiction", and "Horror".
-	"publication_date":
 Date field.
 The "date" should not be editable.
 Every time a new record is created the current time of the creation of the record should be saved.
-	"price": 
 Decimal field.
 Every "price" has a maximum of 8 digits and 2 decimal places.
-	"is_available":
 Boolean field.
 The default value of the field is "True".
-	"rating": 
 Float field.
-	"description": 
 Text field.
Apply all the migrations to the database.
Methods
__str__()
-	The "__str__()" method should return the "title" as a single string.
