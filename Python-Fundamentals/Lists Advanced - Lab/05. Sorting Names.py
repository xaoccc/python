names = input().split(", ")

#The simplest way is to use the built-in function lambda inside the function sorted(), 
#lambda has 1 parameter "name" and returns the sorted list, first by name in decsending order "-len(name)", then alphabetically "name"
#That way we can sort easily by various indications

names_sorted_list = sorted(names, key=lambda name: (-len(name), name))

print(names_sorted_list)
