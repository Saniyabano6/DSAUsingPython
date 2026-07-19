class Solution(object):
    def climbStairs(self, n):
        memo={}
        def dfs(i):
            if i<=2:
                return i
            if i not in memo:
                memo[i]=dfs(i-1)+dfs(i-2)
            return memo[i]
        return dfs(n)
            
            