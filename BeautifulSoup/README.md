# Task1 

Using libraries by your choice (hint - requests & BeautifulSoup4 libraries should do the job) write a Python script that:  
    a. Opens the following webpage: 'https://bnb.bg/Statistics/StInterbankForexMarket/index.htm'  

    b. Extracts the data_rows from the table named "Спот търговия на банките с чуждестранна валута срещу левове" into a list  

    c. Sorts the list in descending order by values in column 'обем продадени'  

    d. Saves the sorted list to a CSV file   

    e. Add the following functionality to the script - upon each run it should compare the latest downloaded table with the one saved in the CSV file and rewrites the CSV file only if the tables are different.  
