# 双指针滑动，交换非零元素和零元素的位置
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 循环遍历数组，当遇到非零元素则开始交换慢指针所指的0元素
        # i 为慢指针 指向最新一个0元素的位置
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums

作者：sunfox
链接：https://leetcode.cn/problems/move-zeroes/solutions/168920/pythonti-san-chong-jie-fa-kuai-lai-kan-by-sunfox/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
