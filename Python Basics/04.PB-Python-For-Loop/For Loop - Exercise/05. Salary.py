#input
n = int(input())
salary = float(input())
face_tab = "Facebook"
insta_tab = "Instagram"
reddit_tab = "Reddit"
tab_open_sum1 = 0
tab_open_sum2 = 0
tab_open_sum3 = 0
penalty = 0
penalty1 = 0
penalty2 = 0
penalty3 = 0

#logic
for i in range (0, n) :
    open_tab = input()
    if open_tab == face_tab :
        tab_open_sum1 += 1 
        penalty1 = tab_open_sum1 * 150
    elif open_tab == insta_tab :
        tab_open_sum2 += 1 
        penalty2 = tab_open_sum2 * 100
    elif open_tab == reddit_tab :
        tab_open_sum3 += 1 
        penalty3 = tab_open_sum3 * 50
    penalty = penalty1 + penalty2 + penalty3
    if penalty > salary :
        break
#user output
if penalty >= salary :
    print("You have lost your salary.")
else :
    print(int(salary-penalty))