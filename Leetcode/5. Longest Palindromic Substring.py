class Solution:
    def longestPalindrome(self, s: str) -> str:
        list_len = len(s)
        palind = []

        def append_to_list(sublist):
            if not palind:
                palind.append(sublist)
            if len(palind[0]) < len(sublist):
                palind[0] = sublist

        def check_palindrome(sublist):
            if len(sublist) % 2 == 0:
                if sublist and sublist[:len(sublist) // 2] == sublist[len(sublist) // 2:][::-1]:
                    append_to_list(sublist)
            else:
                if sublist and sublist[:len(sublist) // 2] == sublist[1 + len(sublist) // 2:][::-1]:
                    append_to_list(sublist)

        for i in range(0, list_len):
            for j in range(i, list_len + 1):
                if s[i] == s[j - 1]:
                    check_palindrome(s[i:j])

        return palind[0]