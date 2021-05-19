# 动态规划转移方程：
# f(i)=max{f(i−1)+nums[i],nums[i]}


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [0 for _ in nums]
        dp[0] = nums[0]
        
        for i, x in enumerate(nums):
            if i:
                if dp[i - 1] > 0:
                    dp[i] = max(dp[i - 1] + x, dp[i])
                else:
                    dp[i] = x
                    
        return max(dp)
