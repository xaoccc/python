def math_operations(*nums, **actions):
    result = ""
    action_num = 1
    for i in range(len(nums)):
        if action_num == 1:
            actions["a"] += nums[i]
        elif action_num == 2:
            actions["s"] -= nums[i]
        elif action_num == 3 and nums[i] != 0:
            actions["d"] /= nums[i]
        elif action_num == 4:
            actions["m"] *= nums[i]
        action_num += 1    
        if action_num == 5:
            action_num = 1
        
    actions = dict(sorted(actions.items(), key=lambda x: (-x[1], x[0])))
    for key, value in actions.items():
        result += f"{key}: {value:.1f}\n"
    return result

