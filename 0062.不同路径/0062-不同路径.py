# 数学解法：排列组合
# 因为机器到底右下角，向下几步，向右几步都是固定的，
# 比如，m=3, n=2，我们只要向下 1 步，向右 2 步就一定能到达终点。
# 所以有 C_{m+n-2}^{m-1}

def uniquePaths(self, m: int, n: int) -> int:
        return int(math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1))

# 动态规划
# 动态方程：dp[i][j] = dp[i-1][j] + dp[i][j-1]
# 注意，对于第一行 dp[0][j]，或者第一列 dp[i][0]，由于都是在边界，所以只能为 1
# 时间复杂度：O(m*n)O(m∗n)
# 空间复杂度：O(m * n)O(m∗n)
# 优化：因为我们每次只需要 dp[i-1][j],dp[i][j-1]

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n] + [[1]+[0] * (n-1) for _ in range(m-1)]
        #print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
