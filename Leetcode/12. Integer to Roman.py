class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""
        roman = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }

        if num in roman.keys():
            return roman[num]

        while num > 0:
            for key, value in roman.items():
                if num >= key:
                    result += value * (num // key)
                    num %= key

        return result
