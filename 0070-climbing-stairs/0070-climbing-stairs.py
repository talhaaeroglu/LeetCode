class Solution:
    memo = {}
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.helper(n, memo)
        
    def helper(self, n: int, memo: {}):
        if n == 1 or n == 0:
            return 1
        else:
            if n not in memo:
                memo[n] = self.helper(n-1, memo) + self.helper(n-2, memo)
            return memo[n]