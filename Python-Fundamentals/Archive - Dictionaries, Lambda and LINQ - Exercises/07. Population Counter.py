command = input()
all_data = {}
country_data = {}

while command != "report":
    city = command.split("|")[0]
    country = command.split("|")[1]
    popul = int(command.split("|")[2])
    if country not in all_data.keys():
        all_data[country] = {city: popul}
    else:
        all_data[country][city] = popul
    command = input()

for i in all_data:
    country_data[i] = sum(all_data[i].values())  
country_data = dict(sorted(country_data.items(), key=lambda x: -x[1]))  

for c in all_data:
    all_data[c] = dict(sorted(all_data[c].items(), key=lambda x: -x[1]))
    
for key, value in country_data.items():
    flag = False   
    print(f"{key} (total population: {value})")
    for test in all_data.items():
        if flag:
            break
        for key1, value1 in all_data[key].items():
            print(f"=>{key1}: {value1}")
            flag = True
