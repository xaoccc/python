class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:

        global_score = []
        result = []
        for i in range(len(score)):
            new_score = []
            new_score.append(score[i][k])
            new_score.append(score[i])
            global_score.append(new_score)
        global_score = list(sorted(global_score))
        global_score.reverse()
        for i in range(len(global_score)):
            result.append(global_score[i][1])
        return result
