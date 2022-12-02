class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words_num = 0
        for i in range(len(sentences)):
            if sentences[i].count(' ') + 1> max_words_num:
                max_words_num = sentences[i].count(' ') + 1        
        return max_words_num  
