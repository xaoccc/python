import re
destinations = input()
pattern = r"([\=\/])(?P<destination>[A-Z][a-zA-Z]{2,})\1"
dest = re.finditer(pattern, destinations)
dest_list, travel_pts = [], 0
for i in dest:
    dest_list.append(i["destination"])
    travel_pts += len(i["destination"])
print(f"Destinations: {', '.join(dest_list)}\nTravel Points: {travel_pts}")
