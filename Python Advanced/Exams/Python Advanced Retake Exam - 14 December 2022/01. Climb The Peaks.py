from collections import deque
food, stamina = deque([int(i) for i in input().split(", ")]), deque([int(i) for i in input().split(", ")])
climbed_peaks = []

peaks = deque([("Vihren", 80), ("Kutelo", 90), ("Banski Suhodol", 100), ("Polezhan",	60), ("Kamenitza", 70)])
    
day = 1
while food and stamina:
    sum_food_stamina = food.pop() + stamina.popleft()
    if sum_food_stamina >= peaks[0][1]:
        climbed_peaks.append(peaks[0][0])
        peaks.popleft()

    if not peaks:
        print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
        break 
    if not food or not stamina or day == 7:
        print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
        break
    

    day += 1
if climbed_peaks:
    print("Conquered peaks:")
    for peak in climbed_peaks:
        print(peak)
