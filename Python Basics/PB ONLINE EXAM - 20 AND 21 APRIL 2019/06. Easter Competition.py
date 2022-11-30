easter_bread_num = int(input())
max_pts = 0
best_baker = "" 
 
for i in range(easter_bread_num):
    baker_name = input()
    total_pts = 0
    while True:
        review = input()
        if review == "Stop":
            print(f"{baker_name} has {total_pts} points.")
            if max_pts < total_pts:
                max_pts = total_pts
                best_baker = baker_name
                print(f"{best_baker} is the new number 1!")
            break
        total_pts += int(review)
 
print(f"{best_baker} won competition with {max_pts} points!")
