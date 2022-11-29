juri_n = int(input())
sum_mark = 0
avg_mark = 0
avg_mark_num = 0
avg_mark_sum = 0
avg_mark_all = 0

while True:
    presentation_name = input()
    if presentation_name == "Finish":
        print(f"Student's final assessment is {avg_mark_all:.2f}." )
        break
    for j in range(juri_n):
        mark = float(input())
        sum_mark += mark
        
    avg_mark = sum_mark / juri_n
    avg_mark_num += 1
    avg_mark_sum += avg_mark
    avg_mark_all = avg_mark_sum / avg_mark_num
    print(f"{presentation_name} - {avg_mark:.2f}.")
    sum_mark = 0