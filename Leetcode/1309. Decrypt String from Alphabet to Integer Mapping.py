class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        import string

        alphabet = list(string.ascii_lowercase)
        alphabet = alphabet[9:]
        code = ["10#", "11#", "12#", "13#", "14#", "15#", "16#", "17#", "18#",
                "19#", "20#", "21#", "22#", "23#", "24#", "25#", "26#"]
        message = ""
        new_s = ""

        for i in range(len(code)):
            if code[i] in s:
                new_s = s.replace(code[i], alphabet[i])
                s = new_s
        new_alphabet = list(string.ascii_lowercase)
        new_alphabet = new_alphabet[:9]
        new_code = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        print(new_alphabet)

        for i in range(len(new_code)):
            if new_code[i] in s:
                new_s = s.replace(new_code[i], new_alphabet[i])
                s = new_s
        return new_s
