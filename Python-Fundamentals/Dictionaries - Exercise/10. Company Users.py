command = input()
companies_data = {}

while command != "End":
    command = command.split(" -> ")
    company_name = command[0]
    employee_id = command[1]
    if company_name not in companies_data:
        companies_data[company_name] = []
    if employee_id not in companies_data[company_name]:
        companies_data[company_name].append(employee_id)
    command = input()

for (key, value) in companies_data.items():
    print(key)
    for i in companies_data[key]:
        print(f"-- {i}")
