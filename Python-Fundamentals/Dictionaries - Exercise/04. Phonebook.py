contact_data = input()
contact_book = {}

while "-" in contact_data:
    contact_data = contact_data.split("-")
    contact_book[contact_data[0]] = contact_data[1]
    
    contact_data = input()
for i in range(int(contact_data)):
    contact_search = input()
    if contact_search in contact_book:
       print(f"{contact_search} -> {contact_book[contact_search]}")
    else: 
        print(f"Contact {contact_search} does not exist.")
