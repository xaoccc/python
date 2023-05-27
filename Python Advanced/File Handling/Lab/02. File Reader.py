try:
    file = open("numbers.txt", "r")
    nums = file.readlines()
    for i in range(len(nums)):
        nums[i] = nums[i].replace("\n", "")
    result = [int(i) for i in nums]
    print(sum(result))
    file.close()
except FileNotFoundError:
    print("File not found")

