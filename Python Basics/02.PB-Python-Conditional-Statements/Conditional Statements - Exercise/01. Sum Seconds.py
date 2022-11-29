#input
time_first = int(input())
time_second = int(input())
time_third = int(input())

#logic
total_time = time_first + time_second + time_third
minutes = total_time // 60
seconds = total_time % 60

#output
if seconds < 10 :
    print (f'{minutes}:0{seconds}')
else :
    print (f'{minutes}:{seconds}')
    
#output 2
if seconds < 10 :
    seconds = "0" + str(seconds)
else :
    seconds = seconds
print (f'{minutes}:{seconds}')
