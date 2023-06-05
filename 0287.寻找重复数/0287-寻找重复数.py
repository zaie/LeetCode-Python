按题目表达，设数组长度为n，则数组中元素∈[1,n−1]，且只有一个重复元素。
一个直观的想法，设一个数字k∈[1,n−1]，统计数组中小于等于k的数字的个数count：

若count<=k，说明重复数字一定在(k,n−1]范围内。
若count>k，说明重复数字一定在[0,k]的范围内。
利用这个性质，我们使用二分查找逐渐缩小重复数字所在的范围。

1 初试化左右 数字 边界left=1,right=n−1
2 循环条件left<right:
    mid=(left+right)//2
    按照性质，统计数组中小于等于mid的元素个数count
    若 count<=mid，说明重复数字一定在(mid,right]的范围内。令left=mid+1
    若count>mid，说明重复数字一定在[left,mid]的范围内。令right=mid。
3 返回left

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = 1
        right = len(nums) - 1
        while(left<right):
            mid=(left+right)//2
            count=0
            for num in nums:
                if(num<=mid):
                    count+=1
            if(count<=mid):
                left=mid+1
            else:
                right=mid
        return left

作者：吴彦祖
链接：https://leetcode.cn/problems/find-the-duplicate-number/solutions/44868/er-fen-fa-kuai-man-zhi-zhen-zhu-xing-jie-shi-pytho/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
