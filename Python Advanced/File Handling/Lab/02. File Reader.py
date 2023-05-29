# try:
#     with open("numbers.txt", "r") as file:
#         nums = file.readlines()
#         for i in range(len(nums)):
#             nums[i] = nums[i].replace("\n", "")
#         result = [int(i) for i in nums]
#         print(sum(result))
# except FileNotFoundError:
#     print("File not found")

try:
    with open("numbers.txt", "r") as file:
        print(sum([int(i) for i in file.read().split("\n")]))
except FileNotFoundError:
    print("File not found")