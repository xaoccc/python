def operate(*nums):
    def divide():
        result = nums[1]
        for i in range(2, len(nums)):
            result /= nums[i]
        return result
        
    def subtract():
        result = nums[1]
        for i in range(2, len(nums)):
            result -= nums[i]
        return result
        
    def multiply():
        result = nums[1]
        for i in range(2, len(nums)):
            result *= nums[i]
        return result
            
    calculate = {
        "+": sum(nums[1:]),
        "*": multiply(), 
        "/": divide(),
        "-": subtract()
    }
    return calculate[nums[0]]

print(operate("*", 3, 2, 5))
