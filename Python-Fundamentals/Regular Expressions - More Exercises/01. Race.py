import re
participants = input().split(", ")
all_data = {}
for i in participants:
    all_data[i] = 0
participant_pattern = r'[a-zA-Z]+'
result_pattern = r'[0-9]'
command = input()
while command != "end of race":
    current_participant = re.findall(participant_pattern, command)
    current_result = re.findall(result_pattern, command)
    current_result = [int(i) for i in current_result]
    for name in all_data:
        if name == "".join(current_participant):
            all_data[name] += sum(current_result)
            break
    command = input()
sorted_data = sorted(all_data.items(), key=lambda x: -x[1])
print(f"1st place: {sorted_data[0][0]}\n2nd place: {sorted_data[1][0]}\n3rd place: {sorted_data[2][0]}")
