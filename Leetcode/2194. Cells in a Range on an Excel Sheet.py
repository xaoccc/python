class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        import string
        alphabet = list(string.ascii_uppercase)
        output = []
        first_row = int(s[1])
        last_row = int(s[4])
        for i in range(len(alphabet)):
            if s[0] == alphabet[i]:
                first_col = i
                break
        for i in range(len(alphabet)):
            if s[3] == alphabet[i]:
                last_col = i
                break
        for j in range(first_col, last_col + 1):
            for k in range(first_row, last_row + 1): 
                output.append(alphabet[j]) 
                output[((j - first_col) * (last_row - first_row + 1)) + k - first_row] += str(k)
                if len(output[k - first_row-1]) > 1:
                    continue  
        return output
