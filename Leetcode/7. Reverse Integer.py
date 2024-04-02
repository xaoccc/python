class Solution:
    def reverse(self, x: int) -> int:

        x_str = str(x)
        if x_str[0] == "-":
            result = int("-" + x_str[1:][::-1])
            if result < -2 ** 31:
                return 0
            return result

        result = int(x_str[::-1])
        if result > 2 ** 31 - 1:
            return 0
        return result
