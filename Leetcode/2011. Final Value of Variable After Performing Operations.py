class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        output = 0
        operator = 0
        for i in range(len(operations)):
            if operations[i] == "++X" or operations[i] == "X++":
                output += 1
            else:
                output -= 1
        return output
