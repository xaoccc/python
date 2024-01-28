# Task1 

Using libraries by your choice (hint - requests & BeautifulSoup4 libraries should do the job) write a Python script that:  
    
    a. Opens the following webpage: 'https://bnb.bg/Statistics/StInterbankForexMarket/index.htm'  

    b. Extracts the data_rows from the table named "Спот търговия на банките с чуждестранна валута срещу левове" into a list  

    c. Sorts the list in descending order by values in column 'обем продадени'  

    d. Saves the sorted list to a CSV file   

    e. Add the following functionality to the script - upon each run it should compare the latest downloaded table with the one saved in the CSV file and rewrites the CSV file only if the tables are different.  


# Task2

Using libraries by your choice (hint - requests & BeautifulSoup4 libraries should do the job) write a Python script that:
    
    a. Opens the following webpage: 'https://en.wikipedia.org/wiki/List_of_European_Union_member_states_by_population'

    b. Extracts the data_rows from the table named "List of European Union member states by population" 

    c. Using values from columns 'Country' and 'Official figure' it should create a countries_dictionary variable with a structure:
```
{country1:{'population': official figure1}, country2:{'population': official figure2}, etc.} 
```

for example -> {'Germany': {'country_population': 83237124}, 'France': {'country_population': 67874000},
 'Italy': {'country_population': 58906742}, etc.} 

    d. Sums country_population values for all countries in the dictionary to get the total_country_population and calculates for each country its country_population_percentage from the total_country_population;
then adds this country_population_percentage to the countries_dictionary; 
finally prints the countries_dictionary and it should look similar to:
```
{'Germany': {  
            'country_population': 83237124,
            'country_population_percentage': 18.5
      },
      'France': {  
            'country_population': 67874000,
            'country_population_percentage': 15
      },
      'Italy': {  
            'country_population': 58906742,
            'country_population_percentage': 13.3
      }, 
}
```