首先，要想找到第 i 位置最大面积是什么？
是以 i 为中心，向左找第一个小于 heights[i] 的位置 left_i；向右找第一个小于于 heights[i] 的位置 right_i，
即最大面积为 heights[i] * (right_i - left_i -1)
所以，我们的问题就变成如何找right_i 和 left_i？

# 暴力解法，会超时
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)
        for i in range(n):
            left_i = i
            right_i = i
            while left_i >= 0 and heights[left_i] >= heights[i]:
                left_i -= 1
            while right_i < n and heights[right_i] >= heights[i]:
                right_i += 1
            res = max(res, (right_i - left_i - 1) * heights[i])
        return res

# 单调栈
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0] #如果遍历之后，栈不为空，那么还需要一步：即弹出栈中所有元素，分别计算最大面积。然而当加了两个0以后，在结束后，栈一定为空！
        # 因为0入栈的时候，会把前面所有的数全部弹出，如果0最后一个入栈，所有的数都会弹出；头部加0便于处理当栈里只有一个有效元素要弹出的时候计算面积
        res = 0
        stack = []
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                top = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[top])

            stack.append(i)
        return res
