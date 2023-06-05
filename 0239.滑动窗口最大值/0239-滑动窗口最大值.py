1.利用双端队列记录当前滑动窗口的元素索引
2.队列最左侧元素记录滑动窗口中最大元素的索引
3.遍历数组：
    如果队列最左侧索引已不在滑动窗口范围内，弹出队列最左侧索引
    通过循环确保队列的最左侧索引所对应元素值最大
    新元素入队
    从第一个滑动窗口的末尾索引开始将最大值存储到结果res中
    
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
#         queue = collections.deque() #如果不用deque,用list也行
        queue=[]
        for i, num in enumerate(nums):
            if queue and queue[0] == i - k:
#                 queue.popleft()
                  queue.pop(0)
            while queue and nums[queue[-1]] < num: #比 nums[i] 小的都不要，因为只要窗口的最大值
                queue.pop()
            queue.append(i)
            if i >= k - 1:
                res.append(nums[queue[0]])
        return res

作者：郁郁雨
链接：https://leetcode.cn/problems/sliding-window-maximum/solutions/626777/239-hua-dong-chuang-kou-zui-da-zhi-li-yo-2jqr/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

#和上面相同，变量名称不同
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []

        window = []
        res = []
        for i in range(len(nums)):
            if window and window[0] <= i - k: #当前window头应该被弹出
                window.pop(0)
                
            while window and nums[window[-1]] < nums[i]: #比 nums[i] 小的都不要，因为只要窗口的最大值
                window.pop()
                
            window.append(i)
            if i >= k - 1:
                res.append(nums[window[0]])
        return res
