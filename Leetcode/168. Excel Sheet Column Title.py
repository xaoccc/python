class Solution(object):
    def convertToTitle(self, columnNumber):
        import string
        column_name = ""
        #We write -1, due to the 1-based excel numbering (A = 1, not A = 0)
        remaining_letters = columnNumber - 1
        alphabet = list(string.ascii_uppercase)
 
        while remaining_letters >= 0:
            #Here we define the last letter of the column name
            column_name = alphabet[remaining_letters % 26] + column_name
            #Here we define every next letter of the name backwards
            remaining_letters = (remaining_letters // 26) - 1
        return column_name
