# 倒推一下，假设当前位于第 n 阶，那么上一步可能在第 n-1 或者第 n-2 阶，分别需要爬 1 级台阶和 2 级台阶。
# 那么，f(n) = f(n-1) + f(n-2)，

class Solution(object):
    # 一维dp，自底向上
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]

        
