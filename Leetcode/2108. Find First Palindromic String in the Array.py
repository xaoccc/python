class Solution(object):
    def firstPalindrome(self, words):
        found = False
        for word in words:
            if len(word) % 2 == 0:
                if word[ :len(word)//2] == word[len(word) // 2: ][::-1]:
                    found = True
                    return word
                    break

            else:
                if word[:len(word) // 2] == word[(len(word)// 2) + 1: ][::-1]:
                    found = True
                    return word
                    break
        if not found:
            return ""