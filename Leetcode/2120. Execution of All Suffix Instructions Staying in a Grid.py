class Solution(object):
    def executeInstructions(self, n, startPos, s):
        """
        :type n: int
        :type startPos: List[int]
        :type s: str
        :rtype: List[int]
        """
        result = []
        start = []
        for i in startPos:
            start.append(i)

        movement = {
            "R": (1, 0),
            "L": (-1, 0),
            "U": (0, -1),
            "D": (0, 1)
        }
        for i in s:
            moves_num = 0
            for i in s:
                if i in "RL":
                    if 0 <= startPos[1] + movement[i][0] < n:
                        moves_num += 1
                        startPos[1] += movement[i][0]
                    else:
                        break
                elif i in "UD":
                    if 0 <= startPos[0] + movement[i][1] < n:
                        moves_num += 1
                        startPos[0] += movement[i][1]
                    else:
                        break
            startPos = []
            for i in start:
                startPos.append(i)
            s = s[1:]
            result.append(moves_num)
        return result