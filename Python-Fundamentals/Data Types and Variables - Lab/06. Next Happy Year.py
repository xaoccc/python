#works in pycharm with all test cases

year = int(input())
while len(set(str(year))) != len(str(year)):
  year += 1
print(year)
