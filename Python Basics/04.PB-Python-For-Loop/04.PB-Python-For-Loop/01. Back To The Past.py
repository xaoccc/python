#user input
money = float(input())
year = int(input())
#defining the year when he received the time machine and his age at that time
startyear = 1799
age = 17
#defining his expences 
expences = 0

#logic
#counting the years, as 1800 is the first year and he is 18 years old
for i in range (startyear, year) :
    startyear += 1
    age += 1
    #checking for even years and calculatin expences
    if startyear % 2 == 0:
        expences += 12000
    #checking for ogg age/yeas and calculatin expences. Here we can use also elif startyear != 0 as a condition, as the even/odd years are the same as our main character's
    if age % 2 != 0:
        expences += 12000 + (50 * age)

#print output
if expences <= money :
    print(f"Yes! He will live a carefree life and will have {(money-expences):.2f} dollars left." )
else :
    print(f"He will need {(expences-money):.2f} dollars to survive." )