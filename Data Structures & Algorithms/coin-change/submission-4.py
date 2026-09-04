class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [-1] * (amount + 1)

        def dfs(current):
            if current == amount:
                return 0
            if current > amount:
                return float('inf')
            
            if memo[current] != -1:
                return memo[current]

            res = float('inf')
            for coin in coins:
                res = min(res, 1 + dfs(current + coin)) 
            memo[current] = res
            return res
        
        return -1 if dfs(0) == float('inf') else dfs(0)


        
