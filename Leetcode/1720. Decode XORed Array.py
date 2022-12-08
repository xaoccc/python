#Explanation: If encoded = [1,2,3], first = 1 , so:
#arr= [first, first XOR encoded[0], encoded[1] XOR encoded[1], encoded[2] XOR encoded[2]] = [1, 1^1, 0^2, 2^3] = [1,0,2,1]
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = []
        arr.append(first)
        for i in range(0, len(encoded)):
            #XOR returns the bitwise sum of two integers. The XOR operator is "^". 
            arr.append(encoded[i] ^ arr[i])
        return arr
