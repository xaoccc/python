import time


while True:
    num = ""
    output = ""
    time_one = time.time()
    text = input()
    time_two = time.time()
    if time_two - time_one > 10:
        print("Waited too long, exiting now...")
        break
    for i in range(len(text)):
        if text[i].isdigit():
            num += text[i]
            if i == len(text) - 1:
                output += num + " "
                print(num)
        else:
            if num != "":
                print(num)
                output += num + " "
                num = ""

print(output) 
