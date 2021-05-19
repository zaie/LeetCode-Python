# 解题思路：
# 如果某一个作为 起跳点 的格子可以跳跃的距离是 3，那么表示后面 3 个格子都可以作为 起跳点。
# 可以对每一个能作为 起跳点 的格子都尝试跳一次，把 能跳到最远的距离 不断更新。
# 如果可以一直跳到最后，就成功了。


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        start, end = 0, 0
        
        while start <= end and end < len(nums):
            end = max(end, start + nums[start])
            start += 1
        return end >= len(nums) - 1
