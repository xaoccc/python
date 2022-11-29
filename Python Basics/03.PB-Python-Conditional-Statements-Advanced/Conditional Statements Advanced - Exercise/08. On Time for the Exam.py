exam_hour = int(input())
exam_min = int(input())
arrival_hour = int(input())
arrival_min = int(input())

early = "Early"
on_time = "On time"
late = "Late"

exam_time = exam_hour*60 + exam_min
arrival_time = arrival_hour*60 + arrival_min
total_minutes_difference = exam_time - arrival_time
if total_minutes_difference == 0 :
    print(on_time)
elif total_minutes_difference > 30 :
    print(early)
    if total_minutes_difference < 60 :
        print(f"{total_minutes_difference} minutes before the start")
    elif total_minutes_difference >= 60 :
        total_hours_difference = total_minutes_difference // 60
        total_minutes_difference %= 60
        if total_minutes_difference < 10 :
            print(f"{total_hours_difference}:0{total_minutes_difference} hours before the start")
        else :
            print(f"{total_hours_difference}:{total_minutes_difference} hours before the start")
elif 30 >= total_minutes_difference >= 0 :
    print(on_time)
    print(f"{total_minutes_difference} minutes before the start")
elif total_minutes_difference < 0 :
    total_minutes_difference *= -1
    print(late)
    if total_minutes_difference < 60 :
        print(f"{total_minutes_difference} minutes after the start")
    elif total_minutes_difference >= 60 :
        total_hours_difference = total_minutes_difference // 60
        total_minutes_difference %= 60
        if total_minutes_difference < 10 :
            print(f"{total_hours_difference}:0{total_minutes_difference} hours after the start")
        else :
            print(f"{total_hours_difference}:{total_minutes_difference} hours after the start")

