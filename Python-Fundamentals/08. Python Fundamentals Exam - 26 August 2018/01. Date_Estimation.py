import datetime

date = input().split("-")
for i in range(len(date)):
    date[i] = int(date[i].lstrip('0'))

day = datetime.date(2018,8,26)
future = datetime.date(date[0],date[1],date[2])
diff = future - day

if diff.days == 0:
    print("Today date")
elif diff.days > 1:
    print (f"{diff.days+1} days left")
else:
    print("Passed")
