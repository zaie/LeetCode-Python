状态定义：
设动态规划列表 dpdpdp ，dp[i]dp[i]dp[i] 代表前 iii 个房子在满足条件下的能偷窃到的最高金额。

转移方程：
设： 有 nnn 个房子，前 nnn 间能偷窃到的最高金额是 dp[n]dp[n]dp[n] ，前 n−1n-1n−1 间能偷窃到的最高金额是 dp[n−1]dp[n-1]dp[n−1] ，此时向这些房子后加一间房，此房间价值为 numnumnum ；
加一间房间后： 由于不能抢相邻的房子，意味着抢第 n+1n+1n+1 间就不能抢第 nnn 间；那么前 n+1n+1n+1 间房能偷取到的最高金额 dp[n+1]dp[n+1]dp[n+1] 一定是以下两种情况的 较大值 ：

不抢第 n+1n+1n+1 个房间，因此等于前 nnn 个房子的最高金额，即 dp[n+1]=dp[n]dp[n+1] = dp[n]dp[n+1]=dp[n] ；
抢第 n+1n+1n+1 个房间，此时不能抢第 nnn 个房间；因此等于前 n−1n-1n−1 个房子的最高金额加上当前房间价值，即 dp[n+1]=dp[n−1]+numdp[n+1] = dp[n-1] + numdp[n+1]=dp[n−1]+num ；
细心的我们发现： 难道在前 nnn 间的最高金额 dp[n]dp[n]dp[n] 情况下，第 nnn 间一定被偷了吗？假设没有被偷，那 n+1n+1n+1 间的最大值应该也可能是 dp[n+1]=dp[n]+numdp[n+1] = dp[n] + numdp[n+1]=dp[n]+num 吧？其实这种假设的情况可以被省略，这是因为：

假设第 nnn 间没有被偷，那么此时 dp[n]=dp[n−1]dp[n] = dp[n-1]dp[n]=dp[n−1] ，此时 dp[n+1]=dp[n]+num=dp[n−1]+numdp[n+1] = dp[n] + num = dp[n-1] + numdp[n+1]=dp[n]+num=dp[n−1]+num ，即两种情况可以 合并为一种情况 考虑；
假设第 nnn 间被偷，那么此时 dp[n+1]=dp[n]+numdp[n+1] = dp[n] + numdp[n+1]=dp[n]+num 不可取 ，因为偷了第 nnn 间就不能偷第 n+1n+1n+1 间。
最终的转移方程： 
dp[n+1] = max(dp[n],dp[n-1]+num)

初始状态：

前 000 间房子的最大偷窃价值为 000 ，即 dp[0]=0dp[0] = 0dp[0]=0 。
返回值：

返回 dpdpdp 列表最后一个元素值，即所有房间的最大偷窃价值。
简化空间复杂度：

我们发现 dp[n]dp[n]dp[n] 只与 dp[n−1]dp[n-1]dp[n−1] 和 dp[n−2]dp[n-2]dp[n−2] 有关系，因此我们可以设两个变量 cur和 pre 交替记录，将空间复杂度降到 O(1)O(1)O(1) 。

# 简化版
class Solution:
    def rob(self, nums: List[int]) -> int:
        cur, pre = 0, 0
        for num in nums:
            cur, pre = max(pre + num, cur), cur
        return cur
# 标准版    
class Solution:
    def rob(self, nums) -> int:
        n = len(nums)
        dp = [0]*(n+1)
        dp[1] = nums[0]
        for i in range(2,n+1):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i-1])
        return dp[-1]
# 作者：Krahets
# 链接：https://leetcode.cn/problems/house-robber/solutions/28242/da-jia-jie-she-dong-tai-gui-hua-jie-gou-hua-si-lu-/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
