# 假设 nums1[i-1]<=nums2[j] 且 nums2[j-1]<=nums1[i]，nums1[:i] 和 nums2[:j] 就是最小的 i+j 个数
# 当 i+j==(m+n)//2 时，即找到了最小的一半数，即可求出中位数
# 因此遍历和为 (m+n)//2 的 <i, j> 对，找到满足 nums1[i-1]<=nums2[j] 且 nums2[j-1]<=nums1[i] 的即可
# 注意 i 递增时，nums1[i-1]、nums1[i] 递增，nums2[j]、nums2[j-1] 递减，因此遍历找到第一个满足 nums2[j-1]<=nums1[i] 的即可。

# 为了方便，当 m>n 时，可以交换 nums1、nums2 使得 m<=n，排除边界情况。

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        i, j = 0, (m+n) // 2
        while i < m and nums1[i] < nums2[j-1]:
            i += 1
            j -= 1
        left = max(nums1[i-1] if i else float('-inf'), nums2[j-1] if j else float('-inf'))
        right = min(nums1[i] if i<m else float('inf'), nums2[j]if j<n else float('inf'))
        return right if (m + n) % 2 else (left+right) / 2
    
# 简单方法：合并排序取中间
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums=nums2+nums1
        nums.sort()
        p=len(nums)
        if p%2==0:
            return (round(nums[p//2-1],5)+nums[p//2])/2
        else:
            o=nums[p//2]
            return o

