class Solution(object):
    def reversePrefix(self, word, ch):
        if ch in word:
            return "".join(list(reversed(word[:word.index(ch)+1]))) + word[word.index(ch)+1: ]
        else:
            return word