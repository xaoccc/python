#input
budget = float(input())
actor_salary_sum = 0
current_budget = 0
#logic
while budget > actor_salary_sum:
    actor_name = input()
    if actor_name == "ACTION":
        break
    current_budget = budget - actor_salary_sum
    if len(actor_name) <= 15:
        actor_salary = float(input())
    else:
        actor_salary = current_budget * 0.2
    actor_salary_sum += actor_salary
#output
if budget >= actor_salary_sum :
    print(f"We are left with {budget - actor_salary_sum:.2f} leva.")
else:
    print(f"We need {actor_salary_sum - budget:.2f} leva for our actors.")
