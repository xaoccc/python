class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for j in range(len(accounts)):
            
            current_wealth = 0
            for i in range(len(accounts[0])):
                current_wealth += accounts[j][i]
                if current_wealth > max_wealth:
                    max_wealth = current_wealth
        return max_wealth
