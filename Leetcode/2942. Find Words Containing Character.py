class Solution(object):
    def findWordsContaining(self, words, x):
        return [i for i in range(0, len(words)) if x in words[i]]