import pandas as pd


# Solution 1:
def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    if len(logs) < 3:
        return pd.DataFrame({'ConsecutiveNums': []})

    if len(logs.drop_duplicates()) == 1:
        return logs.drop_duplicates()

    nums = []
    result = pd.DataFrame({'ConsecutiveNums': []})
    for index, num in logs.iterrows():
        nums.append(num.num)
    for i in range(len(nums)-2):
        if len(set(nums[i:i+3])) == 1:
            result.loc[len(result)] = [nums[i]]
    return result.drop_duplicates()

# Solution 2:
def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    if len(logs) < 3:
        return pd.DataFrame({'ConsecutiveNums': []})

    logs['match'] = (logs['num'] == logs['num'].shift(1)) & (logs['num'] == logs['num'].shift(2))
    result = logs.loc[logs['match'], ['num']].drop_duplicates().rename(columns={'num': 'ConsecutiveNums'})

    return result.drop_duplicates()