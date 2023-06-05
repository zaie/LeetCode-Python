# 很自然的想法，将原数组copy并排序，和原数组比对。

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums_copy=nums[:]
        nums_copy.sort()
        left=float("inf")
        right=0
        for i in range(len(nums)):
            if(nums_copy[i]!=nums[i]):
                left=min(left,i)
                right=max(right,i)
        return right-left+1 if(right-left+1 > 0) else 0

作者：吴彦祖
链接：https://leetcode.cn/problems/shortest-unsorted-continuous-subarray/solutions/45188/liang-ci-bian-li-pai-xu-bi-dui-python3-by-zhu_shi_/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
