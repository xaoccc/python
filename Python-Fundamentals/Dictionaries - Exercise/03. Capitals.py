countries = input().split(", ")
cities = input().split(", ")
dictionary = {key:value for (key,value) in list(zip(countries, cities))}
for (key, value) in dictionary.items():
    print(f"{key} -> {value}")
