#user input
days_off = int(input())
play_time_limit = 30000
days_off_play_time = 127
workdays_play_time = 63

#logic
if play_time_limit <= (days_off_play_time * days_off) + ((365 - days_off) * workdays_play_time) :
    time_more = ((days_off_play_time * days_off) + ((365 - days_off) * workdays_play_time)) - play_time_limit
    time_more_hours = time_more // 60
    time_more_minutes = time_more % 60
    print ("Tom will run away")
    print(f"{time_more_hours} hours and {time_more_minutes} minutes more for play")
else :
    time_less = play_time_limit - ((days_off_play_time * days_off) + ((365 - days_off) * workdays_play_time))
    time_less_hours = time_less // 60
    time_less_minutes = time_less % 60
    print ("Tom sleeps well")
    print(f"{time_less_hours} hours and {time_less_minutes} minutes less for play")