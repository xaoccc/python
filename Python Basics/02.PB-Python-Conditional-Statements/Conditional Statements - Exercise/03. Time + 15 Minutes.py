hours = int(input())
minutes = int(input())

if hours < 24 and minutes < 45 :
    minutes = minutes + 15
    print(f'{hours}:{minutes}')
elif hours < 23 and minutes >= 45 and minutes < 55 :
    hours = hours + 1
    minutes = minutes + 15
    print(f'{hours}:0{minutes % 60}')
elif hours < 23 and minutes >= 55 and minutes < 60 :
    hours = hours + 1
    minutes = minutes + 15
    print(f'{hours}:{minutes % 60}')
elif hours == 23 and minutes >= 45 and minutes < 55 :
    hours = 0
    minutes = minutes + 15
    print(f'{hours}:0{minutes % 60}')
elif hours == 23 and minutes >= 55 and minutes < 60 :
    hours = 0
    minutes = minutes + 15
    print(f'{hours}:{minutes % 60}')
