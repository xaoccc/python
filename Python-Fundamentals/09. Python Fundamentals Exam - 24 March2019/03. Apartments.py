import re
blocks_data = {}
all_data = {}
blocks = []
pattern = r"(?P<hood>[a-zA-Z0-9]+)&(?P<block>[0-9]+) -> (?P<ap_num>[1-9][0-9]*)\|(?P<price>[1-9][0-9]*)"
collect = input()
while collect != "collectApartments":
    collect = collect.split(" -> ")
    neighbourhood = collect[0]
    blocks = list(set([int(i) for i in collect[1].split(",")]))
    if neighbourhood not in blocks_data.keys():
        blocks_data[neighbourhood] = blocks
    else:
        for block in blocks:
            if block not in blocks_data[neighbourhood]:
                blocks_data[neighbourhood].append(block)
    collect = input()
    
for i in blocks_data:
    blocks_data[i] = sorted(blocks_data[i])
    
command = input()
while command != "report":
    match = re.finditer(pattern, command)
    for i in match:
        if i["hood"] in blocks_data.keys():
            if int(i["block"]) in blocks_data[i["hood"]]:
                if i["hood"] in all_data.keys():
                    all_data[i["hood"]][int(i["block"])] = [i["ap_num"], i["price"]]
                else:
                    all_data[i["hood"]] = {int(i["block"]): [i["ap_num"], i["price"]]}
                    
    command = input()

blocks_data = dict(sorted(blocks_data.items(), key=lambda x: x[0]))

for neighbourhood, block in blocks_data.items():
    print(f"Neighborhood: {neighbourhood}")
    if neighbourhood in all_data.keys():
        for i in block:
            if i in all_data[neighbourhood].keys():
                print(f"* Block number: {i} -> {all_data[neighbourhood][i][0]} apartments for sale. Price for one: {all_data[neighbourhood][i][1]}")
            else:
                print(f"* Block number: {i} -> 0 apartments for sale. Price for one: None")
    else:
        for i in block:
            print(f"* Block number: {i} -> 0 apartments for sale. Price for one: None")
