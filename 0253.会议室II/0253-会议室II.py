# 给定一个会议时间安排的数组，每个会议时间都会包括开始和结束的时间 [[s1,e1],[s2,e2],…] (si < ei)，
# 为避免会议冲突，同时要考虑充分利用会议室资源，请你计算至少需要多少间会议室，才能满足这些会议安排。

# 题目给出若干区间，问最多有几个区间发生重叠。这个问题非常适合适用差分数组来求解。
# 具体来说，就是使用一个计数器cnt表示当前正在召开的会议，然后从小到大遍历所有的时间点。
# 若当前时间点有会议召开，那么就将cnt加上1，反之，若当前时间有会议结束，那么就将cnt减去1。
# 得到最新的cnt之后，则使用cnt来更新答案。

# 在这里需要特别注意的是，由于题目中的区间是左闭右开的，因此在计算cnt时如果碰到相同的时间点，则应该先处理结束的会议，再处理新召开的会议。
# 例如两场会议，时间分别是[1, 3)和[3, 5)，那么在3这个时间点应该先处理[1, 3)的结束，再处理[3, 5)的召开。

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        res = cnt = 0
        time_points = []
        for x, y in intervals:
            time_points.append([x, 1])
            time_points.append([y, 0])
        
        for t, p in sorted(time_points):
            if p == 0:
                cnt -= 1
            else:
                cnt += 1

            res = max(res, cnt)
        
        return res
