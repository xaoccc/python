sometext = input()
while sometext != "end":
    print(f"{sometext} = {''.join(list(reversed(sometext)))}")
    sometext = input()
