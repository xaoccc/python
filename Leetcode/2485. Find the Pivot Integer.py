class Solution:
    def pivotInteger(self, n: int) -> int:
        pivot_list = []
        for i in range(1, n+1):
            pivot_list.append(i)

        result = -1

        for i in range(len(pivot_list)):
            if sum(pivot_list[:i+1]) == sum(pivot_list[i:]):
                result = i + 1
                break

        return result
