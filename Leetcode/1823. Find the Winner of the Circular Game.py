class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [1 + i for i in range(n)]
        i = 0
        while len(friends) > 1:
            if i + k >= len(friends):
                i = (i + k - 1) % len(friends)
            else:
                i += k - 1
            friends.pop(i)
        return friends[0]