class Solution:
    def minimumSum(self, num: int) -> int:
        num = str(num)
        min_sum = 9999
        
        if num[2] == "0" and num[3] == "0":
            min_sum = int(num[0]) + int(num[1])
            return min_sum
        elif num[1] == "0" and num[2] == "0":
            min_sum = int(num[0]) + int(num[3])
            return min_sum 
        else:
            for i in range(4):
                for j in range(4):
                    if i == j:
                        continue
                    for k in range(4):
                        if i == k or j == k:
                            continue
                        for l in range(4):
                            if i == l or j == l or k == l:
                                continue
                            if int(num[i] + num[j]) + int(num[k] + num[l]) < min_sum:
                                min_sum = int(num[i] + num[j]) + int(num[k] + num[l])
            
        return min_sum
