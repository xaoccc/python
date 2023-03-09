sometext = input()
while sometext != "end":
    print(f"{sometext} = {''.join(list(reversed(sometext)))}")
    sometext = input()

    
# sometext = input()
# while sometext != "end":
#     print(f"{sometext} = {sometext[::-1]}")
#     sometext = input()
