# 思路
# 如果我们按照区间的左端点排序，那么在排完序的列表中，可以合并的区间一定是连续的。

# 算法
# 我们用数组 merged 存储最终的答案。
# 首先，我们将列表中的区间按照左端点升序排序。然后我们将第一个区间加入 merged 数组中，并按顺序依次考虑之后的每个区间：
# 如果当前区间的左端点在数组 merged 中最后一个区间的右端点之后，那么它们不会重合，我们可以直接将这个区间加入数组 merged 的末尾；
# 否则，它们重合，我们需要用当前区间的右端点更新数组 merged 中最后一个区间的右端点，将其置为二者的较大值。

# 复杂度分析
# 时间复杂度：O(nlogn)，其中 nn 为区间的数量。除去排序的开销，我们只需要一次线性扫描，所以主要的时间开销是排序的 O(nlogn)。
# 空间复杂度：O(logn)，其中 nn 为区间的数量。这里计算的是存储答案之外，使用的额外空间。O(logn) 即为排序所需要的空间复杂度。


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/merge-intervals/solution/he-bing-qu-jian-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 原始解法
# class Solution(object):
#     def merge(self, intervals):
#         """
#         :type intervals: List[List[int]]
#         :rtype: List[List[int]]
#         """
#         if not intervals or not intervals[0]:
#             return intervals
        
#         intervals = sorted(intervals, key = lambda x:x[0])

#         res = []
#         start, end = intervals[0][0], intervals[0][1]
#         for interval in intervals:
#             s, e = interval[0], interval[1]
            
#             if s <= end: # overlap
#                 end = max(end, e)
#             else:
#                 res.append([start, end])
#                 start, end = s, e 

#         res.append([start, end])
#         return res
