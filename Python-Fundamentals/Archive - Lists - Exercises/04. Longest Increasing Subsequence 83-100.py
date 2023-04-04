nums = [int(i) for i in input().split()]
def longest_increasing_subsequence(nums):
    n = len(nums)
    # Initialize the memoization table with all 1's
    dp = [1] * n
    # Compute LIS values for all indices i and j
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    # Find the maximum LIS value and its index
    max_len, max_idx = 0, 0
    for i in range(n):
        if dp[i] > max_len:
            max_len = dp[i]
            max_idx = i
    # Backtrack to reconstruct the LIS
    lis = [nums[max_idx]]
    for i in range(max_idx - 1, -1, -1):
        if nums[i] < nums[max_idx] and dp[i] == dp[max_idx] - 1:
            lis.append(nums[i])
            max_idx = i
    lis.reverse()
    return lis
print(*longest_increasing_subsequence(nums))
