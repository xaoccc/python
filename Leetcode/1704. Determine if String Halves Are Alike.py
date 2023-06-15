class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        first_half, second_half = 0, 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        for i in range(len(s)):
            if i < len(s) / 2:
                if s[i] in vowels:
                    first_half += 1
            else:
                if s[i] in vowels:
                    second_half += 1
        return first_half == second_half
