import re
payneer = {}
command = input()
pattern = r"(?P<singer>.+) @(?P<place>[\w ]+) (?P<ticket_price>\d+) (?P<ticket_count>\d+)"

while command != "End":
    
    match = re.finditer(pattern, command)
    for i in match:
        if i["place"] not in payneer:
            payneer[i["place"]] = {i["singer"]: int(i["ticket_price"]) * int(i["ticket_count"])}
        else:
            if i["singer"] not in payneer[i["place"]]:
                payneer[i["place"]][i["singer"]] = int(i["ticket_price"]) * int(i["ticket_count"])
            else:
                payneer[i["place"]][i["singer"]] += int(i["ticket_price"]) * int(i["ticket_count"])

    command = input()
    
for chalga in payneer:
    payneer[chalga] = dict(sorted(payneer[chalga].items(), key=lambda x: -x[1]))
    
for chalga in payneer:
    print(chalga)
    for key, value in payneer[chalga].items():
        print(f"#  {key} -> {value}")
