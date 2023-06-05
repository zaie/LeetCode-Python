dp[i]表示iii最少可以由几个平方数构成。

1 初试化dp=[0,1,2,⋯ ,n]，长度为n+1，最多次数就是全由1构成。

2 遍历dp，对于i，遍历区间[2,n+1)：
    遍历所有平方数小于i的数j，遍历区间[1,int(sqrt(i))+1)
        dp[i]=min(dp[i],dp[i−j∗j]+1)。始终保存所有可能情况中的最小值。
3 返回dp[n]

class Solution:
    def numSquares(self, n: int) -> int:
        dp=[i for i in range(n+1)]
        for i in range(2,n+1):
            for j in range(1,int(i**(0.5))+1):
                dp[i]=min(dp[i],dp[i-j*j]+1)
        return dp[-1]

作者：吴彦祖
链接：https://leetcode.cn/problems/perfect-squares/solutions/54142/dong-tai-gui-hua-bfs-zhu-xing-jie-shi-python3-by-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
                
