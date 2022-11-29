#user input
exam_hour = int(input())
exam_min = int(input())
arrival_hour = int(input())
arrival_min = int(input())

early = "Early"
on_time = "On time"
late = "Late"
output = ""

#logic
#We turn hours into minutes
exam_time = exam_hour * 60 + exam_min
arrival_time = arrival_hour * 60 + arrival_min
time_diff = exam_time - arrival_time

#We check for the first simple conditions/output - late, early or on time
if time_diff > 30:
    print("Early")
elif time_diff < 0:
    print("Late")
else:
    print("On time")
#We define 2 variables for the output, as we turn the minutes into a positive number
hours = 0
minutes = abs(time_diff)
#We turn back muntes over and equal to 60 to hours and the rest remain as minutes
if minutes >= 60:
    hours = minutes // 60
    minutes %= 60
#here are the variables for the first part of the second output:
if hours > 0:
    output += str(hours) + ":" + ("0" + str(minutes) if minutes < 10 else str(minutes)) + " hours"
#the output if hours (minutes // 60) are < 1
else :
    output += str(minutes) + " minutes"
#Here we add the second part of the second output
if time_diff > 0:
    output += " before the start"
else:
    output += " after the start"
#output
print(output)
    






