class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = deque(sorted(piles))

        coins = 0
        while piles:
            piles.pop()
            piles.popleft()
            coins += piles.pop()
        return coins
