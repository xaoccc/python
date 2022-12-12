class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps_count = 0
        while num > 0:
            if num % 2 == 0:
                num /= 2
                steps_count += 1
            else:
                num -= 1
                steps_count += 1
        return steps_count
