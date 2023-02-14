input_data = input()
global_data = []

while input_data != "make migrations":
    if "." not in input_data:
        break
    input_data = input_data.split(".")
    person_data = []
    all_data = ["Name of the person: ", "Age of the person: ", "Birthdate of the person: "]
    del input_data[-1]
    for i in range(3):
        person_data.append(input_data[i].split(" "))
    if person_data[0][-2][0].isupper() and person_data[0][-1][0].isupper() and person_data[0][-2].isalpha() and person_data[0][-1].isalpha() and 9 < int(person_data[1][3]) < 100 and person_data[2][-1][2] == "-" and person_data[2][-1][5] == "-" and person_data[0][-3] == "is" and len(person_data[0][-1]) > 1:
        all_data[0] += person_data[0][-2] + " " + person_data[0][-1] + "."
        all_data[1] += person_data[1][3] + "."
        all_data[2] += person_data[2][-1] + "."
        global_data.append(all_data)

    input_data = input()
    
if not global_data:
    print("DB is empty")
for i in range(len(global_data)):
    print("\n".join(global_data[i]))
