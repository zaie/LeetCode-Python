# 库函数
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse = True)[k - 1]
    
# 手写快速排序
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(left, right):
            pivot = nums[left]
            l = left + 1
            r = right
            while l <= r:
                if nums[l] < pivot and nums[r] > pivot:
                    nums[l], nums[r] = nums[r], nums[l]
                if nums[l] >= pivot:
                    l += 1
                if nums[r] <= pivot:
                    r -= 1
            nums[r], nums[left] = nums[left], nums[r]
            return r
        left = 0
        right = len(nums) - 1
        while 1:
            idx = partition(left, right)
            if idx == k - 1:
                return nums[idx]
            if idx < k - 1:
                left = idx + 1
            if idx > k - 1:
                right = idx - 1

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left, right, target = 0, len(nums) - 1, k - 1
        while True:
            pos = self.partition(nums, left, right)
            if pos == target:
                return nums[pos]
            elif pos > k: #要往左找
                right = pos - 1
            elif pos < k: #要往右找
                left = pos + 1
                
    def partition(self, nums, left, right):
        import random
        k = random.randint(left, right)
        pivot = nums[k]
        nums[left], nums[k] = nums[k], nums[left]
        index = left
        
        for i in range(left + 1, right + 1):
            if nums[i] > pivot:
                index += 1
                nums[i], nums[index] = nums[index], nums[i]
        nums[left], nums[index] = nums[index], nums[left]
        return index #此时所有index左侧的值都比nums[index]大， 所有右侧的值都比nums[index]小
