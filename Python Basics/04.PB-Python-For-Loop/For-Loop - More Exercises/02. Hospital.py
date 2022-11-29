#user input
days_in_hospital = int(input())
untreated_patients = 0
examined_patients = 0
current_day = 0
doc = 7

#logic
for day in range (1, days_in_hospital + 1) :
    patients_num = int(input())
    current_day += 1
    if day % 3 == 0 and untreated_patients >  examined_patients :
        doc += 1
    if patients_num > doc :
        untreated_patients += (patients_num - doc)
        examined_patients += doc
    else :
        examined_patients += patients_num


print(f"Treated patients: {int(examined_patients)}.")
print(f"Untreated patients: {int(untreated_patients)}.")