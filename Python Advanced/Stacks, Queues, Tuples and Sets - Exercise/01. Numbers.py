nums_one = set([int(i) for i in input().split()])
nums_two = set([int(i) for i in input().split()])
n = int(input())

for i in range(n):
    command = [int(i) if i.isdigit() else i for i in input().split()]
    if command[0] == "Add":
        if command[1] == "First":
            nums_one = nums_one | set(command[2:])
        elif command[1] == "Second":
            nums_two = nums_two | set(command[2:])
    elif command[0] == "Remove":
        if command[1] == "First":
            nums_one = nums_one - set(command[2:])
        elif command[1] == "Second":
            nums_two = nums_two - set(command[2:])
    elif command[0] == "Check":
        if nums_one < nums_two or nums_one > nums_two:
            print(True)
        else:
            print(False)
nums_one = sorted(nums_one)
nums_two = sorted(nums_two)
print(", ".join([str(i) for i in nums_one]))
print(", ".join([str(i) for i in nums_two]))


# nums_one = set([int(i) for i in input().split()])
# nums_two = set([int(i) for i in input().split()])
# n = int(input())
#
# for i in range(n):
#     first_command, second_command, *data = input().split()
#
#     command = first_command + " " + second_command
# todo with dict
