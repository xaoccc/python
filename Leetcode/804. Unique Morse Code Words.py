class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        import string
        morse_list = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
                    ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        alphabet = list(string.ascii_lowercase)
        morse_letter = ""
        morse_words = []
        for i in range(len(words)):

            morse_letter = ""
            for letter in range(len(words[i])):

                for j in range(26):
                    if words[i][letter] == alphabet[j]:
                        morse_letter += morse_list[j]
            morse_words.append(morse_letter)
        return len(set(morse_words))
