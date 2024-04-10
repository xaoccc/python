from collections import deque

class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ["a", "e", "o", "i", "u"]
        vowels_found = deque(sorted([ord(l) for l in s if l.lower() in vowels]))
        return "".join([l if l.lower() not in vowels else chr(vowels_found.popleft()) for l in s])
