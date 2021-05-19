# 直观解法
class Solution1(object):
    def searchRange(self, nums: List[int], target: int) -> List[int]:
            if target not in nums:
                return [-1, -1]
            ans = []
            for i in  range(len(nums)):
                if nums[i] == target:
                    ans.append(i)
                    break

            for i in range(len(nums)-1, -1, -1):
                if nums[i] == target:
                    ans.append(i)
                    break
            return ans

# 二分查找
# 思路：
# 二分查找算法就一种思想：减而治之（逐渐缩小问题规模），也可以视为「排除法」（一直排除一定不是目标元素的区间，思想依然是逐渐缩小搜索区间）；
# 根据看到的中间位置的元素的值 nums[mid] 可以把待搜索区间分为两个部分：「一定不存在目标元素的区间」和「可能存在目标元素的区间」。因此 mid 只可能被分到这两个区间的其中一个，即：while 里面的 if 和 else 就两种写法：
# 如果 mid 分到左边区间，即区间分成 [left..mid] 与 [mid + 1..right]，此时分别设置 right = mid 与 left = mid + 1；
# 如果 mid 分到右边区间，即区间分成 [left..mid - 1] 与 [mid..right]，此时分别设置 right = mid - 1 与 left = mid。
# 分类讨论的时候，不断排除不是目标元素的区间，以确定下一轮搜索的区间。即一直思考下一轮搜索区间是什么，以 左闭右闭区间 的形式表现出来，这样到底变化 left 还是变化 right，加不加 11 就会很清楚；
# 在退出循环的时候。如果区间一定存在目标元素，直接返回 left 或者 right。否则还需要单独做一次判断；
# 在循环体里，对 nums[mid] 与 target 的大小关系的判断需要分类讨论。
# 这里需要仔细一点，向左走还是向右走结果错了的话会导致整个结果都错。如果写成三个分支去判断；
# 最后要合并成两个分支。这样退出循环的时候，left 和 right 才会合并到一起。我们才可以不用纠结到底返回 left 还是返回 right。

# 作者：liweiwei1419
# 链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/si-lu-hen-jian-dan-xi-jie-fei-mo-gui-de-er-fen-cha/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution(object):
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return [-1,-1]
        left=0
        right=len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]<target:
                left=mid+1
            elif nums[mid]==target:
                right=mid
            else:
                right=mid-1
        if nums[left]!=target:
            return [-1,-1]
        l2=left
        r2=len(nums)-1
        while l2<=r2:
            m2=(l2+r2)//2
            if nums[m2]==target:
                l2=m2+1
            elif nums[m2]>target:
                r2=m2-1
        return [left,l2-1]
                    
                
            
