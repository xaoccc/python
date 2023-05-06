class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = []
           
        for i in range(len(boxes)):
            moves = 0
            if boxes[i] == "0":
                for j in range(len(boxes)):
                    if int(boxes[j]) - int(boxes[i]) == 1 and i != j:
                        moves += abs(j - i)
            elif boxes[i] == "1":
                for j in range(len(boxes)):
                    if int(boxes[j]) - int(boxes[i]) == 0 and i != j:
                        moves += abs(j - i)
        
            result.append(moves)
        return result
