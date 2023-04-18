nums = tuple(map(float, input().split()))
nums_count = {}
for num in nums:
    if num not in nums_count:
        nums_count[num] = 0
    nums_count[num] += 1
for num, count in nums_count.items():
    print(f"{num} - {count} times")
