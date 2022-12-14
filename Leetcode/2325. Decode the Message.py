class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        import string
        alphabet = string.ascii_uppercase
        optimal_key = "".join(dict.fromkeys(key)).replace(" ", "")
        for i in range(26):
            message = message.replace(optimal_key[i], alphabet[i])
        return message.lower()
