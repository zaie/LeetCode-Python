# class Solution(object):
#     def nextPermutation(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         if not nums or len(nums) == 1:
#             return nums
#         # print nums, sorted(nums)[::-1]
#         if nums == sorted(nums)[::-1]:
#             nums[:] = nums[::-1]
#             return
        
#         i = len(nums) - 1
#         while(i - 1 >= 0 and nums[i - 1] >= nums[i]):
#             i -= 1
#         i -= 1    
#         tmp = nums[i]
#         j = len(nums) - 1
#         while(j >= i and nums[j] <= tmp):
#             j -= 1
#             if nums[j] > tmp:
#                 break

#         # print tmp, nums[j], nums[i]
#         nums[i], nums[j] = nums[j], nums[i]
#         # print nums
#         nums[i+ 1:] = nums[i + 1:][::-1]
#         return 
    
class Solution:
def nextPermutation(self, nums: List[int]) -> None:
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    if i >= 0:
        j = len(nums) - 1
        while j >= 0 and nums[i] >= nums[j]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    left, right = i + 1, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/next-permutation/solution/xia-yi-ge-pai-lie-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        
