#input
actor_name = input()
acad_pts = float(input())
n = int(input())
pts_sum = 0
 
#logic
for i in range (0, n) :
    judge_name = input()
    judge_pts = float(input())
    judge_name_pts = len(judge_name)
    pts_sum += (judge_name_pts * judge_pts / 2)
    total_pts = pts_sum + acad_pts
    if total_pts > 1250.5 :
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_pts:.1f}!")
        break
if total_pts <= 1250.5 :
        print(f"Sorry, {actor_name} you need {(1250.5-total_pts):.1f} more!")
