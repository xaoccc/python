class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        result = [0] * k
        uam = {}
        for i in logs:
            if i[0] not in uam:
                uam[i[0]] = []
            uam[i[0]].append(i[1])
        for minutes in uam.values():
            result[len(set(minutes)) - 1] += 1
        return result
