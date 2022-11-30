class Solution:
    def generate(self, numRows: int) -> List[List[int]]:   
        outer_list = []
        inner_list = []
        for i in range(0, numRows): 
            if i == 0:
                inner_list = [1]
                outer_list.append(inner_list)
                continue
            elif i == 1:
                inner_list = [1,1]
                outer_list.append(inner_list)
                continue 
            else:
                inner_list = []
                for j in range(0, i + 1):
                    if j == 0 or j == i:
                        current_num = 1
                    else:
                        current_num = outer_list[i-1][j-1] + outer_list[i-1][j]
                    inner_list.append(current_num) 
                outer_list.append(inner_list)                
        return outer_list
