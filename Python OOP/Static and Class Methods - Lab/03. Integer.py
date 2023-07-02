from math import floor


class Integer:
    def __init__(self, value):
        self.value = value

    def from_float(self, float_value):
        if type(float_value) != float:
            return "value is not a float"
        self.value = floor(float_value)

    def from_roman(self, value):
        if type(value) != str:
            return "wrong type"
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
                 'CD': 400, 'CM': 900}
        i = 0
        num = 0
        while i < len(value):
            if i + 1 < len(value) and value[i:i + 2] in roman:
                num += roman[value[i:i + 2]]
                i += 2
            else:

                num += roman[value[i]]
                i += 1
        self.value = value

first_num = Integer(10)
print(first_num.value)
second_num = Integer.from_roman("IV")
print(second_num.value)

